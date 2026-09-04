# Thinking Log: OT Variants Survey

## Round 1 思考记录

**主题**：multi-marginal OT、Wasserstein barycenter、partial OT、Gromov-Wasserstein、Schrödinger Bridge、causal/adapted OT 的概念解释与近期论文阅读。

**实际查询/来源策略**：以 2024-2026 arXiv 代表论文为主，覆盖每个变种至少一篇可验证来源；结合已有本地 OT/SB 材料进行概念对齐，但本轮新增来源以 `PAPERS_MANIFEST.json` 中 6 个 arXiv ID 为准。

**新读论文**：

- arXiv:2412.16385 — collision-based dynamics for MMOT。
- arXiv:2602.05976 — signed Wasserstein barycenter。
- arXiv:2410.16718 — optimal partial transport for graph matching。
- arXiv:2408.08233 — Z-Gromov-Wasserstein distance。
- arXiv:2603.18992 — foundations of SB for generative modeling。
- arXiv:2604.22453 — adapted Wasserstein barycenters of Gaussian processes。

**核心发现**：六类 OT 变种可被统一理解为对经典 Kantorovich OT 的不同轴向扩展：MMOT 扩展边缘数量；barycenter 从两分布距离扩展到多分布中心；partial OT 放松全质量匹配；GW 取消共享坐标系，转为内部结构比较；SB 将静态耦合提升为参考随机过程附近的路径测度；causal/adapted OT 在随机过程运输中加入时间信息约束。

**与已知材料的关系**：SB 论文与本地 Schrödinger Bridge 学习笔记一致，都强调 `reference process + marginal constraints + KL minimization`。Causal/adapted OT 与路径分布研究也高度相关，因为它提醒我们比较轨迹时不能只把整条路径当静态向量，否则会忽略信息流和非前视约束。

**新问题**：

1. partial OT 与 GW 如何结合成 partial/fused GW，用于只有部分节点可对应的结构图？
2. adapted Wasserstein 能否作为机器人轨迹分布评估指标，避免未来信息泄露？
3. SB 与 causal/adapted OT 是否可结合，形成既有路径熵正则又尊重 filtration 的桥模型？

**下一步探索方向**：搜索 `partial Gromov-Wasserstein matching`, `causal Schrödinger bridge`, `adapted optimal transport generative modeling`, `multi-marginal Schrödinger bridge`。

**知识图谱更新**：新增 6 个 paper nodes、6 个 variant concept nodes，并加入 `studies`、`extends`、`applies_to` 关系。

## Round 2 思考记录

**主题**：在首轮 6 篇精读报告基础上，继续扩展候选文献，并转向方法选型和研究路线图。

**实际查询/来源策略**：

- `site:arxiv.org/abs multi-marginal optimal transport 2025 arXiv`
- `site:arxiv.org/abs Wasserstein barycenter 2026 arXiv`
- `site:arxiv.org/abs partial optimal transport Gromov Wasserstein 2025 arXiv`
- `site:arxiv.org/abs causal optimal transport adapted Wasserstein 2025 2026 arXiv`
- `site:arxiv.org/abs Schrodinger bridge generative modeling 2025 arXiv multi marginal unbalanced`
- `site:arxiv.org/abs Gromov Wasserstein graph matching 2025 arXiv fused partial robust`

**新来源**：

- arXiv:2509.22494 — A dynamical formulation of multi-marginal optimal transport。
- arXiv:2510.04602 — Wasserstein Gradient Flows for Scalable and Regularized Barycenter Computation。
- arXiv:2411.02198 — Metric properties of partial and robust Gromov-Wasserstein distances。
- arXiv:2502.09934 — Fused Partial Gromov-Wasserstein for Structured Objects。
- arXiv:2506.10168 — Momentum Multi-Marginal Schrödinger Bridge Matching。
- arXiv:2602.15396 — Adjoint Schrödinger Bridge Matching 相关生成建模论文。
- arXiv:2406.19810 — A Probabilistic View on the Adapted Wasserstein Distance。
- arXiv:2303.14085 — Optimal transport and Wasserstein distances for causal models。

**核心发现**：首轮的六类 OT 变种不是六条平行线，而存在三个特别值得深挖的交叉方向。第一是 `partial + GW`，用于有 outlier 或只有部分对应的结构对象；第二是 `multi-marginal + SB`，用于多个时间快照约束下的动态路径推断；第三是 `causal/adapted + SB`，用于既要路径测度桥接又要尊重时间信息结构的场景。

**与已知的关系**：`2506.10168` 将首轮的 MMOT 和 SB 连接起来；`2502.09934`、`2411.02198` 将 partial OT 和 GW 连接起来；`2406.19810` 为首轮 adapted Gaussian process barycenter 提供基础概率视角。

**新问题**：

1. Multi-marginal SB 是否可以作为多阶段轨迹/多时间快照建模的默认框架？
2. Partial fused GW 能否用于技能图、任务图或关键点结构的鲁棒匹配？
3. Causal/adapted OT 与 SB 的结合是否能避免路径生成评估中的未来信息泄露？

**本轮产物**：

- `EXTENDED_READING_LIST.md`
- `METHOD_SELECTION_ROADMAP.md`

**知识图谱更新**：新增 8 个扩展 paper nodes，新增 `crosses_with`、`supports_next_reading`、`extends` 方向的边，用于标记三条交叉研究线。

## Round 3 思考记录

**主题**：把用户提供的教材体系与截至 2026-07-30 的 OT 前沿对齐，重点核验 FlashSinkhorn、黎曼流形 OT、Wasserstein barycenter 和动态 MMOT。

**材料审计**：

- `OT_book.pdf` 核验为 Peyré–Cuturi 的 *Computational Optimal Transport*，是主干教材。
- `Multi_OT_book.pdf` 核验为 Luca Nenna 2016 博士论文 *Numerical Methods for Multi-Marginal Optimal Transportation*，是 MMOT 专题教材。
- 附件核验为 Durrett *Essentials of Stochastic Processes*，226 页。
- `book/随机过程_2.pdf` 只有 18 页，是陆大䋮、张颢教材的残缺片段，不能视为全书。
- 其余 Flow、VAE、RL、ESL、科研写作材料均按目录和正文定位到 OT 学习路线。

**新增精读**：

- arXiv:2602.03067 — FlashSinkhorn。
- arXiv:2602.03566 — Riemannian Neural Optimal Transport。
- arXiv:2605.04255 — Entropic Riemannian Neural Optimal Transport。
- arXiv:2505.13660 — Sobolev Gradient Ascent barycenter。
- arXiv:2605.11270 — Fisher–Rao unified barycenter。
- arXiv:2509.22494 — dynamical MMOT。

**核心判断**：

1. FlashSinkhorn 的创新属于 GPU IO 与 kernel fusion；它没有改变 entropic OT 目标，也没有消除 dense pairwise arithmetic。
2. “黎曼 OT”至少有四层含义：ground space 是流形、Wasserstein/Otto 几何、约束参数空间的 Riemannian optimization、流形上的生成流。混用会导致错误比较。
3. barycenter 不应只按论文新旧选方法，首先要在 exact/regularized、grid/point cloud、discrete/continuous、Euclidean/manifold 之间做问题分类。
4. MMOT 的现代可扩展性来自 cost 或 coupling 的结构，而非通用地处理 `N^K` tensor。
5. 教材中的 IPFP、Schrödinger problem、Benamou–Brenier 和 barycenter dual，正是理解这些 2025–2026 方法的共同基础。

**本轮产物**：

- `BOOK_READING_GUIDE.md`
- `OT_FRONTIER_2026.md`
- 6 个新增论文包（PDF、文本、元数据、中文报告）
- 更新后的 `INDEX.md`、`PAPERS_MANIFEST.json` 与 `LITERATURE_DB.md`

**建议下一步**：先按 `OT_book Ch.2–4 → Multi_OT Ch.3/7 → OT_book Ch.7/9` 建立公式和代码基线，再分别复现 FlashSinkhorn 与一种 exact barycenter；不要同时启动全部方向。
