# Optimal Transport 深度调研与学习资源目录（2026）

> 检索截止：2026-07-31（Asia/Shanghai）；会议覆盖口径最近复检：2026-09-05（结论无变化；历次复检 08-14、08-25、09-05）  
> 范围：经典 OT、熵正则与高性能 Sinkhorn、unbalanced/partial OT、Wasserstein barycenter、MMOT、Gromov-Wasserstein、黎曼流形 OT、Schrödinger bridge、flow matching、统计 OT，以及视觉/RL/生物信息应用。  
> 定位：这是一份“先建立坐标系，再追前沿”的研究导航，不是论文标题的无差别堆积。

本版共整理 **111 篇正式论文集论文或官方已接收论文**、**11 篇需继续跟踪的前沿预印本**，另含主教材、经典论文链、课程、博客、软件和专题阅读路线。数量只用于检查覆盖度，不能替代对论文贡献质量的判断。

## 0. 证据等级与会议覆盖口径

### 0.1 状态标签

| 标签 | 含义 | 可如何表述 |
|---|---|---|
| **[P] Proceedings** | 已进入会议或期刊正式论文集 | “发表于/收录于” |
| **[A] Accepted** | 官方会议 OpenReview 已明确给出接收类型，但论文集页面尚未稳定归档 | “已被接收为” |
| **[R] Preprint** | arXiv/作者稿，未在所给来源中核实正式接收 | 只能称“预印本” |
| **[B] Book/Notes** | 教材、讲义或综述 | 用于学习，不计作前沿会议成果 |

判断会议归属以官方 proceedings、CVF/ECVA、AAAI OJS 或会议官方 OpenReview 为准；仅在 arXiv 摘要中写 “submitted to” 或在搜索结果中带会议关键词，不算接收证据。

### 0.2 用户指定会议的时间覆盖

| 会议 | 本目录覆盖 | 截止日状态说明 |
|---|---|---|
| NeurIPS | 2024、2025 | 2026 论文集尚未发布，不虚构 2026 条目 |
| ICML | 2024、2025、2026 | 2024–2025 用 PMLR；2026 用官方已接收 OpenReview |
| ICLR | 2024、2025、2026 | 2024 用 proceedings；2025–2026 用官方已接收 OpenReview |
| ECCV | 2024 | ECCV 为双年会；2026 截止日尚无正式论文集 |
| ICCV | 2025 | ICCV 为双年会；2024、2026 本来就不是常规举办年份 |
| CVPR | 2024、2025、2026 | 均使用 CVF Open Access 正式页面 |
| AAAI | 2024、2025、2026 | 均使用 AAAI OJS 正式论文集 |

因此，“最近两年”在双年会和不同截稿日下不能机械解释为每个会议每年都有论文。本目录以 2024-01-01 至 2026-07-31 的实际正式记录为准。

## 1. 先建立 OT 研究地图

| 主线 | 数学对象/目标 | 先修知识 | 计算入口 | 当前前沿问题 |
|---|---|---|---|---|
| 经典 Monge–Kantorovich | 两个概率测度间的耦合与运输代价 | 测度、凸分析、LP、对偶 | LP、半离散 OT | 可扩展精确算法、统计误差 |
| Entropic OT | \(OT_\varepsilon\) 与 KL 正则 | 对偶、矩阵缩放 | Sinkhorn、log-domain、\(\varepsilon\)-scaling | GPU I/O、低精度、稀疏/块算法 |
| UOT / partial OT | 允许质量生成、消失或只匹配一部分 | divergence、凸优化 | generalized Sinkhorn、Dykstra | 鲁棒性、参数可解释性、半离散算法 |
| Wasserstein barycenter | Fréchet 均值 \(\arg\min_\nu\sum_s\lambda_s W_p^p(\nu,\mu_s)\) | OT、变分法 | fixed/free support、dual ascent | 精确 barycenter、流形/概率过程 barycenter |
| MMOT | 多于两个边缘的联合耦合 | 高维 tensor、对偶、结构化代价 | generalized IPFP、动态规划、低秩 | 维数灾难、动态 formulation、SB |
| GW / FGW | 比较不同底空间的内部关系 | metric measure space | conditional gradient、entropic GW | relaxation、对称性、图/形状对齐 |
| 黎曼流形 OT | intrinsic geodesic cost 上的 transport | 黎曼几何、指数/对数映射 | manifold Sinkhorn、neural dual | cut locus、曲率、可扩展 intrinsic solver |
| Wasserstein gradient flow | 概率测度空间上的动力学 | PDE、变分法 | JKO、粒子法、proximal sampler | 非测地凸、二阶法、采样 |
| Schrödinger bridge | 路径空间相对熵最小化 | Markov、SDE、Girsanov | IPF、SB matching | 多边缘/动量/流形 SB、生成建模 |
| Flow matching | 学习连续速度场 pushforward | ODE/CNF、连续性方程 | conditional FM、simulation-free | OT coupling、一般几何、离散数据 |
| Statistical OT | 估计误差、sample complexity、CLT | 经验过程、非参数统计 | plug-in、regularized estimator | dimension dependence、隐私、鲁棒推断 |

几个最容易混淆的边界：

- **OT map ≠ 任意 normalizing flow**：前者还满足特定代价下的最优性；
- **entropic barycenter ≠ 精确 Wasserstein barycenter**：固定 \(\varepsilon\) 会改变目标并可能带来 blur/bias；
- **切空间近似 ≠ intrinsic manifold OT**：在曲率大、分布跨越 cut locus 时差异会放大；
- **multi-marginal static OT ≠ path-space SB**：后者还指定参考随机动力学并优化路径相对熵；
- **硬件 speedup ≠ 算法复杂度改进**：需要分别报告 I/O、迭代数、误差、精度和硬件。

## 2. 基础教材、讲义和综述

### 2.1 主教材

| 优先级 | 资料 | 类型 | 适合解决什么问题 |
|---|---|---|---|
| S | [Peyré & Cuturi, *Computational Optimal Transport*](https://optimaltransport.github.io/book/)；[官方 PDF](https://optimaltransport.github.io/pdf/ComputationalOT.pdf) | [B] 免费在线书 | 离散 OT、对偶、Sinkhorn、动态 OT、GW、barycenter 的计算主线；本地已有 `book/OT_book.pdf` |
| S | Luca Nenna, *Numerical Methods for Multi-Marginal Optimal Transportation*；本地 `book/Multi_OT_book.pdf` | [B] 博士论文 | 多边缘 IPFP、结构化代价、流体与 DFT；MMOT 精读主线 |
| S | [Gabriel Peyré, *Optimal Transport for Machine Learners*](https://www.gpeyre.com/ot4ml/)；[arXiv PDF](https://arxiv.org/pdf/2505.06589) | [B] 2025–2026 在线教材 | 比 2019 书更贴近当前 ML：带可运行 notebook、图示与现代生成模型连接 |
| A | [Chewi, Niles-Weed & Rigollet, *Statistical Optimal Transport*](https://arxiv.org/abs/2407.18163) | [B] 2024/2025 讲义 | sample complexity、极限定理、统计估计；用于判断“几何漂亮”是否统计可靠 |
| A | [Santambrogio, *Optimal Transport for Applied Mathematicians*（作者稿）](https://math.univ-lyon1.fr/~santambrogio/OTAM-cvgmt.pdf) | [B] 理论教材 | Kantorovich 对偶、Brenier、Benamou–Brenier、Wasserstein gradient flow |
| A | [Figalli, *An Introduction to Optimal Transport and Wasserstein Gradient Flows*](https://people.math.ethz.ch/~afigalli/lecture-notes-pdf/An-introduction-to-optimal-transport-and-Wasserstein-gradient-flows.pdf) | [B] 讲义 | 从最优映射走到 continuity equation、JKO 和梯度流 |
| A | [Mérigot & Thibert, *Optimal Transport: Discretization and Algorithms*](https://arxiv.org/abs/2003.00855) | [B] 数值讲义 | 半离散 OT、Laguerre cells、离散化与数值算法 |
| A | Gallager, *Discrete Stochastic Processes*；本地 `book/Discrete_Stochastic_Processes_Gallager_MIT_OCW.pdf` | [B] MIT OCW 开放教材 | Markov、Poisson、renewal、martingale；给 SB、causal/adapted OT 和 RL 打基础 |
| B | Villani, *Topics in Optimal Transportation* / *Optimal Transport: Old and New* | [B] 理论经典 | 深入正则性、几何和概率；不建议作为第一本计算 OT 教材 |
| B | Ambrosio, Gigli & Savaré, *Gradient Flows* | [B] 专著 | metric-space gradient flow 与 Wasserstein PDE 的严格理论 |

### 2.2 经典论文链：按问题而不是按年代读

| 主题 | 基础文献 | 阅读时抓住的核心 |
|---|---|---|
| 映射与对偶 | Brenier, “Polar factorization and monotone rearrangement of vector-valued functions” (1991) | 二次代价下最优映射是凸势梯度；理解 map 存在性与唯一性的入口 |
| 动态 OT | [Benamou & Brenier, “A Computational Fluid Mechanics Solution to the Monge–Kantorovich Mass Transfer Problem”](https://doi.org/10.1007/s002110050002) (2000) | \(W_2\) 的动能最小化与 continuity equation |
| 熵正则 | [Cuturi, “Sinkhorn Distances”](https://proceedings.neurips.cc/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html) (NeurIPS 2013) | 把矩阵缩放引入可扩展 OT；明确算的是 regularized OT |
| Sinkhorn bias | [Feydy et al., “Interpolating between OT and MMD using Sinkhorn Divergences”](https://proceedings.mlr.press/v89/feydy19a.html) (AISTATS 2019) | debias 后的 Sinkhorn divergence、极限与正定性 |
| 统计复杂度 | [Genevay et al., “Sample Complexity of Sinkhorn Divergences”](https://proceedings.mlr.press/v89/genevay19a.html) (AISTATS 2019) | \(\varepsilon\)、维度、样本量之间的偏差—方差折中 |
| UOT | Chizat et al., “Scaling Algorithms for Unbalanced Transport Problems” (2018) | relaxed marginal、generalized Sinkhorn 与不同 divergence |
| barycenter | [Agueh & Carlier, “Barycenters in the Wasserstein Space”](https://doi.org/10.1137/100805741) (2011) | barycenter 的定义、存在性、对偶和 \(W_2\) 几何 |
| debiased barycenter | [Janati et al., “Debiased Sinkhorn Barycenters”](https://proceedings.mlr.press/v119/janati20a.html) (ICML 2020) | 熵正则 barycenter 的 shrinkage/blur 及 debias |
| GW | [Peyré, Cuturi & Solomon, “Gromov-Wasserstein Averaging of Kernel and Distance Matrices”](https://proceedings.mlr.press/v48/peyre16.html) (ICML 2016) | 不同空间之间比较结构、GW barycenter |
| MMOT | [Pass, “Multi-marginal Optimal Transport: Theory and Applications”](https://doi.org/10.1051/cocv/2014010) (2015) | 多边缘问题相较二边缘为何难、结构性解与应用 |
| SB 综述 | [Léonard, “A Survey of the Schrödinger Problem and Some of Its Connections with Optimal Transport”](https://doi.org/10.3934/dcds.2014.34.1533) (2014) | Schrödinger problem、entropic OT、large-deviation 极限 |
| Flow matching | [Lipman et al., “Flow Matching for Generative Modeling”](https://openreview.net/forum?id=PqvMRDCJT9t) (ICLR 2023) | simulation-free vector-field regression 和 probability path |
| 一般几何 FM | [Chen & Lipman, “Flow Matching on General Geometries”](https://proceedings.iclr.cc/paper_files/paper/2024/hash/d1f9936d3be6997ffffab692977eebe6-Abstract-Conference.html) (ICLR 2024) | geodesic conditional paths、流形上的 flow matching |

推荐的最低限度推导顺序：

1. Kantorovich primal/dual 与 complementary slackness；
2. 二次代价下 Brenier map；
3. 熵正则 primal、dual 与 Sinkhorn scaling；
4. Benamou–Brenier continuity equation；
5. barycenter 与 JKO；
6. entropic OT 的 path-space 解释；
7. MMOT/GW/流形 OT 再分叉。

## 3. 2024–2026 正式会议论文目录

### 3.1 NeurIPS

#### NeurIPS 2024 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Progressive Entropic Optimal Transport Solvers](https://proceedings.neurips.cc/paper_files/paper/2024/hash/22b6bc18be9c2bfaa48adc1122f0a971-Abstract-Conference.html) | Sinkhorn | progressive regularization；研究速度时要与固定 \(\varepsilon\) 目标区分 |
| ⭐ [Expectile Regularization for Fast and Accurate Training of Neural Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d885c74aa0e00cc07a35346aa7988e34-Abstract-Conference.html) | neural OT | 用 expectile 目标改善 neural OT 训练的速度与精度 |
| [Light Unbalanced Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2024/hash/aa93a55655e49cc8bf8e6e9295d9b295-Abstract-Conference.html) | UOT | 面向大规模 UOT 的轻量化近似 |
| ⭐ [Semidefinite Relaxations of the Gromov-Wasserstein Distance](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8189d86a5d8dea0694d43bb90e01c14d-Abstract-Conference.html) | GW | 从非凸 GW 到可认证 relaxation；适合研究 lower bound/全局性 |
| [A Combinatorial Algorithm for Semi-Discrete Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2d950a2cfd8a75124c178a89545b97fd-Abstract-Conference.html) | 半离散 OT | 与主流 smooth dual/Newton 法不同的组合算法路径 |
| [Bisimulation Metrics are Optimal Transport Distances, and Can be Computed Efficiently](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f257fe05388ba5d98b7c6089b1841bd0-Abstract.html) | RL / metric | 把状态抽象中的 bisimulation metric 纳入 OT 统一视角 |
| [Non-geodesically-convex Optimization in the Wasserstein Space](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1e1cf05517b959c1ce5934734efc421b-Abstract-Conference.html) | Wasserstein optimization | 不依赖测地凸的优化分析，连接概率测度空间算法 |
| [OPEL: Optimal Transport Guided Procedure Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6e4b14e76d0d4f42a9dff031a7a8417b-Abstract-Conference.html) | 序列/模仿 | OT 对齐过程轨迹的应用实例 |

#### NeurIPS 2025 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Efficient Algorithms for Robust and Partial Semi-Discrete Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3e8f3ca5a82f5511370af7ed0efcad0f-Abstract-Conference.html) | partial / semi-discrete | 同时处理 outlier、部分匹配和连续—离散结构 |
| [Variational Regularized Unbalanced Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2025/hash/18aee41e1bb41bbb8fee53cfff8138b7-Abstract-Conference.html) | UOT | 从变分正则角度理解 UOT |
| ⭐ [Momentum Multi-Marginal Schrödinger Bridge Matching](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7c3875b86bd2b0639ab1e858c678af40-Abstract-Conference.html) | MMOT / SB | 多时间边缘、动量状态与生成建模的重要交叉 |
| [Pairwise Optimal Transport for Training All-to-All Flow Condition Transfer](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a821bd31e93435b50c0a461337fe75c0-Abstract-Conference.html) | flow matching | 研究不同条件间 all-to-all transport，而非只从单一 base 出发 |
| [Hessian-Guided Perturbed Wasserstein Gradient Flows](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3dca8a6a5422c2d5d22c6e9a26469d7e-Abstract-Conference.html) | Wasserstein gradient flow | 二阶几何信息与测度空间动力学 |
| ⭐ [Riemannian Proximal Sampler for High-dimensional and Non-convex Sampling](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8e185f16e458ef5e666901260079cd42-Abstract-Conference.html) | 黎曼几何 / sampling | 几何感知 proximal sampling；与 Riemannian OT 不完全相同但高度相关 |
| [Transfer Learning of Graph Neural Networks with Gromov-Wasserstein Alignment](https://proceedings.neurips.cc/paper_files/paper/2025/hash/30dee0ddc6c0b4907a9d587d3ce87979-Abstract-Conference.html) | GW / graph | graphon/图结构迁移中的 GW 对齐 |
| [Harmonizing Optical Coherence Tomography Across Devices with Latent-Metric Schrödinger Bridges](https://proceedings.neurips.cc/paper_files/paper/2025/hash/08b60b4af0b8163b18553b15f5ce25d2-Abstract-Conference.html) | SB / medical | latent metric 与 SB 的真实跨设备数据应用 |

> NeurIPS 2026：截止检索日没有正式论文集，故不把预印本标为 NeurIPS 2026。

### 3.2 ICML

#### ICML 2024 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Light and Optimal Schrödinger Bridge Matching](https://proceedings.mlr.press/v235/gushchin24a.html) | SB | simulation-free/轻量 SB matching 的关键工作 |
| [Variational Schrödinger Diffusion Models](https://proceedings.mlr.press/v235/deng24c.html) | SB / diffusion | 变分 SB 与 diffusion generative modeling |
| ⭐ [FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html) | 黎曼 FM | 晶体构型空间上的几何约束生成 |
| [Contextuality and Optimal Transport in Quantum Theory](https://proceedings.mlr.press/v235/mariella24a.html) | generalized OT | 展示 OT 在量子 contextuality 中的理论用途 |
| [Generalized Sobolev Transport for Probability Measures on a Graph](https://proceedings.mlr.press/v235/le24a.html) | graph transport | 图上 Sobolev transport 与概率测度比较 |
| [Geometry-Aware Instrumental Variable Regression via Sinkhorn Method of Moments](https://proceedings.mlr.press/v235/kremer24a.html) | causal / Sinkhorn | OT 几何进入 moment matching 与工具变量估计 |

#### ICML 2025 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Hierarchical Refinement: Optimal Transport to Infinity and Beyond](https://openreview.net/forum?id=EBNgREMoVD) | OT geometry | ICML 2025 Oral；研究高阶/极限层次的 transport refinement |
| ⭐ [Wasserstein Flow Matching: Generative Modeling over Families of Distributions](https://proceedings.mlr.press/v267/haviv25a.html) | Wasserstein FM | 从点分布生成扩展到“分布的分布” |
| [Private Estimation of Smooth Transport Maps](https://proceedings.mlr.press/v267/lalanne25a.html) | statistical OT | differential privacy 下 transport map 估计 |
| ⭐ [Flowing Datasets with Wasserstein over Wasserstein Gradient Flows](https://proceedings.mlr.press/v267/bonet25a.html) | higher-order Wasserstein | dataset/family-of-measures 层面的梯度流 |
| [Scalable Approximation of the \(p\)-Wasserstein Distance](https://proceedings.mlr.press/v267/lahn25a.html) | scalable OT | 近似保证与可扩展距离计算 |
| ⭐ [Finding the Center of a Wasserstein Ball](https://proceedings.mlr.press/v267/wang25be.html) | barycenter / robust | Wasserstein ball center 与 robust aggregation |
| [The Procrustes-Wasserstein Barycenter Problem](https://proceedings.mlr.press/v267/adamo25a.html) | barycenter / alignment | 同时处理刚体/正交对齐与 barycenter |
| [Tree-Sliced Wasserstein Distance: A Nonlinear Slicing Approach](https://proceedings.mlr.press/v267/tran25c.html) | sliced OT | 用树结构替代单纯线性投影 |
| [Geometric Tree-Sliced Wasserstein Distance](https://proceedings.mlr.press/v267/tran25b.html) | sliced OT | 结构化切片与几何近似 |
| [Wasserstein Policy Optimization](https://proceedings.mlr.press/v267/pfau25a.html) | RL | 用 Wasserstein 几何定义/约束策略更新 |

#### ICML 2026 — [A]

本节接收状态另由 [ICML 2026 官方下载/活动索引](https://icml.cc/Downloads/2026) 交叉核验；在 PMLR 卷稳定发布后，应把链接替换为最终论文页。

| 论文 | 接收类型/主线 | 为什么值得读 |
|---|---|---|
| ⭐ [FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU](https://arxiv.org/abs/2602.03067)；[代码](https://github.com/ot-triton-lab/flash-sinkhorn) | Oral；GPU Sinkhorn | tile/online softmax 风格的 I/O-aware kernel；必须在同精度、同误差下 benchmark |
| ⭐ [Optimal Transport with Symmetry Groups](https://openreview.net/forum?id=C4JJrPSwpy) | Regular；对称性 | quotient/group symmetry 如何改变 OT 目标和计算 |
| [Minibatch Optimal Transport and Perplexity in Discrete Flow Matching](https://openreview.net/forum?id=A8rmJlSET9) | Regular；discrete FM | minibatch coupling 对离散路径与 perplexity 的影响 |
| [AvAtar: Active Optimal Transport](https://openreview.net/forum?id=X0wQLbleXa) | Regular；active OT | 将采样/查询选择与 transport 联合考虑 |
| [LAST: Language-Action Skill Transfer via Gromov-Wasserstein Alignment](https://openreview.net/forum?id=gIkOQkb4fU) | Regular；GW / robotics | 视觉语言动作空间的跨域结构对齐 |
| [Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing](https://openreview.net/forum?id=LrNH0O3s45) | Spotlight；RL | OT smoothing 与 Bellman/planning 的二阶平滑 |
| [Rethinking Flow-based Gradual Domain Adaptation via Semi-dual Optimal Transport](https://openreview.net/forum?id=iqXzDUd36x) | Regular；domain adaptation | 用 semi-dual OT 重审逐步域迁移 |
| [Video-Based Optimal Transport for Offline Preference Reinforcement Learning](https://openreview.net/forum?id=G8LVO5easu) | Spotlight；RL | 视频证据、偏好与 occupancy transport |
| [Learning One-Dimensional Noise for Generative Flows](https://openreview.net/forum?id=vLQO6nrpYq) | Regular；flow | 学习 base/noise distribution 与 transport flow 的关系 |
| [Partial Fusion of Neural Networks via Partial Optimal Transport](https://openreview.net/forum?id=lvRLG6C0zZ) | Regular；model fusion | 用 partial OT 处理神经网络参数/神经元的不完全对应 |
| ⭐ [Gromov-Wasserstein at Scale, Beyond Squared Norms](https://arxiv.org/abs/2602.06658) | GW / scalable | lifted feature alignment、线性内存与更广 distortion penalty |
| ⭐ [Multimarginal Flow Matching with Optimal Transport Potentials](https://arxiv.org/abs/2606.05327) | MMOT / flow matching | 用 dynamic-OT potential 软约束中间边缘，保持 simulation-free 训练 |
| ⭐ [Multi-Marginal Temporal Schrödinger Bridge Matching from Unpaired Data](https://arxiv.org/abs/2510.01894) | MMOT / SB | 多时间静态快照、factorized fitting 与高维视频/单细胞动力学 |
| [Sinkhorn Normalization of Diffusion Kernels](https://icml.cc/Downloads/2026) | Sinkhorn / geometry | 对 diffusion kernel 做双随机归一化；关注连续极限和几何性质 |
| [Sinkhorn Treatment Effects: A Causal Optimal Transport Measure](https://arxiv.org/abs/2605.08485) | causal / statistical OT | 比均值处理效应更完整地比较反事实分布，并发展有效推断 |
| [ITSPACE: Monotone Gaussian Optimal Transport Updates](https://arxiv.org/abs/2606.30523) | Bures-Wasserstein / SPD | exact BW objective 的结构保持、单调 proximal update |

### 3.3 ICLR

#### ICLR 2024 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Accelerating Sinkhorn Algorithm with Sparse Newton Iterations](https://proceedings.iclr.cc/paper_files/paper/2024/hash/3a819a53408e20b75d1954bf617ccc0a-Abstract-Conference.html) | Sinkhorn / second order | 一阶缩放后的稀疏 Newton 加速；与 FlashSinkhorn 的硬件加速互补 |
| [Energy-guided Entropic Neural Optimal Transport](https://proceedings.iclr.cc/paper_files/paper/2024/hash/517eb19e99947f60afff0cf93e451825-Abstract-Conference.html) | neural OT | energy guidance 与 entropic neural transport |
| [Neural Optimal Transport with General Cost Functionals](https://proceedings.iclr.cc/paper_files/paper/2024/hash/5c882988ce5fac487974ee4f415b96a9-Abstract-Conference.html) | neural OT | 超越简单点对点 cost 的泛函目标 |
| ⭐ [Flow Matching on General Geometries](https://proceedings.iclr.cc/paper_files/paper/2024/hash/d1f9936d3be6997ffffab692977eebe6-Abstract-Conference.html) | Riemannian FM | 流形/一般几何生成的基础前沿论文 |
| [P2OT: Progressive Partial Optimal Transport for Deep Imbalanced Clustering](https://proceedings.iclr.cc/paper_files/paper/2024/hash/3d03791377a31cb3e7357014ba58eb80-Abstract-Conference.html) | partial OT | 类别不平衡、部分匹配和 progressive schedule |
| [Sparsistency for Inverse Optimal Transport](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4761fab863f0900d90cf601fce6d5155-Abstract-Conference.html) | inverse OT | 从观测耦合反推 cost 的稀疏一致性 |
| [Improving Dynamic NeRFs with Optimal Transport](https://proceedings.iclr.cc/paper_files/paper/2024/hash/568b6cc71889ea0b2aa74152ef9c28db-Abstract-Conference.html) | vision / dynamic OT | OT 约束时变 3D 表示 |

#### ICLR 2025 — [A]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Optimal Flow Transport](https://openreview.net/forum?id=NtSlKEJ2DS) | flow / OT | 在 transport optimality 与 flow parameterization 间建立联系 |
| [Cross-Domain Offline Policy Adaptation with Optimal Transport](https://openreview.net/forum?id=LRrbD8EZJl) | RL | 用 OT 对齐不同动力学/观测域的离线策略 |
| [Spherical Tree-Sliced Wasserstein Distance](https://openreview.net/forum?id=FPQzXME9NK) | sliced / manifold | 球面几何与 tree-sliced 构造 |
| [Distance-Based Tree-Sliced Wasserstein Distance](https://openreview.net/forum?id=OiQttMHwce) | sliced OT | 基于距离结构构造树切片 |
| ⭐ [Stochastic Variance-Reduced Variational Inference on the Bures-Wasserstein Manifold](https://openreview.net/forum?id=iMJpmcYucq) | Bures / Riemannian | SPD/Gaussian 分布的 Bures-Wasserstein 几何优化 |
| [PEARL: Learning Recurrent Dynamics with Contrastive Optimal Transport](https://openreview.net/forum?id=txoJvjfI9w) | representation | OT 进入 recurrent dynamics 表征学习 |

#### ICLR 2026 — [A]

| 论文 | 接收类型/主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Sobolev Gradient Ascent for Optimal Transport](https://openreview.net/forum?id=IjL1xEoxXi) | barycenter / exact OT | SGA 路线避免固定熵正则，是 exact barycenter 前沿核心 |
| ⭐ [HALO: Scaling Optimal Transport for High-Dimensional Large-Scale Data](https://openreview.net/forum?id=CkOBcyntGd) | scalable OT | 高维大规模 OT 的算法与系统问题 |
| [Neural Hamilton–Jacobi Characteristic Flows](https://openreview.net/forum?id=YbQxus1KEa) | HJ / neural OT | Hamilton–Jacobi 特征线与可学习 transport flow |
| [Optimal Transport for Single-Molecule Localization Microscopy](https://openreview.net/forum?id=V1i58pZmp3) | scientific ML | OT 在点过程/显微定位中的严肃科学应用 |
| [Hyperparameter Trajectory Modeling via Conditional Lagrangian Optimal Transport](https://openreview.net/forum?id=P5B97gZwRb) | Oral；conditional OT | 把训练超参数轨迹看成条件 Lagrangian transport |
| [A Scalable Constant-Factor Approximation for \(W_p\)](https://openreview.net/forum?id=RPQKJxrEPs&noteId=dkFpewJ3Kh) | approximation | 带理论保证的 scalable Wasserstein approximation |
| [Spectral-Grassmann Wasserstein Distance](https://openreview.net/forum?id=B02EqvyiF3) | manifold / subspace | 频谱、Grassmann 几何与 Wasserstein 的组合 |
| [Efficient Regression with Normalizing Flows and Optimal Transport](https://openreview.net/forum?id=ctdnzPxDI3) | regression / flow | conditional density/regression 中 flow 与 OT 的效率问题 |

### 3.4 CVPR

CVPR 中大量工作把 OT 当作模块或 loss。阅读时应区分：论文是在推进 OT 本身，还是用已有 Sinkhorn/GW 解决视觉任务。

#### CVPR 2024 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Integrating Efficient Optimal Transport and Functional Maps for Unsupervised Shape Correspondence Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Le_Integrating_Efficient_Optimal_Transport_and_Functional_Maps_For_Unsupervised_Shape_CVPR_2024_paper.html) | sliced OT / shape | 将 sliced Wasserstein 与 functional map 结合，计算与几何任务结合紧密 |
| [SALAD: Part-Level Latent Optimal Transport for Visual Place Recognition](https://openaccess.thecvf.com/content/CVPR2024/html/Izquierdo_Optimal_Transport_Aggregation_for_Visual_Place_Recognition_CVPR_2024_paper.html) | aggregation | OT 作为局部视觉特征的可学习聚合器 |
| [Global and Local Prompts Cooperation via Optimal Transport for Federated Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Global_and_Local_Prompts_Cooperation_via_Optimal_Transport_for_Federated_CVPR_2024_paper.html) | federated / prompt | 用 transport plan 协调全局与本地 prompt |

#### CVPR 2025 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Optimal Transport-Guided Source-Free Adaptation for Face Anti-Spoofing](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Optimal_Transport-Guided_Source-Free_Adaptation_for_Face_Anti-Spoofing_CVPR_2025_paper.html) | domain adaptation | source-free 约束下的 prototype/feature transport |
| [OPTICAL: Leveraging Optimal Transport for Contribution Allocation in Dataset Distillation](https://openaccess.thecvf.com/content/CVPR2025/html/Cui_OPTICAL_Leveraging_Optimal_Transport_for_Contribution_Allocation_in_Dataset_Distillation_CVPR_2025_paper.html) | dataset distillation | 用 transport plan 分配真实样本对合成样本的贡献 |
| [Recover and Match: Open-Vocabulary Multi-Label Recognition through Knowledge-Constrained Optimal Transport](https://openaccess.thecvf.com/content/CVPR2025/html/Tan_Recover_and_Match_Open-Vocabulary_Multi-Label_Recognition_through_Knowledge-Constrained_Optimal_Transport_CVPR_2025_paper.html) | open vocabulary | 在类别语义约束下做视觉—标签匹配 |
| [Boosting Point-Supervised Temporal Action Localization through Query Reformation and Optimal Transport](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Boosting_Point-Supervised_Temporal_Action_Localization_through_Integrating_Query_Reformation_and_CVPR_2025_paper.html) | temporal action | 点监督时序动作定位中的 OT 分配 |
| [POT: Prototypical Optimal Transport for Weakly Supervised Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_POT_Prototypical_Optimal_Transport_for_Weakly_Supervised_Semantic_Segmentation_CVPR_2025_paper.html) | segmentation | prototype 与像素/区域之间的 transport |

#### CVPR 2026 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Shape-of-You: Fused Gromov-Wasserstein Optimal Transport for Semantic Correspondence in-the-Wild](https://openaccess.thecvf.com/content/CVPR2026/html/Im_Shape-of-You_Fused_Gromov-Wasserstein_Optimal_Transport_for_Semantic_Correspondence_in-the-Wild_CVPR_2026_paper.html) | FGW / correspondence | 用 3D 结构先验和 anchor linearization 缓解 FGW 计算成本 |
| [Vision-Language Model Guided Source-Free Domain Adaptation via Optimal Transport](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Vision-Language_Model_Guided_Source-Free_Domain_Adaptation_via_Optimal_Transport_CVPR_2026_paper.html) | VLM / DA | VLM semantic prior 引导 source prototype 与 target feature 对齐 |
| [Bypassing the Transport Plan: Dynamic Reweighting for Out-of-Distribution Detection with Semi-Unbalanced Optimal Transport](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_Bypassing_the_Transport_Plan_Dynamic_Reweighting_for_Out-of-Distribution_Detection_with_CVPR_2026_paper.html) | semi-UOT / OOD | 不显式保存完整 plan 的动态重权方法 |
| [VDOT: Efficient Unified Video Creation via Optimal Transport Distillation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_VDOT_Efficient_Unified_Video_Creation_via_Optimal_Transport_Distillation_CVPR_2026_paper.html) | video distillation | 用 OT distill 视频生成过程 |
| [Towards Uncertainty-aware Unsupervised Domain Adaptation for Videos and Time-Series with Causal Optimal Transport](https://openaccess.thecvf.com/content/CVPR2026/html/Mishra_Towards_Uncertainty-aware_Unsupervised_Domain_Adaptation_for_Videos_and_Time-Series_with_CVPR_2026_paper.html) | causal OT | 保持时间因果结构的对齐；与普通静态 OT 有本质区别 |
| [An Optimal Transport-driven Approach for Cultivating Latent Space in Online Incremental Learning](https://openaccess.thecvf.com/content/CVPR2026/html/Tran_An_Optimal_Transport-driven_Approach_for_Cultivating_Latent_Space_in_Online_CVPR_2026_paper.html) | online / MMOT | 在线增量学习中的多分布 latent alignment |
| [FLOW: Optimal Transport-Driven Feature Warping for Generalized Remote Physiological Measurement](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLOW_Optimal_Transport-Driven_Feature_Warping_for_Generalized_Remote_Physiological_Measurement_CVPR_2026_paper.html) | feature alignment | 生理信号跨域特征 warping |

### 3.5 ICCV 2025 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [The Curse of Conditions: Analyzing and Improving Optimal Transport for Conditional Flow Matching](https://openaccess.thecvf.com/content/ICCV2025/html/Cheng_The_Curse_of_Conditions_Analyzing_and_Improving_Optimal_Transport_for_ICCV_2025_paper.html) | conditional FM | 解释无条件 minibatch OT 在 conditional FM 中为何可能适得其反，并提出 C2OT |
| [Optimal Transport for Brain-Image Alignment: Unveiling Redundancy and Synergy in Neural Information Processing](https://openaccess.thecvf.com/content/ICCV2025/html/Xiao_Optimal_Transport_for_Brain-Image_Alignment_Unveiling_Redundancy_and_Synergy_in_ICCV_2025_paper.html) | multimodal / neuroscience | voxel embedding 与 image embedding 的全局匹配 |
| [Taming Flow Matching with Unbalanced Optimal Transport into Fast Pansharpening](https://openaccess.thecvf.com/content/ICCV2025/html/Cao_Taming_Flow_Matching_with_Unbalanced_Optimal_Transport_into_Fast_Pansharpening_ICCV_2025_paper.html) | UOT / flow | 由 UOT dual 构造快速 one-step pansharpening |
| [LaCoOT: Layer Collapse through Optimal Transport](https://openaccess.thecvf.com/content/ICCV2025/html/Quetu_LaCoOT_Layer_Collapse_through_Optimal_Transport_ICCV_2025_paper.html) | model compression | 用 OT 对齐并压缩网络层 |
| [UniversalBooth: Model-Agnostic Personalized Text-to-Image Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_UniversalBooth_Model-Agnostic_Personalized_Text-to-Image_Generation_ICCV_2025_paper.html) | personalized generation | OT 参与跨模型个性化表征传递 |

> ICCV 是双年会；2024 和 2026 没有常规 ICCV 论文集，不能视为检索缺失。

### 3.6 ECCV 2024 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Improving Hyperbolic Representations via Gromov-Wasserstein Regularization](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10766_ECCV_2024_paper.php) | GW / hyperbolic | 用 GW 衡量嵌入前后的结构保持，连接非欧几何表示 |
| [Multiscale Sliced Wasserstein Distances as Perceptual Color Difference Measures](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7025_ECCV_2024_paper.php) | sliced OT | training-free、multiscale SWD 用于非对齐图像颜色感知 |
| [Mahalanobis Distance-based Multi-view Optimal Transport for Multi-view Crowd Localization](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00471.pdf) | UOT / vision | 以相机视线和距离定义任务感知 transport cost |
| [Click Prompt Learning with Optimal Transport for Interactive Segmentation](https://eccv2024.ecva.net/virtual/2024/papers.html) | prompt / segmentation | OT 组织点击提示与语义区域；链接指向 ECCV 官方论文索引 |

> ECCV 2026：截止检索日无正式论文集；后续更新时应从 ECVA official papers 页面核验。2026-08-14 复检：[ECVA papers 页面](https://www.ecva.net/papers.php)仍只收录到 ECCV 2024；按[官方政策](https://eccv.ecva.net/Conferences/2026/SubmissionPolicies)论文集由 Springer/ECVA 发布、不早于会前四周（会议 2026-09-10 开幕，即 2026-08-13 起随时可能上线），建议 8 月下旬至 9 月初再次核验补录。2026-08-25、2026-09-05 两次复检：ECVA papers 页仍只收录到 ECCV 2024，全页无 2026 条目；会议 2026-09-10 开幕，建议 9 月中旬（会后）再查一次。

### 3.7 AAAI

#### AAAI 2024 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Optimal Transport with Cyclic Symmetry](https://ojs.aaai.org/index.php/AAAI/article/view/29444) | symmetry | 对称性下 OT 的理论与计算，和 ICML 2026 symmetry groups 可连读 |
| ⭐ [Revisiting Partial Optimal Transport: A Fast, Robust and Numerically Stable Algorithm](https://ojs.aaai.org/index.php/AAAI/article/view/28648) | partial OT | partial OT 的 Sinkhorn 型数值稳定算法 |
| [Dynamic Optimal Transport with Skip Orthogonal List](https://ojs.aaai.org/index.php/AAAI/article/view/30073) | dynamic OT | 动态环境中 transport matching 的数据结构/算法 |
| [Multi-view Clustering via Optimal Transport](https://ojs.aaai.org/index.php/AAAI/article/view/29563) | barycenter / clustering | 多视图分布聚合与共识表征 |
| [Learning Ultrametric Trees for Optimal Transport Regression](https://ojs.aaai.org/index.php/AAAI/article/view/30052) | tree OT | 学习 tree metric 以加速/结构化 transport |
| [Hierarchical Multi-Marginal Optimal Transport for Network Alignment](https://ojs.aaai.org/index.php/AAAI/article/download/29605/31022) | MMOT / graph | 多网络联合对齐和层次结构 |
| [General Variational Inference via Optimal Transport](https://ojs.aaai.org/index.php/AAAI/article/view/29035) | VI / OT | OT 目标与通用变分推断 |
| [Treatment Effect Estimation with Optimal Transport](https://ojs.aaai.org/index.php/AAAI/article/view/29564) | causal | covariate distribution alignment 与处理效应 |

#### AAAI 2025 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [Optimal Transport Latent Mixer for Graph Representation Learning](https://ojs.aaai.org/index.php/AAAI/article/view/33849) | FGW barycenter / graph | 用 FGW/barycentric mixing 生成图 latent representation |
| [Conditional Fairness via Optimal Transport](https://ojs.aaai.org/index.php/AAAI/article/view/33847) | fairness | 条件分布层面的公平约束；需审视 cost 与群体定义 |
| [Online Optimal Transport for Continual Generative Modeling](https://ojs.aaai.org/index.php/AAAI/article/view/34362) | online OT / generation | 数据流/持续学习中的 transport update |
| [Optimal Transport for Model Fusion and Backdoor Mitigation](https://ojs.aaai.org/index.php/AAAI/article/view/34828) | model fusion | 参数/神经元匹配与安全应用 |

#### AAAI 2026 — [P]

| 论文 | 主线 | 为什么值得读 |
|---|---|---|
| ⭐ [CellStream: Multi-Marginal Optimal Transport for Cellular Trajectory Inference](https://ojs.aaai.org/index.php/AAAI/article/download/37041/41003) | MMOT / biology | 多时间点单细胞分布与轨迹推断 |
| [Wasserstein-Aware Transfer for Diffusion Models](https://ojs.aaai.org/index.php/AAAI/article/view/39365) | diffusion / transfer | 以 Wasserstein 几何控制生成模型迁移 |
| [Geometric Image Representation via Optimal Transport](https://ojs.aaai.org/index.php/AAAI/article/download/39119/43081) | vision / geometry | 将图像表示构造成 transport geometry |
| [Wasserstein-Aligned Hyperbolic Multi-View Clustering](https://ojs.aaai.org/index.php/AAAI/article/view/39851) | hyperbolic / clustering | 双曲几何与分布对齐结合 |
| [IdeFN: Relaxed Partial Optimal Transport for Incomplete Data](https://ojs.aaai.org/index.php/AAAI/article/download/38690/42652) | partial OT | 缺失/不完整观测下 relaxed partial matching |
| [Inverse Optimal Transport for Vision-Language Model Adaptation](https://ojs.aaai.org/index.php/AAAI/issue/view/712) | inverse OT / VLM | 从适配行为学习 transport cost；链接为 AAAI 2026 官方卷索引 |

## 4. 2025–2026 前沿预印本：不要与会议论文混写

以下项目很新、与用户指定方向直接相关，但截至检索日应保留 **[R] Preprint** 标签。后来若正式接收，需同时保存会议官方证据并更新状态。

| 预印本 | 方向 | 现在为什么值得跟 |
|---|---|---|
| ⭐ [Riemannian Neural Optimal Transport](https://arxiv.org/abs/2602.03566) | Riemannian OT | 学习流形上的 Kantorovich potentials/maps；本地已有精读报告 |
| ⭐ [Entropic Riemannian Neural Optimal Transport](https://arxiv.org/abs/2605.04255) | entropic Riemannian OT | intrinsic entropic objective 与 neural solver |
| [Riemannian Barycentric Projections](https://arxiv.org/abs/2606.07926) | manifold barycenter | barycentric projection 从欧氏扩展到黎曼几何 |
| [Sub-Riemannian Schrödinger Bridges and Optimal Transport](https://arxiv.org/abs/2605.11429) | sub-Riemannian / SB | 非完整约束几何上的路径空间 transport |
| ⭐ [A Unified Approach for Computing Wasserstein Barycenters](https://arxiv.org/abs/2605.11270) | exact barycenter | FRBary；统一离散/连续计算视角，本地已有精读报告 |
| [The Signed Wasserstein Barycenter Problem](https://arxiv.org/abs/2602.05976) | signed barycenter | barycenter 权重允许符号后的定义、存在性与算法 |
| [Adapted Wasserstein Barycenters of Gaussian Processes](https://arxiv.org/abs/2604.22453) | causal/adapted barycenter | 高斯过程的非前视耦合和 barycenter |
| ⭐ [A Dynamical Formulation of Multi-Marginal Optimal Transport](https://arxiv.org/abs/2509.22494) | dynamic MMOT | 从静态高维 coupling 转向连续动力学 formulation |
| [FastSinkhorn](https://arxiv.org/abs/2605.00837) | high-performance Sinkhorn | 与 FlashSinkhorn 对比算法、kernel 和 benchmark 定义 |
| [cuRegOT](https://arxiv.org/abs/2605.08793) | GPU regularized OT | CUDA/GPU regularized OT 工程路线 |
| ⭐ [Foundations of Schrödinger Bridges for Generative Modeling](https://arxiv.org/abs/2603.18992) | SB foundations | 统一生成建模中 bridge、score、flow 的基础概念 |

前沿论文的阅读检查：

1. 目标是 exact OT、entropic OT、Sinkhorn divergence，还是只借用了 transport plan？
2. manifold 方法使用 intrinsic geodesic cost，还是在 embedding/tangent space 做 Euclidean OT？
3. barycenter 是 fixed-support、free-support、continuous 还是 parametric？
4. speedup 在何种 \(n,d,\varepsilon\)、dtype、误差标准和硬件上成立？
5. 理论比较的是 objective gap、marginal violation、map error 还是下游指标？
6. GitHub 是否包含训练代码、数据预处理、环境锁定和可复现实验脚本？

## 5. 优质课程、教程与博客

### 5.1 系统课程

| 资源 | 形式 | 建议用法 |
|---|---|---|
| ⭐ [Gabriel Peyré — Optimal Transport for Machine Learners](https://www.gpeyre.com/ot4ml/) | 在线书、slides、notebooks | 与 `OT_book` 同步；每章跑 notebook，建立公式—代码映射 |
| [Gabriel Peyré — Teaching](https://www.gpeyre.com/teaching/) | MVA 等课程材料入口 | 找 OT、inverse problems、mathematical data science 的完整课件 |
| ⭐ [Computational Optimal Transport for Machine Learning](https://mathurinm.github.io/otml/) | 2025 课程 | 偏现代 ML 与实践；适合完成基础教材后系统复习 |
| [Göttingen — Computational Optimal Transport](https://ot.cs.uni-goettingen.de/teaching_cot.html) | 课程/讲义 | 计算几何、离散与半离散视角的补充 |
| [MIT OCW 6.262 — Discrete Stochastic Processes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/) | 视频、教材、习题、解答 | SB 前置；先学 Markov/Poisson/renewal/martingale |
| [Optimal Transport for Unsupervised Learning Tutorial](https://optimaltransporttutorial.github.io/) | tutorial website | 快速理解 OT 在聚类、domain adaptation、representation 中的用法 |

### 5.2 视频与短教程

| 资源 | 强项 | 注意 |
|---|---|---|
| [Lénaïc Chizat — A Primer/Tutorial on Optimal Transport](https://www.broadinstitute.org/talks/primer-tutorial-optimal-transport) | 从概念到生物信息应用，讲解清晰 | 看完应回到教材补证明 |
| [Marco Cuturi — Optimal Transport Mini-Tutorial](https://www.youtube.com/watch?v=W29-YKYQLBY) | 计算 OT 与 Sinkhorn 的作者视角 | 视频公式建议配 `OT_book` Ch.4 |
| [Flow Matching on General Geometries](https://proceedings.iclr.cc/paper_files/paper/2024/hash/d1f9936d3be6997ffffab692977eebe6-Abstract-Conference.html)；[代码](https://github.com/facebookresearch/riemannian-fm) | 黎曼 FM 的论文—代码配对 | 先会 exp/log map、ODE 和 conditional FM |

### 5.3 直觉型网页与博客

| 资源 | 用途 | 证据权重 |
|---|---|---|
| ⭐ [OT4ML Interactive Book](https://www.gpeyre.com/ot4ml/myst/_build/html/index.html) | 交互图、公式和 notebook；最适合查概念 | 高：作者教材 |
| [Transport: An Interactive Introduction](https://pablowilliams.github.io/Transport/) | 1D/2D transport 的视觉直觉 | 中：教学辅助 |
| [Kai Zhao — Optimal Transport and Sinkhorn](https://kaizhao.net/blog/ot) | 快速理解离散 OT 与 Sinkhorn | 中：博客 |
| [Runnable Sinkhorn Notes](https://khey17.github.io/sinkhorn-algorithm/) | 结合实现理解数值过程 | 中：需以正式文献核验 |
| [An Introduction to Optimal Transport](https://abdgafartunde.github.io/blog/2026/06/22/optimal-transport/) | 初学者概览 | 低至中：只作导读 |

博客最适合回答“为什么”，教材负责“是什么”，论文和代码负责“是否真的有效”。不要用博客替代定义、定理或会议状态的来源。

## 6. 软件与复现实验栈

| 工具 | 适合什么 | 主要限制/提醒 |
|---|---|---|
| ⭐ [POT — Python Optimal Transport](https://pythonot.github.io/) | exact、entropic、UOT、partial、GW、barycenter、MMOT；最全基线库 | 高性能大矩阵未必是最佳；记录 backend 与版本 |
| ⭐ [OTT-JAX](https://ott-jax.readthedocs.io/) | JAX 可微 OT、Sinkhorn、low-rank、几何对象 | JIT/设备布局影响 benchmark；第一次编译应单独计时 |
| [GeomLoss](https://www.kernel-operations.io/geomloss/) | PyTorch 中大规模 differentiable Sinkhorn loss | 偏 point cloud/loss；不覆盖所有 OT 变种 |
| [KeOps](https://www.kernel-operations.io/keops/) | 不显式物化大 cost/kernel matrix | 是通用 kernel 引擎，不等同完整 OT solver |
| [Geomstats](https://geomstats.github.io/) | sphere、SPD、Grassmann 等流形运算 | 负责几何 primitives；OT objective 需另实现/集成 |
| ⭐ [FlashSinkhorn](https://github.com/ot-triton-lab/flash-sinkhorn) | Triton GPU entropic OT benchmark | 核对支持的 cost、shape、dtype、backward 和误差定义 |
| [TorchCFM](https://github.com/atong01/conditional-flow-matching) | conditional/OT flow matching 实验 | minibatch OT coupling 不是总体精确 OT |
| [Riemannian Flow Matching](https://github.com/facebookresearch/riemannian-fm) | 流形生成模型 | 重点检查 chart、exp/log、数值 ODE 与 cut locus |
| [DMMOT](https://github.com/yairshenfeld/DMMOT) | dynamic MMOT 预印本实现 | 研究代码；复现前锁定 commit 和依赖 |

### 6.1 建议的统一 benchmark 记录

```text
problem:
  variant: exact | entropic | debiased | UOT | partial | GW | barycenter
  n_source / n_target / dimension:
  cost:
  epsilon / rho / transported_mass:

numerics:
  dtype:
  stopping_rule:
  marginal_violation:
  objective_gap_or_reference:
  iterations:

system:
  hardware:
  library_and_version:
  compile_time_included:
  peak_memory:
  wall_time_median_and_trials:
```

FlashSinkhorn、POT、OTT、GeomLoss 只有在目标、误差、dtype 和计时边界一致时才可直接比较。

## 7. 五条可执行阅读路线

### 路线 A：FlashSinkhorn 与大规模 Sinkhorn（4–6 周）

1. `OT_book` Ch.3–4：dual、KL projection、Sinkhorn；
2. Cuturi 2013 → Feydy 2019 → Genevay 2019；
3. ICLR 2024 Sparse Newton、NeurIPS 2024 ProgOT；
4. ICML 2026 FlashSinkhorn；
5. 再横向比较 FastSinkhorn、cuRegOT、HALO；
6. 输出：同一 cost/dtype/tolerance 下的 speed–memory–error Pareto curve。

研究切口：非欧 cost、unbalanced/partial kernel、backward pass、超小 \(\varepsilon\)、多 GPU、动态 shape。

### 路线 B：黎曼流形 OT（6–8 周）

1. 补 manifold、geodesic、exp/log、volume form、cut locus；
2. Figalli/Santambrogio 中 Brenier 与 Wasserstein geometry；
3. ICLR 2024 Flow Matching on General Geometries；
4. ICML 2024 FlowMM、ICLR 2025 Bures-Wasserstein VI；
5. RNOT → Entropic RNOT → Riemannian barycentric projections；
6. 输出：sphere/SPD 上 intrinsic、tangent 和 ambient 三种 baseline。

研究切口：曲率相关误差、cut-locus 稳定性、quotient symmetry、manifold UOT/barycenter、intrinsic GPU kernel。

### 路线 C：Wasserstein barycenter（6–8 周）

1. `OT_book` Ch.9.2 与 Agueh–Carlier；
2. `Multi_OT_book` 中 barycenter 作为 MMOT；
3. entropic barycenter → debiased Sinkhorn barycenter；
4. ICML 2025 Wasserstein ball center、Procrustes-Wasserstein；
5. ICLR 2026 SGA → FRBary → signed/adapted/manifold barycenter；
6. 输出：exact/entropic/debiased、fixed/free support 的对照表与实验。

研究切口：不确定性、鲁棒/trimmed barycenter、流形 barycenter、streaming、统计置信区间。

### 路线 D：MMOT 与 Schrödinger bridge（8–10 周）

1. Gallager Markov/renewal/martingale；
2. `Multi_OT_book` Ch.1–3、6–7；
3. Léonard SB survey；
4. ICML 2024 Light SB Matching；
5. NeurIPS 2025 3MSBM、AAAI 2026 CellStream；
6. dynamic MMOT、sub-Riemannian SB、Foundations of SB；
7. 输出：static coupling、dynamic action、path-space KL 三种 formulation 的对应关系。

研究切口：多时间观测、参考动力学错设、momentum state、causal/adapted constraint、simulation-free matching。

### 路线 E：GW 与跨空间对齐（5–7 周）

1. `OT_book` GW 章节；
2. Peyré–Cuturi–Solomon 2016；
3. NeurIPS 2024 SDP relaxation；
4. ECCV 2024 hyperbolic GW、CVPR 2026 Shape-of-You；
5. ICML 2026 symmetry groups / LAST；
6. 输出：GW、FGW、linearized/anchor approximation 的精度—复杂度表。

研究切口：可认证 lower bound、partial/unbalanced GW、对称性、可扩展 FGW barycenter。

## 8. 建议的本地文献管理字段

每篇论文至少保留：

```yaml
title:
authors:
year:
venue:
status: proceedings | accepted | preprint
official_url:
arxiv_url:
code_url:
task:
ot_variant:
exact_or_regularized:
geometry:
main_claim:
evidence:
limitations:
reproduction_status:
last_verified:
```

### 8.1 每月更新程序

1. 只从会议官方 proceedings/OpenReview 按 title 搜索；
2. 用 Crossref/OpenAlex 补 DOI 和引用信息，但不用它替代接收证据；
3. 检查 arXiv version history、代码仓库 release/commit；
4. 新增论文先归入 [R]，获得官方接收证据后再改 [A]/[P]；
5. benchmark 数字必须回到论文表格和代码配置核验；
6. 对 NeurIPS/ECCV 2026 在正式结果发布后单独补检，不提前占位。

## 9. 先读哪 15 篇

若目标是尽快形成前沿判断力，建议按此顺序：

1. Cuturi 2013 — Sinkhorn；
2. Feydy et al. 2019 — Sinkhorn divergence；
3. Agueh & Carlier 2011 — barycenter；
4. Léonard 2014 — SB；
5. Flow Matching on General Geometries — ICLR 2024；
6. Accelerating Sinkhorn with Sparse Newton — ICLR 2024；
7. Semidefinite Relaxations of GW — NeurIPS 2024；
8. Light and Optimal SB Matching — ICML 2024；
9. FlowMM — ICML 2024；
10. Momentum Multi-Marginal SB Matching — NeurIPS 2025；
11. Wasserstein Flow Matching — ICML 2025；
12. Sobolev Gradient Ascent for OT — ICLR 2026；
13. FlashSinkhorn — ICML 2026 Oral；
14. Riemannian Neural OT — 2026 preprint；
15. Unified Wasserstein Barycenters — 2026 preprint。

这 15 篇覆盖计算、几何、barycenter、MMOT、SB 和生成模型；读完后再按具体研究问题扩展，效率远高于按关键词顺序浏览全部应用论文。
