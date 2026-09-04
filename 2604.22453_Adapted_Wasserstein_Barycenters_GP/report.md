# 中文阅读报告：Adapted Wasserstein Barycenters of Gaussian Processes

## 1. 基本信息

- **论文标题**：Adapted Wasserstein Barycenters of Gaussian Processes
- **arXiv**：2604.22453
- **对应 OT 变种**：Causal OT / adapted Wasserstein / stochastic process barycenter
- **本地文件**：`paper.pdf`、`paper.txt`

## 2. 论文要解决的问题

经典 Wasserstein 距离比较静态概率分布。若把随机过程的一整条路径当成高维向量，普通 Wasserstein 距离会忽略时间和信息结构：它可能允许 coupling 使用未来信息，从而不适合多阶段决策、时间序列和金融等场景。

Adapted Wasserstein / causal transport 的核心是让耦合尊重 filtration，即只能使用当前和过去信息，不能前视未来。本文进一步研究：**如何在 adapted Wasserstein 几何下定义多个高斯过程的 barycenter，并证明其存在性、唯一性和可计算刻画？**

## 3. 核心方法

论文聚焦离散时间 Gaussian processes。每个过程可写成：

```text
X_i = a_i + L_i G
```

其中 `G` 是标准高斯噪声，`L_i` 是 block-lower-triangular Cholesky factor，编码噪声如何随时间传播。lower-triangular 结构正是适应时间信息流的关键。

作者利用 multicausal reformulation 和 backward induction，把 adapted Wasserstein barycenter 问题化为 adapted Bures-Wasserstein barycenter 问题。核心结果是：高斯输入的 adapted barycenter 仍然是高斯，并且问题可以在 Cholesky factor 层面求解。

## 4. 主要贡献

Theorem 2.1 是论文主结果，可概括为四点：

- **存在性与高斯性**：高斯过程的 adapted barycenter 存在，且任一 minimizer 都是高斯。
- **唯一性**：adapted Bures-Wasserstein barycenter 在等价类 `L/O` 上唯一。
- **列分解**：adapted Bures-Wasserstein 距离可分解为 `T` 个 classical Bures-Wasserstein 距离之和，每个对应 Cholesky factor 的一个截断列协方差。
- **固定点刻画**：barycenter 满足一个 Procrustes optimizer 参与的 fixed-point equation，并可据此设计 alternating minimization algorithm。

论文还证明 regularity：若输入 Cholesky factors 属于 regular 类，则 barycenter 也保持 regular。

## 5. 数值实验理解

实验使用多个 AR(1) 高斯过程，比较 adapted Bures-Wasserstein barycenter 与 classical Bures-Wasserstein barycenter。结果显示：

- adapted barycenter 在 Cholesky factor `L` 层面工作，因此能看到 AR 参数 `α_i` 的正负号；
- 对称正负 AR 参数会在 adapted barycenter 中相互抵消；
- classical barycenter 在 covariance `Σ = LL^T` 层面工作，协方差对 `α_i` 符号不敏感，因此无法捕捉这种时间方向/信息传播差异；
- 两者主要差异体现在 marginal variances、covariance heatmap 和 Cholesky heatmap 的对角结构。

这说明 adapted OT 不只是普通 Wasserstein 的技术变体，而是真正改变了“随机过程相似性”的定义。

## 6. 与 Causal/adapted OT 的关系

这篇论文是 causal/adapted OT 在 barycenter 问题中的最新理论代表。它说明：当对象是 stochastic processes 时，平均模型不能只平均路径分布，还应保留时间信息结构。Cholesky factor 视角尤其重要，因为它直接编码噪声从过去到未来的传播方式。

## 7. 局限与开放问题

论文列出多个开放方向：

- **非高斯 barycenter**：存在性较一般，但唯一性和结构刻画仍开放。
- **连续时间扩展**：当前结果在离散时间；扩展到 Brownian diffusion、Ornstein-Uhlenbeck 等连续时间过程并不直接。
- **geodesic structure**：列分解与 adapted Wasserstein 空间几何之间关系仍需深入研究。
- **应用验证**：金融、多阶段随机优化、时序统计中的实际表现需要进一步实验。

## 8. 对后续研究的启发

对轨迹分布、时间序列策略和动态系统建模而言，普通 Wasserstein 距离可能过于静态。若比较对象包含信息流和因果时间结构，应优先考虑 adapted/causal OT。本文提供了一个非常清楚的例子：classical barycenter 会丢失 AR 参数符号，而 adapted barycenter 可以保留这种动态结构。
