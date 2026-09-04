# Optimal Transport 六类变种详解与近期论文调研报告

## 0. 本报告范围

本目录围绕六类 Optimal Transport（OT）变种整理：

- **Multi-marginal OT**：多于两个边缘分布之间的联合耦合问题。
- **Wasserstein barycenter**：在 Wasserstein 几何下定义多个分布的“平均”。
- **Partial OT**：只运输部分质量，允许 unmatched / outlier。
- **Gromov-Wasserstein**：比较没有共享坐标系、只给内部结构的对象。
- **Schrödinger Bridge**：在参考随机过程附近寻找满足边缘约束的最小相对熵路径测度。
- **Causal / adapted OT**：在随机过程/时间序列中加入信息流、过滤和非前视约束。

已下载并阅读的代表性近期论文见 `PAPERS_MANIFEST.json`。每篇论文的 PDF、抽取文本和中文阅读报告位于对应子目录。

## 1. 从经典 OT 到变种：核心问题如何改变

经典 Kantorovich OT 的形式是：给定两个分布 `μ`、`ν` 和代价 `c(x,y)`，在所有边缘为 `μ,ν` 的耦合 `π` 中最小化期望代价。它回答的是“如何把一个分布的质量搬到另一个分布”。多数 OT 变种都可以理解为修改以下四个要素之一：

- **边缘数量**：从两个分布扩展到多个分布，得到 multi-marginal OT。
- **质量约束**：从必须全部匹配，放松到只匹配部分质量，得到 partial/unbalanced OT。
- **对象类型**：从共享坐标空间的点分布，扩展到图、度量空间、网络等结构对象，得到 GW。
- **动态/信息约束**：从静态耦合扩展到路径测度、随机过程或非前视耦合，得到 SB 与 causal/adapted OT。
- **统计任务**：从两分布距离扩展到“多个分布的中心”，得到 Wasserstein barycenter。

因此，本报告不把这些变种看成互不相关的名词，而看成 OT 的不同“坐标轴扩展”。

## 2. Multi-marginal OT

### 2.1 问题定义

Multi-marginal OT（MMOT）给定 `K` 个边缘分布 `μ_1,...,μ_K`，寻找联合分布 `π(x_1,...,x_K)`，使每个边缘等于指定分布，并最小化多体代价：

```text
min_{π ∈ Π(μ_1,...,μ_K)} ∫ c(x_1,...,x_K) dπ(x_1,...,x_K)
```

当 `K=2` 时退化为标准 OT。`K>2` 时，耦合不再只是“从源到目标”的一对一运输，而是多个分布之间的联合匹配。

### 2.2 直觉

MMOT 可以理解为“给多个分布同时配对”。例如：

- 多个图像类别/风格之间建立共享对应关系；
- 多个时间点的细胞群体状态联合对齐；
- 多电子密度泛函理论中的多体相关；
- 多任务/多域学习中的公共潜在结构。

相较两边 OT，MMOT 的难点在于耦合维度随边缘数量指数式膨胀。若每个边缘有 `N` 个样本，联合表大小可能达到 `N^K`，直接线性规划很快不可行。

### 2.3 代表论文

本次选读 `Collision-based Dynamics for Multi-Marginal Optimal Transport`（arXiv:2412.16385）。该文把 MMOT 的离散求解看成随机碰撞动力学：不是枚举所有排列或所有 swap，而是随机选择样本对进行二元交换，若交换降低代价则接受。论文强调：对于 `L_p`-Wasserstein 代价，方法保持边缘分布，单轮复杂度随样本数线性增长，整体复杂度估计为 `O(n K^2 N_p)`，适合大量边缘和高维样本。

### 2.4 优点与限制

- **优点**：表达多方联合结构；能刻画多体相关，而不是只做 pairwise 对齐。
- **限制**：理论和计算都比二边 OT 困难；很多算法只能近似；全局最优性不易保证。
- **适用场景**：多分布平均、多域对齐、多体物理、联合数据集结构发现。

## 3. Wasserstein barycenter

### 3.1 问题定义

Wasserstein barycenter 试图在 Wasserstein 空间中定义多个分布的几何平均。给定分布 `μ_i` 和权重 `λ_i`，求：

```text
min_ν Σ_i λ_i W_p^p(ν, μ_i)
```

它不是对密度逐点相加，而是在运输几何下寻找中心分布。

### 3.2 直觉

普通欧氏平均会模糊多峰结构。例如两个高斯分布位置不同，直接平均密度可能产生两个峰或不合理扩散；Wasserstein barycenter 更像“把形状沿空间移动后平均”，能得到更符合几何的中心。

### 3.3 变种：signed barycenter

经典 barycenter 通常要求权重非负且和为 1。最新理论开始研究带负权的 signed barycenter，即目标函数包含正负 Wasserstein 距离项。这类问题可用于：

- 测度值输出的回归/外推；
- Wasserstein gradient flow 的高阶时间离散；
- 在分布空间中做类似线性组合或加速度项。

本次选读 `The Signed Wasserstein Barycenter Problem`（arXiv:2602.05976）。该文指出负权会破坏欧氏凸性和经典广义测地凸性，因此问题显著更难。论文从 primal 和 dual 两条线推进：证明一般代价下的存在性；在单个正权重的特殊情形建立凸插值和唯一性；对任意正负权重提出新的 Kantorovich 势函数 min-max 对偶表述，并给出 saddle point 诱导 signed barycenter、唯一性和 stationary point 升级为全局最优的充分条件。

### 3.4 优点与限制

- **优点**：提供分布集合的几何代表；适合图像、统计、时间序列模型聚合和不确定性量化。
- **限制**：高维计算难；多 barycenter 可能非唯一；带负权时凸性和稳定性更复杂。
- **适用场景**：分布平均、模板生成、模型融合、场景聚类、分布回归。

## 4. Partial OT

### 4.1 问题定义

Partial OT 放松“全部质量必须运输”的约束，允许只匹配一部分质量。典型形式是：只运输质量 `m ≤ min(|μ|,|ν|)`，或对未运输质量施加惩罚。

直观地，它适合处理 outlier、遮挡、不完整对应和部分重叠数据。

### 4.2 与 unbalanced OT 的区别

Partial OT 和 unbalanced OT 都放松质量守恒，但侧重点不同：

- **Partial OT**：常强调选择一部分可信质量进行匹配，其余不匹配。
- **Unbalanced OT**：常允许质量增删，并用 KL/TV 等 divergence 惩罚边缘偏差。

Partial OT 更像“最优子集匹配”；unbalanced OT 更像“带质量创建/消灭代价的运输”。

### 4.3 代表论文

本次选读 `Learning Partial Graph Matching via Optimal Partial Transport`（arXiv:2410.16718）。论文把 partial graph matching 表述为 optimal partial transport，用 weighted total variation 控制未匹配节点的代价，并证明该目标在 unit-weighted 情况下存在 partial assignment 型最优解。关键算法贡献是把 partial graph matching 嵌入 linear sum assignment，通过 Hungarian algorithm 精确求解，最坏复杂度 `O(n^3)`。

实验上，论文在 SPair-71K、IMCPT 和 PPI 网络匹配上展示了较强性能与较低推理时间；但也承认在标注不可靠、语义模糊或高噪声情况下鲁棒性下降。

### 4.4 优点与限制

- **优点**：天然处理 outlier、缺失点和部分可匹配结构；比强制全匹配更现实。
- **限制**：需要选择质量/惩罚参数；过小会漏匹配，过大会引入错误匹配。
- **适用场景**：关键点匹配、图匹配、生物网络对齐、多模态部分对应。

## 5. Gromov-Wasserstein

### 5.1 问题定义

经典 OT 要求两个分布位于同一个度量空间，代价 `c(x,y)` 能直接比较 `x` 和 `y`。但图、网络、形状、度量空间之间往往没有共享坐标系。Gromov-Wasserstein（GW）比较的是内部关系是否相似。

标准 GW 的核心代价是比较两边内部距离：

```text
min_π ∫∫ |d_X(x,x') - d_Y(y,y')|^p dπ(x,y)dπ(x',y')
```

它寻找一个跨对象耦合，使得被匹配点对之间的内部距离结构尽量一致。

### 5.2 直觉

GW 不问“点 x 和点 y 在同一空间中距离多近”，而问“如果 x 对应 y、x' 对应 y'，那么 x 与 x' 的关系是否像 y 与 y' 的关系”。因此它非常适合图、形状、社交网络和度量测度空间比较。

### 5.3 代表论文

本次选读 `The Z-Gromov-Wasserstein Distance`（arXiv:2408.08233）。该文将许多 GW-like 距离统一为 `Z`-valued network 上的 Z-GW 框架。传统网络核通常取实值距离，而 Z-GW 允许网络边/关系落在一般度量空间 `Z` 中。论文证明多个已知距离可以作为 Z-GW 特例，包括标准 GW、ultrametric GW、Fused GW、Fused Network GW、spectral GW 等；在 `Z` 可分时，Z-GW 在适当等价类上构成真正的 metric；并建立 separability、completeness、contractibility、geodesicity 等性质以及可计算下界和近似。

论文也指出一般 Z-GW 的朴素计算需要四维数组，时间和空间可达 `O(n^2 m^2)`；可通过 `R^n`-network 近似、熵正则迭代和 sampled GW 等方向改善。

### 5.4 优点与限制

- **优点**：无需共享坐标系；能比较结构对象；可融合节点属性和边关系。
- **限制**：目标通常非凸；计算重；最优耦合解释可能不唯一。
- **适用场景**：图匹配、形状分析、跨域结构对齐、网络比较、单细胞多组学对齐。

## 6. Schrödinger Bridge

### 6.1 问题定义

Schrödinger Bridge（SB）给定参考随机过程 `Q` 和边缘约束（通常是初末分布 `μ_0, μ_T`），寻找满足边缘约束且与参考过程最接近的路径测度 `P`：

```text
min_P KL(P || Q)
subject to P_0 = μ_0, P_T = μ_T
```

它是路径空间上的相对熵最小化，也是熵正则 OT 的动态版本。

### 6.2 直觉

如果 OT 是“最便宜地搬运质量”，SB 是“在一个默认随机动力学附近，最小幅度地改变路径分布，使起点和终点满足要求”。其中参考过程可理解为先验动力学；KL 约束使桥不要偏离先验太远。

SB 同时连接：

- **OT**：噪声趋零或熵正则视角下接近 OT；
- **随机控制**：最优控制漂移把过程引向目标边缘；
- **扩散模型**：通过正反向 SDE、score、flow matching 等方式学习路径；
- **IPF/Sinkhorn**：交替投影/势函数更新求解边缘约束。

### 6.3 代表论文

本次选读 `Foundations of Schrödinger Bridges for Generative Modeling`（arXiv:2603.18992）。这是一篇基础性长综述/讲义，将 SB 作为生成建模的统一理论框架，系统覆盖静态 SB、动态 SB、path measure、Fokker-Planck、Feynman-Kac、Girsanov、随机最优控制、Doob h-transform、Markovian/reciprocal projection、stochastic interpolants，以及多种变体：Gaussian SB、generalized SB、multi-marginal SB、unbalanced SB、branched SB、fractional SB。它进一步连接 diffusion Schrödinger bridge matching、simulation-free score/flow matching、adjoint matching、离散 CTMC SB，并讨论数据翻译、单细胞动力学和 Boltzmann 分布采样。

### 6.4 优点与限制

- **优点**：动态、随机、可引入先验过程；理论统一 OT、扩散和控制；适合生成模型和科学动力学建模。
- **限制**：数学门槛高；训练依赖 score/势函数/路径采样；不同算法间关系复杂。
- **适用场景**：生成建模、数据翻译、轨迹建模、受控采样、分子/细胞动力学、路径规划。

## 7. Causal / adapted OT

### 7.1 问题定义

Causal OT 或 adapted OT 关注随机过程之间的运输，但要求耦合尊重时间和信息流。普通 Wasserstein 距离比较路径分布时可能使用未来信息；adapted/causal OT 禁止这种“看未来”的耦合。

简言之，它把“每个时间点可用的信息”纳入运输约束：

- 源过程到目标过程的匹配必须非前视；
- 耦合要适应 filtration；
- 比较的是随机过程作为动态对象的距离，而不是把整条路径当静态向量。

### 7.2 直觉

两个时间序列即使静态路径分布相近，也可能有完全不同的信息结构。例如一个过程的早期噪声决定未来，另一个过程的未来信息被提前泄露。普通 Wasserstein 距离可能无法区分；adapted Wasserstein 会惩罚信息结构不一致。

### 7.3 代表论文

本次选读 `Adapted Wasserstein Barycenters of Gaussian Processes`（arXiv:2604.22453）。该文研究高斯过程的 adapted 2-Wasserstein barycenter。主要结果包括：

- 证明高斯过程的 adapted barycenter 存在，且最优 barycenter 仍为高斯；
- 通过 multicausal reformulation 和 backward induction 将问题化为 adapted Bures-Wasserstein barycenter；
- 证明唯一性；
- 给出列分解：adapted Bures-Wasserstein 距离分解为多个 classical Bures-Wasserstein 距离之和；
- 建立 fixed-point characterization，并给出交替最小化算法。

数值实验中，adapted barycenter 在 Cholesky factor 层面保留 AR(1) 参数符号，因此能反映时间因果结构；普通 Bures-Wasserstein barycenter 在 covariance 层面会丢失这类符号信息。

### 7.4 优点与限制

- **优点**：适合时间序列、金融、多阶段决策、随机控制；避免未来信息泄露。
- **限制**：理论和计算更复杂；高斯/离散时间之外的唯一性和结构刻画仍开放。
- **适用场景**：随机过程模型聚合、鲁棒金融、scenario reduction、多阶段优化、时序生成模型评估。

## 8. 横向比较

| 变种 | 主要改变 | 核心对象 | 关键难点 | 本次代表论文 |
|---|---|---|---|---|
| Multi-marginal OT | 两边缘变多边缘 | 多分布联合耦合 | 维度爆炸、计算复杂 | arXiv:2412.16385 |
| Wasserstein barycenter | 距离变平均/中心 | 分布的几何平均 | 非唯一、高维求解、signed 情形非凸 | arXiv:2602.05976 |
| Partial OT | 全量匹配变部分匹配 | 子集/部分质量耦合 | 匹配质量和惩罚参数选择 | arXiv:2410.16718 |
| Gromov-Wasserstein | 共享空间变内部结构比较 | 图/网络/度量空间 | 非凸、四阶代价、结构解释 | arXiv:2408.08233 |
| Schrödinger Bridge | 静态耦合变路径测度 | 随机过程/生成路径 | 训练与路径推断复杂 | arXiv:2603.18992 |
| Causal/adapted OT | 普通耦合变信息约束耦合 | 过滤概率空间/随机过程 | 非前视约束和动态规划 | arXiv:2604.22453 |

## 9. 给后续研究的建议

### 9.1 如果目标是机器人/轨迹/生成策略

最相关的是 **Schrödinger Bridge**、**causal/adapted OT** 和 **partial OT**：

- SB 适合作为路径分布桥、轨迹生成和从先验动力学到目标行为的最小偏移框架。
- Causal/adapted OT 可用于比较策略轨迹时保留信息结构，避免“离线全路径比较”带来的未来泄露。
- Partial OT 可处理演示轨迹、视觉关键点或状态序列中的缺失、遮挡和 outlier。

### 9.2 如果目标是多数据集/多任务融合

最相关的是 **Wasserstein barycenter** 和 **multi-marginal OT**：

- barycenter 用于求多个分布的中心模板或代表模型；
- MMOT 用于多域同时对齐，而不只是 pairwise 对齐。

### 9.3 如果目标是图/结构对齐

最相关的是 **Gromov-Wasserstein** 和 **partial OT**：

- GW 解决无共享坐标的结构比较；
- partial OT 解决结构中只有一部分节点可对应的问题；
- 二者结合可自然导向 partial GW / fused partial GW 等方向。

## 10. 一句话总结

这些 OT 变种本质上是在经典“两个分布之间的质量搬运”问题上分别加入 **多边缘、几何平均、部分匹配、结构不变性、路径熵正则、时间信息约束**。它们共同说明：OT 已经从一个静态距离工具扩展为一套用于分布、结构、动态和生成模型的统一建模语言。
