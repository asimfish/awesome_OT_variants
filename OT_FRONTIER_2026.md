# Optimal Transport 前沿调研：截至 2026-07-30

## 0. 结论先行

过去两年的进展不宜概括成“又出现了更多 OT 变体”。更准确的变化有五个：

1. **系统层开始追上算法层**：FlashSinkhorn 把 stabilized Sinkhorn 写成 attention-like LogSumExp kernel，解决 GPU HBM IO，而不是发明一个新的 OT 目标。
2. **流形 OT 从离散求解走向 amortized neural map/coupling**：RNOT 与 Entropic RNOT 试图同时保留 intrinsic geometry、out-of-sample evaluation 和可扩展性。
3. **barycenter 重新分裂成 exact 与 scalable 两条路线**：一条用 Sobolev/Fisher–Rao 几何追求无熵偏差的精确解，另一条用 neural、sliced、linearized 或 regularized 方法换取高维规模。
4. **MMOT 的突破越来越依赖结构**：graph/Markov/dynamic/low-rank/collision，而不是显式存储 \(N^K\) tensor。
5. **OT、Schrödinger bridge 与 flow matching 正在汇合**：共同语言是 coupling、概率路径、速度场和参考过程，但三者的目标并不相同。

本报告把来源标记为：

- **正式论文**：已由会议/期刊公开接收；
- **预印本**：arXiv 工作，结论尚需更多独立验证；
- **软件**：官方实现的当前能力，不等同于论文全部理论。

## 1. FlashSinkhorn：它到底“Flash”在哪里

### 1.1 论文与状态

- Felix X.-F. Ye 等，[FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU](https://arxiv.org/abs/2602.03067)，ICML 2026 Oral。
- [官方 PyTorch + Triton 实现](https://github.com/ot-triton-lab/flash-sinkhorn)，当前公开 API 支持 balanced、unbalanced/semi-unbalanced、analytic gradient 与 streaming HVP。
- 本地原文与报告：`2602.03067_FlashSinkhorn/`。

### 1.2 数学并没有被替换

它求解的是离散 entropic OT：

\[
\mathrm{OT}_\varepsilon(a,b)
=\min_{P\in\Pi(a,b)}
\langle C,P\rangle+\varepsilon\mathrm{KL}(P\Vert a\otimes b),
\qquad C_{ij}=\|x_i-y_j\|^2.
\]

log-domain half-step 是

\[
f_i\leftarrow-\varepsilon\operatorname{LSE}_j
\left((g_j-C_{ij})/\varepsilon+\log b_j\right).
\]

平方欧氏代价分解为

\[
-C_{ij}/\varepsilon
=\frac{2x_i^\top y_j-\|x_i\|^2-\|y_j\|^2}{\varepsilon}.
\]

把行/列范数吸收到 shifted potentials 后，更新就是“dot-product score + bias”的 row-wise LogSumExp，与 attention softmax 的核心归约同构。

### 1.3 系统贡献

FlashSinkhorn：

- 不物化 \(n\times m\) cost/score/plan；
- 把点积、bias、online max/sum-exp、势函数更新融合进 Triton kernel；
- tile 在 on-chip SRAM 中流动，只把输入和最终势写入 HBM；
- transport-plan–vector/matrix product 同样 streaming；
- 通过 implicit/analytic differentiation 支持 gradient；
- 用 streaming conjugate-gradient 支持 Hessian–vector product。

论文给出的内存由 dense \(O(nm)\) 降到 \(O((n+m)d)\)。但每轮所有 pairwise interaction 仍要计算，所以算术量仍约为 \(O(nmd)\)；它是 **IO-optimal/IO-aware 的 dense interaction solver**，不是把二次 pairwise 计算变成真正的次二次算法。

### 1.4 实验结论应怎样读

论文在 A100-80GB 上报告相对 online baselines：

- forward 最高 \(32\times\)；
- end-to-end 最高 \(161\times\)；
- 大规模 gradient/HVP 和 OTDD/shuffled regression 明显受益；
- \(n=50{,}000,d=64\) 的 HVP 峰值内存仍按线性趋势增长。

这些是**特定硬件、维度、精度、迭代预算和 baseline backend** 下的结果。论文附录也显示：

- 小维度时 KeOps 更有竞争力；
- dense tensorized backend 在 cost matrix 能放入显存、且 \(d\) 很大时可能更快；
- 极端 rectangular aspect ratio 会削弱加速；
- 小 \(\varepsilon\) 不明显增加单轮时间，但会增加达到收敛所需的迭代数。

因此正确结论是：“在大 point-cloud、memory-bound、平方欧氏 EOT 场景下，它显著改写了工程可行边界”，而不是“它在所有 OT 问题上都快 32–161 倍”。

### 1.5 当前边界

- 只针对可化为 biased dot product 的 cost，公开高层 API 主要是 \(p=2\)；
- 求的是固定 \(\varepsilon>0\) 的 EOT/Sinkhorn divergence，不是 exact unregularized OT；
- 固定离散样本，不替代 streaming-sample Online Sinkhorn；
- 非欧氏 geodesic、GW 的四阶 cost、一般 learned cost 不能直接套同一 kernel；
- 更快的 half-step 不解决小 \(\varepsilon\) 下迭代条件数恶化。

### 1.6 值得做的复现实验

至少同时报告：

| 变量 | 建议取值 |
|---|---|
| \(n=m\) | 2k, 5k, 10k, 20k, 50k |
| \(d\) | 16, 64, 128, 512, 1024 |
| \(\varepsilon\) | 0.1, 0.05, 0.01 |
| backend | POT/CuPy、GeomLoss tensorized/online、OTT-JAX、FlashSinkhorn |
| stopping | 固定迭代与相同 marginal tolerance 各做一组 |
| 指标 | forward、forward+backward、峰值显存、marginal residual、objective gap |

若只比固定 10 次迭代的 wall time，不足以支持“求解器更快收敛”的结论。

## 2. “黎曼流形 + OT”其实有四种不同问题

### 2.1 Ground space 是 Riemannian manifold

数据本身位于 \((\mathcal M,g)\)，cost 取 intrinsic geodesic distance：

\[
c(x,y)=\tfrac12d_g(x,y)^2.
\]

例子包括：

- 球面 \(\mathbb S^d\)；
- rotation group \(\mathrm{SO}(3)\)；
- rigid motion \(\mathrm{SE}(3)\)；
- SPD covariance manifold；
- hyperbolic space。

这里的难点来自 exp/log map、cut locus、曲率、Fréchet mean 和 geodesic distance 的计算。

### 2.2 Wasserstein space 自身的“Otto Riemannian geometry”

即使 ground space 是欧氏空间，\(\mathcal P_2(\mathbb R^d)\) 也可形式化地看成无限维 Riemannian-like space。切向量由速度场表示，metric 来自动能：

\[
\|\dot\mu_t\|_{\mu_t}^2
=\inf_{v_t:\ \partial_t\mu_t+\nabla\cdot(\mu_tv_t)=0}
\int\|v_t\|^2\,d\mu_t.
\]

Benamou–Brenier、Wasserstein gradient flow、JKO scheme 和 barycenter 都在这条线上。它与“数据位于球面”不是同一个含义。

### 2.3 用 Riemannian optimization 求有限维 OT 相关问题

变量可能是：

- SPD matrix 上的 Bures–Wasserstein geometry；
- fixed-rank coupling/factor；
- Stiefel/Grassmann 上的 projection-robust OT；
- transport polytope 的某种 manifold parameterization。

这里“Riemannian”描述优化变量的约束几何，不一定表示 ground cost 是 geodesic。

### 2.4 Riemannian flow matching

向量场 \(v_t(x)\in T_x\mathcal M\)，插值沿 manifold geodesic，学习目标在 tangent metric 下回归。Chen–Lipman 的 [Flow Matching on General Geometries](https://proceedings.iclr.cc/paper_files/paper/2024/hash/d1f9936d3be6997ffffab692977eebe6-Abstract-Conference.html) 是 ICLR 2024 的基础工作；它是生成流方法，不自动等于求解 Monge OT。

## 3. 2025–2026 的流形 OT 主线

### 3.1 OT map 稳定性

Kitagawa、Letrouit、Mérigot 的 [Stability of optimal transport maps on Riemannian manifolds](https://arxiv.org/abs/2504.05412)（2025 预印本）研究固定 source、target 变化时，平方 Riemannian distance 下 map 与 Kantorovich potential 的定量稳定性。值得注意的是，其证明工具反过来使用了 entropic OT、谱方法与积分几何。

价值：为 empirical target、barycenter iteration、learned target perturbation 下的 map 误差提供理论接口。

### 3.2 RNOT：非熵、连续 neural map

Micheli 等，[Riemannian Neural Optimal Transport](https://arxiv.org/abs/2602.03566)（2026 预印本）：

- 先证明输出离散 map approximation 的方法在 manifold dimension 上必受 curse of dimensionality；
- 用连续 neural prepotential 与 intrinsic \(c\)-transform 构造 \(c\)-concave potential；
- 输出 intrinsic manifold-valued map；
- 在假设下给出网络规模对精度的次指数/多项式型保证。

关键优点：训练后可 out-of-sample evaluation，避免每个新 support 重做离散 OT。

关键限制：

- 理论集中于 compact manifolds；
- 正则性假设较强；
- 每次训练要解隐式 \(c\)-transform 的 inner minimization，训练明显比一些 baseline 慢；
- 实验维度仍有限，不能把 asymptotic guarantee 等同于已解决高维 manifold OT。

### 3.3 Entropic RNOT：学习 coupling，而非硬 map

Micheli、Sapora、Monod、Bhatt 的 [Entropic Riemannian Neural Optimal Transport](https://arxiv.org/abs/2605.04255)（2026 预印本）把 intrinsic EOT 与 amortization 合并：

- 从 semidual 学一个 target-side Schrödinger potential；
- 恢复 Gibbs conditional coupling；
- 在 Cartan–Hadamard manifold 上用 conditional Fréchet mean 做 barycentric projection；
- 在 stochastically complete manifold 上用 heat smoothing 得到连续 conditional surrogate；
- fixed \(\varepsilon>0\) 下证明 coupling recovery 与相应 surrogate 的稳定/收敛性质。

覆盖的实验几何包括 \(\mathbb S^2,\mathrm{SO}(3),\mathrm{SPD}(3),\mathrm{SE}(3),\mathbb H^2\)。其 scaling 实验显示 neural training 的资源主要由 minibatch 决定，而 full discrete manifold Sinkhorn 仍需 \(N^2\) cost matrix。

必须保留的边界：

- 正温度下自然对象是 coupling，不是确定性 map；
- barycentric projection/heat-smoothed mode 只是 conditional law 的摘要，会丢失多模态；
- 理论固定 \(\varepsilon>0\)，不覆盖 \(\varepsilon\to0\)；
- positive curvature 下 Fréchet mean 可能非唯一；
- docking 只是已有 pose ensemble 的 rigid \(\mathrm{SE}(3)\) refinement，不是 end-to-end docking，也没有 torsional flexibility。

### 3.4 Manifold barycentric projection

[Barycentric Projections of Optimal Transport Plans on Riemannian Manifolds](https://arxiv.org/abs/2606.07926)（2026-06 预印本）系统化了 coupling-to-map：

\[
T_{\mathrm{bar}}(x)
\in\arg\min_{z\in\mathcal M}
\int d_g(z,y)^2\,d\pi(y\mid x).
\]

它说明 intrinsic projection 是 squared geodesic loss 下的最佳确定性代表，并用 integrated conditional Fréchet variance 定义 Monge defect。该工作对解释 Entropic RNOT、manifold Sinkhorn 后怎样抽取 map 很重要。

### 3.5 生成模型分支

- [FlowMM](https://proceedings.mlr.press/v235/miller24a.html)，ICML 2024：把 Riemannian flow matching 用到 crystal 的 translation/rotation/permutation/periodicity。
- [Riemannian Variational Flow Matching for Material and Protein Design](https://openreview.net/forum?id=NlnDselrtl)，ICLR 2026：指出 velocity-only RFM objective 未显式包含由 Jacobi fields 编码的 curvature-dependent penalty，并发展 variational 版本。
- [Learning Manifold Data with Flow Matching](https://openreview.net/forum?id=9mA5d705Gd)，ICML 2026：从内在维度分析 flow matching transformer 的样本复杂度。

这些工作说明“流形”正在从一个 cost 替换项变成生成模型的 inductive bias，但它们不应与静态 Riemannian OT solver 混为一谈。

## 4. Barycenter：2026 应按六条路线读

### 4.1 经典与熵正则

\[
\bar\mu
\in\arg\min_\mu\sum_{i=1}^K\lambda_iW_2^2(\mu,\mu_i).
\]

传统主力是 LP、fixed/free-support iteration、entropic Bregman projection、convolutional barycenter 与 debiased Sinkhorn barycenter。POT 0.9.7 的[当前文档](https://pythonot.github.io/)同时提供 exact small-scale、entropic、debiased、free-support、GW/FGW barycenter 等实现。

### 4.2 Exact grid barycenter：Sobolev Gradient Ascent

Kim、Zhou、Zhu、Chen 的 [Sobolev Gradient Ascent for Optimal Transport](https://openreview.net/forum?id=IjL1xEoxXi) 是 ICLR 2026 正式论文：

- 推导 unconstrained concave dual；
- 不需要每轮执行昂贵的 \(c\)-concavity projection；
- 在 \(\dot H^1\) 几何下，gradient 通过 inverse Laplacian 得到；
- 规则网格上每轮约 \(O(KN\log N)\)；
- 给出 \(O(1/\sqrt T)\) 或带 \(\log T\) 的 global rate；
- 目标是 unregularized exact barycenter。

边界：依赖规则 grid、fast \(c\)-transform、FFT Poisson solver，主要面向 2D/3D；网格数对维度指数增长。

### 4.3 Exact heterogeneous barycenter：FRBary

Xu、Zhu、Chen 的 [A Unified Approach for Computing Wasserstein Barycenters of Discrete and Continuous Measures](https://arxiv.org/abs/2605.11270)（2026 预印本）：

- 在 Fisher–Rao geometry 下做 primal mirror descent；
- 同时接收 point cloud、连续密度及混合输入；
- 每轮解 semi-discrete/continuous OT 子问题；
- 离散输入也产生 absolutely continuous iterates；
- 在紧凸 support 上给出 \(O(\log T/\sqrt T)\) 型 objective convergence。

这是概念上很重要的“统一”，但当前实现主要验证 2D/3D，且 semi-discrete 子问题、密度表示和采样可能成为新瓶颈。

### 4.4 Signed barycenter

本地已精读 [The Signed Wasserstein Barycenter Problem](https://arxiv.org/abs/2602.05976)：

\[
\min_\mu\sum_i\lambda_iW_2^2(\mu,\mu_i),
\qquad \lambda_i\ \text{允许为负}.
\]

它服务于分布外推、measure-valued regression 和 Wasserstein gradient flow 的高阶时间离散。负权会破坏经典 convex/geodesic-convex 结构；当前贡献以存在性、对偶和充分条件为主，高维通用数值仍未成熟。

### 4.5 Robust、minimax 与公平

- [Robust Wasserstein barycenter](https://arxiv.org/abs/2603.07563)（2026 预印本）针对 outlier 敏感性和 moment assumption，给出 existence/consistency 与实验。
- [Wasserstein Ball Center](https://proceedings.mlr.press/v267/wang25be.html)（ICML 2025）把求和目标改为 min–max，使所有输入都落在最小半径 Wasserstein ball 内，面向 minority/fairness。

二者都不是经典 barycenter 的“更快 solver”，而是更换了统计目标。

### 4.6 Structured barycenter

- [Linearized Wasserstein Barycenters](https://proceedings.mlr.press/v258/werenski25a.html)，AISTATS 2025：在 LOT 切空间中获得闭式/低成本表达，但多维 representational capacity 仍有限。
- [Procrustes-Wasserstein barycenters](https://proceedings.mlr.press/v267/adamo25a.html)，ICML 2025：在刚体变换不变性下平均 point-cloud shape。
- 本地 `2604.22453_Adapted_Wasserstein_Barycenters_GP/`：对 Gaussian processes 保留 non-anticipative information structure。

### 4.7 一个实用选择表

| 数据/目标 | 首选 |
|---|---|
| 2D/3D 同一规则网格、需要高精度 exact | SGA |
| point cloud + density 混合输入、希望连续输出 | FRBary，先做规模验证 |
| 大规模经验分布、允许正则化 | Sinkhorn/debiased/free-support |
| 高维连续分布、需要 amortization | neural barycenter |
| 有 outlier | robust/trimmed/unbalanced barycenter |
| 需要外推或高阶时间格式 | signed barycenter |
| 时间序列/随机过程 | adapted barycenter |
| shape 需旋转/反射不变 | Procrustes-Wasserstein barycenter |
| 不希望 minority 被平均目标牺牲 | Wasserstein Ball Center |

## 5. Multi-marginal OT 的最新结构化方向

### 5.1 从“显式 tensor”转向“结构”

MMOT 的朴素 plan 是 \(N^K\)。当前可行方法基本都回答同一问题：cost/coupling 有什么结构可以避免这个 tensor？

- graph/tree factorization → message passing；
- Markov chain/path cost → dynamic programming / SB；
- low-rank tensor → factorized representation；
- samples only → stochastic/neural/MMD penalty；
- local exchange → collision dynamics；
- convex dynamic formulation → proximal splitting。

### 5.2 动态 MMOT

Pass、Shenfeld 的 [A dynamical formulation of multi-marginal optimal transport](https://arxiv.org/abs/2509.22494)（2025 预印本）：

- 对（半）凸 multi-marginal cost 给出 primal–dual dynamic formulation；
- 与固定初末 marginals 的 Benamou–Brenier 不同：从一个 source coupling 出发，只要求终点 coupling 的各 marginals 正确；
- 经 momentum 变量变换得到 convex optimization；
- 对 translation-invariant cost，从 dynamic flow 获得 quasi-Monge solution；
- 给出 proximal splitting 的 1D 数值实验。

限制：当前数值主要是低维 proof-of-concept；离散连续性方程可能产生负密度现象，细网格可缓解但规模问题仍在。

### 5.3 MMOT + Schrödinger bridge

- 本地扩展清单中的 [Momentum Multi-Marginal Schrödinger Bridge Matching](https://arxiv.org/abs/2506.10168) 面向多快照 trajectory inference。
- [Optimal and Scalable MAPF via MMOT and Schrödinger Bridges](https://arxiv.org/abs/2605.10917)（2026 预印本）利用 Markov structure 把匿名 multi-agent path finding 的 MMOT 化为多项式 LP，再用 entropic SB 产生 fractional template 并缩小整数 LP。

这条线的研究价值很高：多时间 marginal constraint 与动态 prior 天然属于 SB，而不是独立做 \(K-1\) 个 pairwise OT。

### 5.4 Collision 与 neural MMOT

- 本地 `2412.16385_CollisionDynamics_MultiMarginalOT/`：随机二元 swap，内存低、经验上快，但 stationary point 不等于 global optimum。
- [A deep learning approach to MMOT via Hilbert-space embeddings](https://arxiv.org/abs/2507.09206)：用 MMD penalty 近似 enforce marginals，适合 GPU，但把硬约束变成 penalty，并需要讨论 penalty bias。

### 5.5 一条必须记住的判断

“边缘数很多”不自动意味着要用 generic MMOT solver。先问：

1. cost 是否只连相邻时间？
2. 是否是 star cost / barycenter？
3. 是否有 tree-width 小的 factor graph？
4. 是否只需某些低阶 marginals/observable？
5. 是否能接受 entropic、MMD 或 local-collision approximation？

结构判断通常比优化器选择更重要。

## 6. 与既有六类调研的合并判断

现有 `OT_VARIANTS_SURVEY_REPORT.md` 的六类变体仍成立，但应加上新的“计算层”：

| 原类别 | 2026 新增重点 |
|---|---|
| MMOT | dynamic convex formulation、MM-SB、Markov/path structure |
| Barycenter | exact SGA、Fisher–Rao mirror descent、signed/robust/adapted |
| Partial OT | 理论保证、partial + fused GW |
| GW | metric/robust/partial GW、统一的 Z-GW、规模近似 |
| Schrödinger Bridge | multi-marginal、adjoint/reference-process design、生成建模统一 |
| Causal/adapted OT | adapted barycenter、随机过程 information structure |
| 新增：系统层 | FlashSinkhorn、native CUDA、IO-aware differentiation/HVP |
| 新增：几何层 | RNOT、Entropic RNOT、manifold barycentric projection、Riemannian FM |

## 7. 最值得继续做的三个研究问题

### 7.1 FlashSinkhorn × manifold OT

问题：能否对具有 dot-product representation 的 manifold distance 构造 IO-aware kernel？

可行切口：

- sphere 上 \(\arccos(\langle x,y\rangle)\) 的近似/分段 kernel；
- \(\mathrm{SO}(3)\) quaternion inner product；
- SPD 的 log-Euclidean tangent representation；
- intrinsic distance 与近似 embedding 的误差—速度权衡。

难点：一般 geodesic cost 不再是一个点积加 separable bias，且 cut locus/曲率会破坏简单 attention form。

### 7.2 Entropic RNOT × barycenter

问题：学习多个 target potentials，能否得到 amortized intrinsic barycenter？

必须解决：

- coupling summary 在 positive curvature 下可能非唯一；
- entropic bias 与 manifold curvature 的相互作用；
- 多输入时 shared representation 与权重条件化；
- out-of-sample measure，而不只是 out-of-sample point。

### 7.3 MMOT × adapted/SB

问题：多时间快照的 bridge 如何同时尊重 Markov prior 与 non-anticipative information？

这会连接：

- Multi_OT Ch.6 的多时间边缘；
- multi-marginal SB；
- adapted Wasserstein/causal coupling；
- trajectory/robot policy distribution。

理论难点是 path-space KL、filtration constraint 和多边缘约束同时存在；数值难点是不能用未来信息的 message passing / projection。

## 8. 阅读优先级

### 第一层：本周读

1. OT_book Ch.4；
2. FlashSinkhorn；
3. OT_book Ch.9.2；
4. SGA barycenter。

### 第二层：两周内

1. Multi_OT Ch.3、7；
2. dynamic MMOT；
3. RNOT；
4. Entropic RNOT。

### 第三层：按方向

- 生成/轨迹：Riemannian FM、SB foundations、multi-marginal SB；
- 数值精度：FRBary、signed barycenter；
- 图结构：partial/fused GW、Z-GW；
- 随机过程：adapted Wasserstein 与 adapted barycenter。

## 9. 复现工具栈

| 工具 | 合适场景 | 注意 |
|---|---|---|
| [POT](https://pythonot.github.io/) | 方法覆盖广、教学与 baseline | exact/regularized API 要分清 |
| [GeomLoss](https://www.kernel-operations.io/geomloss/) | PyTorch 大样本 Sinkhorn loss | online 与 tensorized backend 性能差异大 |
| [OTT-JAX](https://ott-jax.readthedocs.io/) | JAX 可微 OT、低层 solver 组合 | JIT warm-up 与设备同步要单独计时 |
| [FlashSinkhorn](https://github.com/ot-triton-lab/flash-sinkhorn) | NVIDIA GPU、大 point cloud、\(p=2\) EOT | PyTorch/Triton/CUDA 版本约束 |
| `facebookresearch/riemannian-fm` | Riemannian flow matching | 生成流，不是静态 OT baseline |

复现报告应固定 random seed，记录软件版本、GPU、精度模式、JIT warm-up、迭代/容差、是否形成 cost matrix、是否计算 gradient。

## 10. 最后判断

当前最值得投入的不是再收集一长串 OT 名词，而是抓住三条可互相验证的主线：

1. **计算主线**：Sinkhorn 数学 → log-domain → FlashSinkhorn IO；
2. **几何主线**：Wasserstein/Otto geometry → ground-manifold OT → RNOT/Entropic RNOT；
3. **多分布主线**：MMOT → barycenter → dynamic MMOT/MM-SB/adapted barycenter。

这三条线正好分别由 `OT_book`、`Multi_OT_book` 和随机过程/flow 材料支撑，也最容易形成可复现的研究问题。

