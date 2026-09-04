# OT 教材解读与交叉精读指南

> 版本核验与阅读建议基于本目录中的 PDF。本文的目标不是逐页缩写，而是回答三个问题：每本材料在讲什么、它与 OT 的哪条主线相连、应该以什么顺序深入。

## 1. 先给结论：这些材料如何分工

| 材料 | 文件与版本 | 对 OT 的作用 | 建议优先级 |
|---|---|---|---|
| Computational Optimal Transport | `book/OT_book.pdf`，Peyré–Cuturi，2020 版，209 页 | 计算 OT 的主教材：理论、对偶、Sinkhorn、动态 OT、barycenter、GW 等 | S |
| Numerical Methods for Multi-Marginal Optimal Transportation | `book/Multi_OT_book.pdf`，Luca Nenna 2016 博士论文，223 页 | MMOT 深入教材：多边缘 IPFP、流体、排斥代价、DFT | S |
| Discrete Stochastic Processes | `book/Discrete_Stochastic_Processes_Gallager_MIT_OCW.pdf`，Gallager，MIT OCW，392 页 | Markov、Poisson、renewal、martingale；连接离散 SB、路径空间 OT 和 RL | A |
| Essentials of Stochastic Processes | 附件 `随机过程.pdf`，Durrett，第 2 版草稿，226 页 | SB、causal/adapted OT 的随机过程基础；偏 Markov 链而非 SDE | A |
| 随机过程及其应用（第 2 版） | `book/随机过程_2.pdf`，陆大䋮、张颢；本地文件仅 18 页 | 工程型随机过程目录与开篇；全书重二阶过程、谱、滤波、Markov 链 | B；当前文件不完整 |
| Normalizing Flows for Probabilistic Modeling and Inference | `book/Flow_based.pdf`，JMLR 2021，64 页 | pushforward、可逆映射、连续流；连接 neural OT 与 flow matching | A |
| An Introduction to Variational Autoencoders | `book/VAE.pdf`，Kingma–Welling，2019，89 页 | 潜变量、ELBO、重参数化、IAF；生成模型背景 | B |
| Easy RL v1.0.6 | `book/EasyRL_v1.0.6.pdf`，2023，189 页 | MDP、策略梯度、PPO、DQN、模仿学习；连接 occupancy-measure OT | B |
| The Elements of Statistical Learning II | `book/ESLII圣经.pdf`，第 2 版，764 页 | 统计学习方法论、正则化、模型选择、无监督学习；OT 的统计参照系 | B |
| Writing for Computer Science | `book/writing4cs.pdf`，285 页 | 研究问题、证据、实验、写作与审稿 | A（研究工作流） |

建议把两本 OT 材料视为一套“主干 + 专题”：

```text
OT_book Ch.2–4
    │  Monge/Kantorovich → 对偶 → 熵正则 → Sinkhorn
    ├──────────────┐
    ▼              ▼
Multi_OT Ch.3,7    OT_book Ch.9
多边缘 IPFP         barycenter / gradient flow
    │              │
    └──────┬───────┘
           ▼
Multi_OT Ch.6 + OT_book Ch.7
动态 OT、流体、路径空间、Schrödinger 问题
           │
           ▼
2024–2026：FlashSinkhorn、RNOT、现代 barycenter、MMOT/SB
```

## 2. `OT_book` 深入解读

### 2.1 这本书真正教的是什么

它不只是一本 OT 理论简介。它建立了一个可反复使用的计算范式：

1. 用 coupling 把不可解或不存在的 Monge map 放松成凸问题；
2. 用对偶势函数把高维 transport plan 改写成低维变量；
3. 用熵正则把线性规划变成光滑、严格凸的 KL 投影；
4. 用 Sinkhorn 把投影化成矩阵缩放；
5. 对最优值或势函数求导，把 OT 嵌进机器学习；
6. 把同一语言扩展到 barycenter、unbalanced、MMOT、GW 和动态问题。

书中有三层叙述：离散直觉、离散测度、一般测度。第一次阅读时，不必在每个灰框的测度论细节上停住；先让离散公式成为“可运行的心理模型”，再回补一般情形。

### 2.2 必须掌握的五个对象

给定

\[
\alpha=\sum_{i=1}^n a_i\delta_{x_i},\qquad
\beta=\sum_{j=1}^m b_j\delta_{y_j},\qquad
C_{ij}=c(x_i,y_j),
\]

全书不断变换的其实是以下五个对象。

**1. Monge map**

\[
\min_{T:T_\#\alpha=\beta}\int c(x,T(x))\,d\alpha(x).
\]

它直观，但不允许质量分裂，离散情形常无可行映射。

**2. Kantorovich coupling**

\[
\min_{P\in U(a,b)}\langle C,P\rangle,\qquad
U(a,b)=\{P\ge 0:P\mathbf1=a,\ P^\top\mathbf1=b\}.
\]

这是计算 OT 的原点。`P` 是联合分布，不自动等于确定性 map。

**3. 对偶势**

\[
\max_{f,g}\langle f,a\rangle+\langle g,b\rangle
\quad\text{s.t.}\quad f_i+g_j\le C_{ij}.
\]

对偶不仅用于证明，也给出算法、梯度、统计解释和神经参数化入口。

**4. 熵正则 coupling**

\[
P_\varepsilon
=\arg\min_{P\in U(a,b)}
\langle C,P\rangle+\varepsilon\,\mathrm{KL}(P\Vert a\otimes b).
\]

等价于把 Gibbs kernel \(K_{ij}=e^{-C_{ij}/\varepsilon}\) KL 投影到 transport polytope。

**5. Sinkhorn scaling**

\[
P_\varepsilon=\operatorname{diag}(u)K\operatorname{diag}(v),\qquad
u\leftarrow a/(Kv),\quad v\leftarrow b/(K^\top u).
\]

`FlashSinkhorn` 没有改变这个优化问题；它改变的是上述更新在 GPU 上的实现方式。

### 2.3 逐章阅读地图

| 章 | 核心问题 | 必须带走的结论 | 阅读建议 |
|---|---|---|---|
| Ch.1 Introduction | OT 为什么适合数据科学 | ground geometry 会传递到分布空间；本书偏计算而非纯分析 | 快读 |
| Ch.2 Theoretical Foundations | Monge、Kantorovich、Wasserstein、对偶是什么 | coupling、pushforward、\(c\)-transform、Brenier map、1D 分位数公式 | 精读 |
| Ch.3 Algorithmic Foundations | 不加正则时怎样求解 | LP、互补松弛、transport polytope 顶点、network simplex、auction | 理论读，工程上了解边界 |
| Ch.4 Entropic Regularization | 为什么 Sinkhorn 快、稳、可微 | KL 投影、矩阵缩放、收敛、log-domain、\(\varepsilon\)-scaling、generalized Sinkhorn | 全书最重要，逐式复现 |
| Ch.5 Semidiscrete OT | 一边连续、一边离散怎么办 | Laguerre cells、半对偶、随机优化 | 对现代 barycenter/RNOT 很重要 |
| Ch.6 \(W_1\) OT | \(W_1\) 有何特殊结构 | Kantorovich–Rubinstein 对偶、流/图上的 \(W_1\) | 与 WGAN、图 OT 配合读 |
| Ch.7 Dynamic Formulations | 静态 coupling 如何变成流 | Benamou–Brenier 连续性方程、动量变量、proximal solver、路径空间 | 与 SB/flow matching 交叉精读 |
| Ch.8 Statistical Divergences | OT 与 KL、MMD 有何不同 | 样本复杂度、Hilbert 性、Sinkhorn 位于 OT 与 MMD 之间 | 做统计或 ML 必读 |
| Ch.9 Variational Wasserstein Problems | 如何对分布做优化 | OT loss 的梯度、barycenter、字典学习、Wasserstein gradient flow | barycenter 主章节 |
| Ch.10 Extensions | 哪些约束产生哪些 OT 变体 | MMOT、unbalanced、sliced、vector/matrix OT、GW | 建立研究选型地图 |

### 2.4 第 4 章应该怎样读

第 4 章有四条不能混淆的线。

#### A. 正则化极限

- \(\varepsilon\to 0\)：\(P_\varepsilon\) 收敛到原 OT 最优解集合中的最大熵解；
- \(\varepsilon\to\infty\)：\(P_\varepsilon\to a\otimes b\)，即独立 coupling；
- 小 \(\varepsilon\) 更接近原 OT，但收敛慢且数值容易 underflow；
- 大 \(\varepsilon\) 更平滑、更好算，但运输偏差更强。

所以“减小 \(\varepsilon\)”不是免费的精度按钮。

#### B. 代价、正则化代价和 Sinkhorn divergence

至少要区分：

\[
\mathrm{OT}_\varepsilon(\alpha,\beta),\qquad
\mathrm{OT}_0(\alpha,\beta),\qquad
S_\varepsilon(\alpha,\beta)
=\mathrm{OT}_\varepsilon(\alpha,\beta)
-\tfrac12\mathrm{OT}_\varepsilon(\alpha,\alpha)
-\tfrac12\mathrm{OT}_\varepsilon(\beta,\beta).
\]

前者有 entropic bias；第三个通过 self-cost 去偏。代码中 `debias=True` 通常返回的是 Sinkhorn divergence，而不是裸的正则化 OT。

#### C. log-domain 与 \(\varepsilon\)-scaling

直接存 \(K=e^{-C/\varepsilon}\) 在小 \(\varepsilon\) 下会下溢。实际实现应转到势函数

\[
u=e^{f/\varepsilon},\quad v=e^{g/\varepsilon},
\]

使用 log-sum-exp 更新，并常用从大到小的 \(\varepsilon\) continuation。FlashSinkhorn 正是在 stabilized log-domain 更新上做 IO-aware 融合。

#### D. 数学复杂度不等于硬件效率

传统分析以 FLOPs 和迭代数为中心；现代 GPU 上，大规模 Sinkhorn 往往先受 HBM 读写限制。FlashSinkhorn 的核心进展不是更少的 Sinkhorn 迭代，而是把平方欧氏代价写成

\[
-\|x_i-y_j\|^2
=2x_i^\top y_j-\|x_i\|^2-\|y_j\|^2,
\]

使每个 half-step 成为带 bias 的 row-wise LogSumExp，从而可像 FlashAttention 一样 tile、stream、fusion。

### 2.5 第 9 章与 barycenter

标准 \(p=2\) Wasserstein barycenter 是

\[
\bar\mu\in\arg\min_{\mu}\sum_{s=1}^{S}\lambda_s W_2^2(\mu,\mu_s),
\qquad \lambda\in\Delta_S.
\]

它不是密度逐点平均。它平均的是“移动质量所需的几何”，所以对平移的形状不容易产生欧氏平均那样的重影。

阅读时要沿三层区分：

1. **fixed-support barycenter**：候选 barycenter 的 support 已给，只优化权重；
2. **free-support barycenter**：同时优化 support 位置与权重；
3. **continuous barycenter**：直接在概率测度空间求解，通常借助半离散 OT、势函数或神经表示。

还要区分三种“近似”：

- 熵正则 barycenter：算的是正则化目标；
- debiased Sinkhorn barycenter：减轻 entropic shrinkage，但仍不是一般意义下 exact \(W_2\) barycenter；
- sliced/linearized/neural barycenter：通过投影、切空间或函数逼近换取可扩展性。

2025–2026 的一条明显趋势是重新追求**无熵正则的高精度 barycenter**：SGA 在规则网格上用 Sobolev 对偶梯度，FRBary 在 Fisher–Rao 几何下做 primal mirror descent；二者都在补本章“理论清晰、精确计算难”的缺口。

### 2.6 推荐的实操验收

完成下面四个实验，才算真正读完这本书的主线。

1. **1D exact OT**
   - 用排序/分位数计算 \(W_1,W_2\)；
   - 与线性规划结果核对；
   - 观察 Monge map 与 coupling 的差别。

2. **2D discrete Sinkhorn**
   - 自己实现 standard-domain 与 log-domain 版本；
   - 扫描 \(\varepsilon\)，记录 marginal residual、objective、稀疏度和迭代数；
   - 比较裸 EOT 与 Sinkhorn divergence。

3. **Barycenter**
   - 对几个平移高斯/图形比较像素平均、entropic barycenter、debiased barycenter；
   - 区分固定 support 和自由 support。

4. **动态 OT**
   - 在小网格上离散连续性方程；
   - 对比 displacement interpolation 与普通线性插值；
   - 再把扩散项加入，观察向 Schrödinger bridge 的过渡。

## 3. `Multi_OT_book` 深入解读

### 3.1 先看清它的身份

这不是 2026 年的新教程，而是 Luca Nenna 于 2016 年完成的博士论文。它的价值不在“覆盖最新算法”，而在于把以下三条线放在同一套数学里：

- 熵正则、Bregman projection、IPFP；
- 多边缘 OT、barycenter、流体动力学；
- 排斥型代价与 density functional theory。

其法文 introduction 后是英文主体。对只关心 MMOT 数值方法的读者，Part I 和 Part II 是核心；Part III 是非常有价值但更专业的物理专题。

### 3.2 MMOT 的基本问题

给定 \(K\) 个边缘分布，

\[
\min_{\gamma\in\Pi(\mu_1,\ldots,\mu_K)}
\int c(x_1,\ldots,x_K)\,d\gamma(x_1,\ldots,x_K).
\]

二边 OT 中的矩阵变成 \(K\) 阶 tensor。若每个边缘有 \(N\) 个点，朴素 plan 有 \(N^K\) 个元素；这就是 MMOT 的核心计算障碍。

Monge 型版本试图寻找

\[
(x,T_2(x),\ldots,T_K(x))_\#\mu_1,
\]

但 \(K>2\) 时 map 的存在、唯一性和结构比二边情形脆弱得多，严重依赖 cost 的 twist、对称性和排斥/吸引结构。

### 3.3 逐章阅读地图

| 部分/章 | 内容 | 真正价值 | 2026 视角 |
|---|---|---|---|
| Part I Ch.1 | 连续/离散 OT、Benamou–Brenier 回顾 | 为全论文统一记号 | 可与 OT_book Ch.2/7 对照 |
| Ch.2 | regularized OT 与 Schrödinger problem | 把熵正则解释为相对熵投影，不只是数值平滑 | 直接连接 SB |
| Ch.3 | Bregman alternating projection、IPFP、Dykstra | 全论文算法核心 | FlashSinkhorn 优化其二边 GPU 内核 |
| Ch.4 | barycenter、matching for teams、partial/capacity constraint | 展示“改约束，不改投影框架” | 仍是 generalized Sinkhorn 的基本模板 |
| Ch.5 | entropic Cournot–Nash equilibria | OT 与博弈/均衡的变分联系 | 专题选读 |
| Part II Ch.6 | Euler、Arnold/Brenier 原理、广义不可压流 | 把流体写成多时间边缘 OT | 与动态 MMOT、SB 最相关 |
| Ch.7 | MMOT 理论、对偶、几何、Gangbo–Święch cost、IPFP | MMOT 主章节 | 必读 |
| Ch.8 | repulsive harmonic/determinant cost | 展示多边缘特有的 fractal/非 Monge 结构 | 适合做理论研究 |
| Part III Ch.9 | DFT、Coulomb MMOT、SCE | 物理动机与严格关联 | DFT 方向必读 |
| Ch.10 | Seidl conjecture 与反例 | 告诉你“漂亮的 cyclic Monge ansatz 未必正确” | 理论警示价值很高 |
| Ch.11 | 1D/径向数值与反例 | 理论结构怎样进入实验 | 代码/数值方法已有年代感 |

### 3.4 generalized IPFP 的核心

对离散 MMOT 加熵正则后，

\[
\gamma_\varepsilon
\propto
K(x_1,\ldots,x_K)\prod_{k=1}^{K}u_k(x_k),
\qquad
K=e^{-c/\varepsilon}.
\]

每次更新一个 scaling \(u_k\)，使第 \(k\) 个边缘匹配 \(\mu_k\)；循环更新所有边缘就是多边缘 IPFP。抽象地，

\[
u_k
\leftarrow
\frac{\mu_k}{
\operatorname{Marginal}_k\left(
K\prod_{\ell\ne k}u_\ell
\right)}.
\]

关键不是公式难，而是分母的边缘化可能需要对 \(N^{K-1}\) 个元素求和。现代 MMOT 算法的主要问题因此变成：

- cost tensor 能否按链/树/低秩形式分解；
- 能否用 message passing 计算 marginal；
- 能否只访问样本、低秩因子或局部 swap；
- 能否通过动态/Markov 结构把指数问题降维。

所以“把 Sinkhorn 从二边照搬到多边缘”在数学上成立，但在计算上远远不够。

### 3.5 Dykstra 为什么重要

普通交替 KL 投影适合 affine marginal constraints。加入不等式、capacity、partial transport 等约束后，简单轮流投影可能不再得到对交集的正确 KL 投影。Dykstra correction 保存每个约束集的残差信息，修正循环投影。

应形成一个方法选择规则：

- 只有等式边缘约束：IPFP / Sinkhorn；
- 额外凸约束、上界或 partial/capacity 结构：Bregman–Dykstra；
- 非凸结构：投影框架只给局部或启发式保证，需要单独分析。

### 3.6 barycenter 是“隐藏的 MMOT”

平方欧氏代价下，可定义

\[
c(x_1,\ldots,x_K)
=\min_y\sum_{k=1}^K\lambda_k\|x_k-y\|^2,
\qquad
B(x_1,\ldots,x_K)=\sum_k\lambda_k x_k.
\]

若 \(\gamma^\star\) 是该 MMOT 的最优 coupling，则

\[
\bar\mu=B_\#\gamma^\star
\]

给出 Wasserstein barycenter。这个等价关系非常重要：

- barycenter 不只是“对 \(K\) 个二边 OT 求和”；
- 它可以看成先联合耦合所有边缘，再把联合样本映到欧氏重心；
- 它解释了 barycenter 与 matching for teams、共同 latent variable 的关系；
- 也解释了为什么 MMOT 的维度爆炸会传导到 barycenter。

### 3.7 Ch.6 的流体与路径空间

Arnold 原理把不可压 Euler 方程解释为体积保持微分同胚群上的测地线。Brenier 的放松把确定性流变成路径空间上的概率测度，并要求每个时间边缘保持 Lebesgue 测度。

离散时间后，多个时间切片就是多个 marginals：

\[
\gamma(x_{t_0},x_{t_1},\ldots,x_{t_K}),
\]

相邻状态代价之和近似动能。这条线同时通向：

- generalized incompressible flow；
- multi-marginal dynamic OT；
- 多时间快照 trajectory inference；
- 多边缘 Schrödinger bridge。

2025 年 Pass–Shenfeld 的动态 MMOT 不是简单复述本章：它对更一般的（半）凸 cost 给出 primal–dual 动态表述，并通过 convex formulation 产生 quasi-Monge 解；但 Nenna 的第 6 章是理解该工作的最佳前置材料。

### 3.8 排斥代价与 DFT 的要点

对吸引型平方代价，最优样本倾向聚集并常有较规则的 Monge 结构；对 Coulomb 或 repulsive harmonic cost，

\[
c(x_1,\ldots,x_K)
=\sum_{i<j}\frac{1}{\|x_i-x_j\|}
\quad\text{或}\quad
-\sum_{i<j}\|x_i-x_j\|^2,
\]

联合样本倾向彼此远离。多边缘结构在这里不是“多做几次二边匹配”，而是多体相关本身。

Part III 的核心认识是：在 strictly correlated electrons / 半经典极限中，电子密度给定，而电子联合分布的最小 Coulomb 排斥能可以写成相同边缘的 MMOT。这里的 transport plan 表示相关结构，不能随意压缩成 pairwise couplings。

### 3.9 这本书哪些地方已经需要现代补丁

1. **规模分析**：论文以显式 tensor/IPFP 为中心；现代工作更强调 graph-structured cost、low-rank、message passing、sampling 和 GPU kernel。
2. **熵正则偏差**：今天应同时考虑 Sinkhorn divergence、debiased barycenter 和 exact/unregularized solver。
3. **自动微分**：2016 版本没有系统覆盖 implicit differentiation、analytic gradient、HVP。
4. **神经参数化**：neural OT、RNOT、flow matching、amortized barycenter 是后续主线。
5. **动态 MMOT**：最新工作给出了更一般 cost 的动态凸表述，并与 quasi-Monge 解联系。

### 3.10 建议的精读顺序

不要从头线性读到尾。建议：

1. OT_book Ch.2、Ch.4；
2. Multi_OT Ch.1–3；
3. Multi_OT Ch.7.1–7.4；
4. OT_book Ch.9.2 与 Multi_OT Ch.4.1、7.3.1、7.5.1；
5. OT_book Ch.7 与 Multi_OT Ch.6；
6. 根据方向分叉：
   - 算法：Ch.7.4 + 新版 scalable MMOT；
   - 流体/SB：Ch.6；
   - 理论/反例：Ch.8、10；
   - 量子/DFT：Ch.9–11。

## 4. 其余教程的解读

### 4.1 `Flow_based.pdf`

这是 Papamakarios 等人的 normalizing-flow 综述。主线为：

- 可逆可微变换 \(x=T(u)\)；
- change of variables
  \[
  p_X(x)=p_U(T^{-1}(x))|\det J_{T^{-1}}(x)|;
  \]
- finite compositions：autoregressive、coupling、residual flows；
- continuous-time transformations：CNF/ODE；
- 离散变量、流形等推广；
- density estimation、VI、生成与监督学习应用。

与 OT 的关系：

- 二者都使用 pushforward map；
- normalizing flow 主要优化 likelihood/KL，任意满足目标分布的 diffeomorphism 都可以；
- Monge OT 还要求在给定 cost 下最优，平方欧氏情形的最优 map 具有 Brenier 结构；
- flow matching 学习的是一条概率路径/速度场；OT coupling 常用于让训练路径更直；
- Riemannian flow matching 把速度场和 geodesic 放到流形切空间，但不等同于静态 OT 求解器。

建议精读 Sec.2、Sec.4、Sec.5；有限 flow 架构细节按研究需要选读。

### 4.2 `VAE.pdf`

主线为：

\[
p_\theta(x,z)=p_\theta(x\mid z)p(z),\qquad
\log p_\theta(x)\ge
\mathbb E_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
-\mathrm{KL}(q_\phi(z\mid x)\Vert p(z)).
\]

核心内容：

- encoder 是近似 posterior，不只是压缩器；
- ELBO 同时包含重建项与 posterior regularization；
- 重参数化 \(z=\mu_\phi(x)+\sigma_\phi(x)\odot\epsilon\) 让随机节点可反传；
- IAF/normalizing flow 提升 posterior expressiveness；
- 多层 latent model 会带来 inference 与 posterior collapse 等困难。

与 OT 的关系：

- 原始 VAE 的 discrepancy 是 KL，不是 Wasserstein；
- WAE 从 aggregate posterior 与 prior 的匹配角度引入 OT 式 autoencoding 目标；
- SB/flow matching 通常直接学习分布间动态，而 VAE 先引入 latent variable；
- 读 VAE 的价值是建立“变分推断—生成模型—潜空间”语言，不应把 ELBO 当 OT 目标。

### 4.3 `EasyRL_v1.0.6.pdf`

本版覆盖 13 章：MDP、表格方法、策略梯度、PPO、DQN 及改进、连续动作、actor–critic、稀疏奖励、模仿学习、DDPG/TD3、AlphaStar。

与 OT 最相关的是：

- Ch.2：状态/动作/策略/occupancy measure 的概率基础；
- Ch.4–5：策略梯度、importance ratio、trust-region/proximal 思想；
- Ch.9：pathwise derivative 与 actor–critic；
- Ch.10：curriculum 可用 Wasserstein 距离设计任务进度；
- Ch.11：模仿学习可把 expert 与 policy 的 occupancy measure 做 OT 对齐；
- Ch.12：连续控制与 SB/stochastic control 的应用接口。

这不是 OT 教材。若主线是 OT，只需精读 Ch.2、4、5、9、11、12。

### 4.4 `ESLII圣经.pdf`

全书 18 章，从 supervised learning、线性模型与正则化，覆盖 kernel smoothing、模型选择、boosting、神经网络、SVM、无监督学习、随机森林、ensemble、无向图模型与高维统计。

对 OT 研究最有用的不是某个公式，而是统计判断框架：

- Ch.2、7：bias–variance、泛化误差、交叉验证；
- Ch.3、5：regularization path 与函数空间；
- Ch.6：kernel/MMD 的参照系；
- Ch.8：bootstrap、模型平均与不确定性；
- Ch.14：聚类、MDS、manifold learning、ICA；
- Ch.18：\(p\gg N\) 时的估计风险。

OT 方法常在训练集上得到漂亮几何图，但研究是否成立取决于样本复杂度、正则选择、统计稳定性和 out-of-sample 评估；ESL 用来补这部分。

### 4.5 三份随机过程材料

#### `book/Discrete_Stochastic_Processes_Gallager_MIT_OCW.pdf`

这是本次新增的合法开放教材：Robert G. Gallager 的 *Discrete Stochastic Processes*（第 2 版草稿），来自 MIT OpenCourseWare 6.262。正文 392 页，官方课程同时提供视频、习题和解答；来源、许可与文件校验见 `book/OPEN_SOURCE_BOOKS.md`。

全书的主线是：

- 概率论复习与随机过程建模；
- Bernoulli、Poisson 过程；
- 有限状态与可数状态 Markov 链；
- renewal process、renewal-reward 与排队直觉；
- random walk、martingale 和 stopping。

它比当前 18 页中文节选完整，也比 Durrett 更贴近工程、通信和排队应用。对 OT 的直接价值是把 Markov kernel、路径概率、动态规划和 martingale 语言补齐，从而更顺畅地进入 Schrödinger bridge、causal/adapted OT 与 occupancy-measure OT。它仍不是 diffusion/SDE 专著：深入连续扩散桥时需要另补 Brownian motion、Itô calculus、Girsanov 与 Fokker–Planck。

#### 附件：Durrett

章节是 Markov chains、Poisson processes、renewal processes、continuous-time Markov chains、martingales、mathematical finance。优点是以例子和计算为主，适合建立：

- transition kernel、stationary distribution、reversibility；
- generator 与连续时间链；
- hitting/exit time；
- martingale、stopping time；
- Metropolis–Hastings。

它能支撑离散 SB、CTMC bridge 与 causal/adapted OT 的入门，但 Brownian motion/SDE 只在金融章短暂出现；若要深入 diffusion SB，还需补 Itô calculus、Girsanov、Fokker–Planck 和 path-space relative entropy。

#### `book/随机过程_2.pdf`

它是《随机过程及其应用（第 2 版）》的 18 页节选，不是完整 297 页正文。目录显示全书包括：

- 二阶矩过程的时域分析；
- Gauss 过程；
- Poisson 过程；
- Fourier 谱分析；
- 最优线性估计、Wiener/Kalman filtering；
- 离散/连续时间 Markov 链。

该书偏电子信息工程，对信号、相关函数、功率谱和滤波很强；对 SB 更需要的是 Markov、Kolmogorov 方程和 Gauss 过程部分。由于当前 PDF 不完整，不能据此完成逐章精读。

### 4.6 `writing4cs.pdf`

这本书覆盖从选题、阅读和审稿，到 hypothesis/evidence、论文结构、数学与算法书写、图表、实验、统计原则、演讲和伦理。

对当前 OT 调研最重要的检查表：

1. 每篇论文分开写“problem / claim / evidence / limitation”；
2. 理论改进、数值改进、硬件优化不能混写成同一种 SOTA；
3. speedup 必须报告硬件、精度、迭代数、收敛容差和 baseline backend；
4. barycenter 实验必须说明 exact/regularized/debiased、fixed/free support；
5. manifold 实验必须说明 intrinsic cost、metric、cut locus/曲率假设；
6. 预印本、正式录用和开源复现状态应分开标注。

## 5. 一条可执行的 12 周路线

| 周 | 理论阅读 | 实验/输出 |
|---|---|---|
| 1 | OT_book Ch.2 | 1D OT、LP、对偶互补松弛 |
| 2 | OT_book Ch.3–4.2 | 手写 Sinkhorn，检查 marginals |
| 3 | OT_book Ch.4.3–4.6 | log-domain、\(\varepsilon\)-scaling、Sinkhorn divergence |
| 4 | Multi_OT Ch.1–3 | generalized IPFP、Bregman/Dykstra 小例子 |
| 5 | Multi_OT Ch.7 | 三边缘小 tensor、对偶与 cost 结构 |
| 6 | OT_book Ch.9.2 + Multi_OT barycenter 小节 | fixed/free-support barycenter 对比 |
| 7 | OT_book Ch.7 + Multi_OT Ch.6 | displacement interpolation、动态约束 |
| 8 | Gallager Ch.3–7；Durrett Ch.1、4、5 作互补 | Markov kernel、renewal、generator、martingale 习题 |
| 9 | Flow review Sec.2、4、5 | CNF 与 OT map 的差别说明 |
| 10 | FlashSinkhorn 论文 | POT/GeomLoss/FlashSinkhorn benchmark 设计 |
| 11 | RNOT/Entropic RNOT | 球面或 SPD 上 intrinsic vs tangent baseline |
| 12 | SGA/FRBary + 动态 MMOT | 形成个人研究问题、复现实验与阅读报告 |

## 6. 深入研究前的自测问题

如果以下问题能不看资料回答，说明主干已经建立：

1. 为什么 Kantorovich relaxation 是凸的，而 Monge 问题通常不是？
2. 为什么 \(P_\varepsilon=\mathrm{diag}(u)K\mathrm{diag}(v)\)？
3. 小 \(\varepsilon\) 为什么同时提高 OT fidelity、降低数值稳定性和收敛速度？
4. regularized OT cost 与 Sinkhorn divergence 有什么不同？
5. barycenter 为什么可以写成一个隐藏的 MMOT？
6. generalized IPFP 的公式看似简单，为什么仍有 \(N^K\) 障碍？
7. Benamou–Brenier、Schrödinger bridge、flow matching 分别优化什么对象？
8. “OT on a Riemannian manifold”和“Wasserstein space has a Riemannian structure”为什么不是同一句话？
9. entropic coupling 为什么通常没有唯一的确定性 map？barycentric projection 丢掉了什么？
10. FlashSinkhorn 改变的是数学目标、迭代复杂度，还是硬件 IO 路径？
