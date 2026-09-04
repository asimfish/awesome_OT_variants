# OT Variants 扩展阅读清单（Round 2）

本清单是在首轮 6 篇已下载论文之外，继续检索得到的可验证候选文献。此轮只整理扩展阅读与选题地图，**未批量下载 PDF**，避免在无明确指令下制造大量文件。

> 2026-07-30 更新：`2509.22494` 已在 Round 3 下载并精读；FlashSinkhorn、Riemannian OT 和两条 exact barycenter 路线等新增材料见 `OT_FRONTIER_2026.md` 与 `INDEX.md`。本文件保留为 Round 2 的候选清单快照。

## 1. Multi-marginal OT

### arXiv:2509.22494 — A dynamical formulation of multi-marginal optimal transport

- **URL**：https://arxiv.org/abs/2509.22494
- **检索摘要定位**：提出 multi-marginal OT 的 primal-dual dynamical formulation，面向 semi-convex cost，并扩展 Benamou-Brenier 式动态 OT 思路。
- **为什么值得读**：首轮 MMOT 论文偏随机交换/离散算法；这篇更偏连续动态表述，可补足“MMOT 的动态规划/流体力学视角”。
- **建议阅读重点**：动态变量、primal-dual 结构、semi-convex cost 条件、与 Benamou-Brenier 的差异。

### arXiv:2507.09206 — A deep learning approach to multi-marginal optimal transport

- **URL**：https://arxiv.org/abs/2507.09206
- **检索摘要定位**：提出求解 multi-marginal Monge problem 的数值方法，使用 probability measure 的 Hilbert space embedding 和 penalization。
- **为什么值得读**：可作为“神经求解 MMOT”的代表，与 collision-based 离散求解互补。
- **建议阅读重点**：Monge formulation、多目标分布、embedding 损失、训练稳定性和可扩展性。

## 2. Wasserstein barycenter

### arXiv:2510.04602 — Wasserstein Gradient Flows for Scalable and Regularized Barycenter Computation

- **URL**：https://arxiv.org/abs/2510.04602
- **检索摘要定位**：研究可扩展、正则化的 barycenter 计算，并与 Wasserstein gradient flows 关联。
- **为什么值得读**：首轮 signed barycenter 偏理论；这篇更偏 scalable computation，可补足工程和数值算法方向。
- **建议阅读重点**：正则化形式、gradient-flow 解释、复杂度、与 Sinkhorn barycenter/固定点方法的比较。

### arXiv:2602.09181 — Weighted Wasserstein Barycenter of Gaussian Processes

- **URL**：https://arxiv.org/abs/2602.09181
- **检索摘要定位**：将 Wasserstein barycenter 用于 Gaussian processes，并与 Bayesian optimization acquisition functions 建立联系。
- **为什么值得读**：与 causal/adapted barycenter 的高斯过程主题相邻，但这里更接近 classical Wasserstein / BO 应用。
- **建议阅读重点**：GP barycenter 的计算简化、acquisition function 重解释、与 adapted barycenter 的差异。

## 3. Partial OT 与 Partial/Robust GW

### arXiv:2411.02198 — Metric properties of partial and robust Gromov-Wasserstein distances

- **URL**：https://arxiv.org/abs/2411.02198
- **检索摘要定位**：研究 partial 和 robust GW 距离的 metric properties。
- **为什么值得读**：它正好连接 partial OT 与 GW，是首轮两个主题之间的桥。
- **建议阅读重点**：partial GW 定义、robust GW 定义、metric / pseudometric 条件、与 outlier 处理的关系。

### arXiv:2502.09934 — Fused Partial Gromov-Wasserstein for Structured Objects

- **URL**：https://arxiv.org/abs/2502.09934
- **检索摘要定位**：面向 structured data/graphs，提出 fused partial GW，同时处理结构和特征，允许部分匹配。
- **为什么值得读**：它是“partial + fused GW + structured objects”的应用型代表，可补足首轮 partial graph matching 和 Z-GW 理论之间的实践路线。
- **建议阅读重点**：部分质量约束、节点特征融合、图结构匹配、实际 benchmark。

### arXiv:2406.19767 — Subgraph Matching via Partial Optimal Transport

- **URL**：https://arxiv.org/abs/2406.19767
- **检索摘要定位**：将 subgraph matching 表述为 partial fused Gromov-Wasserstein 问题。
- **为什么值得读**：它比首轮 partial graph matching 更直接处理“查询子图在大图中出现”的应用。
- **建议阅读重点**：subgraph matching 目标、partial fused GW 构造、与传统子图同构/图匹配方法的比较。

## 4. Schrödinger Bridge

### arXiv:2506.10168 — Momentum Multi-Marginal Schrödinger Bridge Matching

- **URL**：https://arxiv.org/abs/2506.10168
- **检索摘要定位**：面向稀疏快照下的复杂系统轨迹推断，提出 multi-marginal SB matching。
- **为什么值得读**：直接连接 multi-marginal OT 与 Schrödinger Bridge，是“多时间点边缘约束 + 动态路径测度”的关键候选。
- **建议阅读重点**：多边缘约束、momentum 建模、与 pairwise bridge/flow matching 的差异、单细胞/气象等应用。

### arXiv:2510.11829 — Schrödinger bridge for generative AI: Soft-constrained ...

- **URL**：https://arxiv.org/abs/2510.11829
- **检索摘要定位**：将生成 AI 中从简单参考测度到复杂数据分布的学习问题与 SBP 联系起来，并强调 soft-constrained 形式。
- **为什么值得读**：可作为 SB 在生成 AI 中更应用导向的补充。
- **建议阅读重点**：soft constraint 与 hard marginal constraint 的差异、生成模型训练目标、相对熵正则。

### arXiv:2602.15396 — Efficient Generative Modeling beyond Memoryless ... / Adjoint Schrödinger Bridge Matching

- **URL**：https://arxiv.org/abs/2602.15396
- **检索摘要定位**：提出 Adjoint Schrödinger Bridge Matching，批评 memoryless forward process 会导致弯曲轨迹和 noisy score targets。
- **为什么值得读**：与首轮 SB foundations 中的 adjoint matching 主题直接相关，适合深入“更优参考过程/非 memoryless coupling”。
- **建议阅读重点**：adjoint 训练目标、参考过程设计、轨迹曲率、采样效率。

## 5. Causal / adapted OT

### arXiv:2406.19810 — A Probabilistic View on the Adapted Wasserstein Distance

- **URL**：https://arxiv.org/abs/2406.19810
- **检索摘要定位**：从概率视角解释 adapted Wasserstein distance；摘要明确关联 causal optimal transport 与 adapted Wasserstein。
- **为什么值得读**：适合作为 adapted Wasserstein 的基础入门，与首轮高斯过程 barycenter 论文互补。
- **建议阅读重点**：probabilistic characterization、causal coupling、adapted distance 与普通 Wasserstein 的差异。

### arXiv:2303.14085 — Optimal transport and Wasserstein distances for causal models

- **URL**：https://arxiv.org/abs/2303.14085
- **检索摘要定位**：在有向图 causal structure 下定义 OT 变体；不同图结构给出不同 OT 问题，完全连接图退化为标准 OT。
- **为什么值得读**：虽然不是 2024-2026，但它是 causal graph 结构与 OT 距离结合的重要背景。
- **建议阅读重点**：DAG/graph-conditioned OT、causal model distance、与 adapted/filtration 视角的关系。

## 6. 推荐下一步下载优先级

如果只继续下载 3 篇，建议优先：

1. **arXiv:2506.10168**：Momentum Multi-Marginal Schrödinger Bridge Matching。原因：同时连接 MMOT、SB、动态多边缘约束。
2. **arXiv:2502.09934**：Fused Partial Gromov-Wasserstein for Structured Objects。原因：同时连接 partial OT、GW、structured graph 应用。
3. **arXiv:2406.19810**：A Probabilistic View on the Adapted Wasserstein Distance。原因：补足 causal/adapted OT 的基础理解。

如果目标是工程实现或实验路线，则优先 `2510.04602` 和 `2507.09206`；如果目标是理论统一，则优先 `2509.22494`、`2411.02198`、`2406.19810`。
