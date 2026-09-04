# OT Variants Survey Index

> GitHub 镜像：<https://github.com/asimfish/awesome_OT_variants>（仓库位于 `~/Code/awesome_OT_variants`，只含 Markdown/JSON/HTML 笔记，不含 PDF 与抽取全文；本目录为原始工作区，更新后用仓库内 `scripts/sync_from_survey.sh` 同步）。
>
> 姊妹知识库：`../diffusion_ot_survey/`（2026-08-14 新建，30 agent 并行调研「扩散模型×OT」：451 篇文献、234 篇 PDF、调研报告与 ARIS 审计；与本库共用证据分级口径；GitHub 整理版 <https://github.com/asimfish/awesome_diffusion_OT>）。

## 建议从这里开始

- `OT_SURVEY_PROGRESS_REPORT_20260825.html`：项目阶段汇报（需求对照、资料库结构图、覆盖统计、核心发现、质量核验、下一步）；浏览器打开。
- `BOOK_READING_GUIDE.md`：十份教材/教程的版本核验、内容解读与 12 周学习路线；重点精读 `OT_book` 与 `Multi_OT_book`。
- `OT_DEEP_REFERENCE_CATALOG_2026.md`：2024–2026 深度参考目录；按理论主线、指定会议、课程、博客和软件组织，并严格区分正式论文、已接收论文与预印本。
- `book/OPEN_SOURCE_BOOKS.md`：新增开源教材的来源、许可、文件生成方式和校验记录。
- `OT_FRONTIER_2026.md`：截至 2026-07-30 的前沿调研，覆盖 FlashSinkhorn、Riemannian OT、Wasserstein barycenter、MMOT、SB/flow matching。
- `OT_VARIANTS_SURVEY_REPORT.md`：首轮六类 OT 变种的系统讲解、横向比较和研究建议。
- `METHOD_SELECTION_ROADMAP.md`：从具体问题反推 OT 变种和算法路线。

## 已精读并归档的论文

完整元数据见 `PAPERS_MANIFEST.json`。每个子目录均含原文 `paper.pdf`、抽取文本 `paper.txt`、元数据和中文 `report.md`。

| 主题 | 论文 | 状态 | 子目录 |
|---|---|---|---|
| GPU Sinkhorn | FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU | ICML 2026 Oral | `2602.03067_FlashSinkhorn/` |
| Riemannian OT | Riemannian Neural Optimal Transport | 2026 preprint | `2602.03566_Riemannian_Neural_OT/` |
| Riemannian entropic OT | Entropic Riemannian Neural Optimal Transport | 2026 preprint | `2605.04255_Entropic_Riemannian_Neural_OT/` |
| Exact barycenter | Sobolev Gradient Ascent for Optimal Transport | ICLR 2026 | `2505.13660_Sobolev_Barycenter/` |
| Discrete/continuous barycenter | A Unified Approach for Computing Wasserstein Barycenters | 2026 preprint | `2605.11270_Unified_Wasserstein_Barycenter/` |
| Dynamical MMOT | A dynamical formulation of multi-marginal optimal transport | 2025 preprint | `2509.22494_Dynamical_MMOT/` |
| MMOT | Collision-based Dynamics for Multi-Marginal OT | 2024 preprint | `2412.16385_CollisionDynamics_MultiMarginalOT/` |
| Signed barycenter | The Signed Wasserstein Barycenter Problem | 2026 preprint | `2602.05976_Signed_Wasserstein_Barycenter/` |
| Partial OT | Learning Partial Graph Matching via Optimal Partial Transport | 2024/2026 version | `2410.16718_OptimalPartialTransport_GraphMatching/` |
| Gromov-Wasserstein | The Z-Gromov-Wasserstein Distance | 2024 preprint | `2408.08233_Z_Gromov_Wasserstein/` |
| Schrödinger Bridge | Foundations of Schrödinger Bridges for Generative Modeling | 2026 preprint | `2603.18992_Foundations_SB_Generative_Modeling/` |
| Causal/adapted OT | Adapted Wasserstein Barycenters of Gaussian Processes | 2026 preprint | `2604.22453_Adapted_Wasserstein_Barycenters_GP/` |

## 其他研究文件

- `LITERATURE_DB.md`：精读论文和扩展候选的结构化文献条目。
- `EXTENDED_READING_LIST.md`：尚未全部精读的交叉方向候选文献。
- `THINKING_LOG.md`：三轮检索、综合洞察和开放问题。
- `THINKING_STATE.json`：首轮轻量知识图谱快照；以本索引和 `PAPERS_MANIFEST.json` 的当前状态为准。
