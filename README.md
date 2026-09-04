# Awesome OT Variants

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Proceedings papers](https://img.shields.io/badge/proceedings%20%2B%20accepted-111-orange.svg)](OT_DEEP_REFERENCE_CATALOG_2026.md) [![Preprints](https://img.shields.io/badge/tracked%20preprints-11-lightgrey.svg)](OT_DEEP_REFERENCE_CATALOG_2026.md) [![Deep reads](https://img.shields.io/badge/deep--read%20reports-12-green.svg)](INDEX.md)

An evidence-first (Chinese) reading map of **optimal transport variants**, 2024–2026: entropic / GPU Sinkhorn, unbalanced & partial OT, Wasserstein barycenters, multi-marginal OT, Gromov–Wasserstein, Riemannian OT, Schrödinger bridges & flow matching, statistical OT. Ships with a vetted textbook guide, a conference-organised reference catalog, and 12 deep-read paper reports. Sister repo: [awesome_diffusion_OT](https://github.com/asimfish/awesome_diffusion_OT).

**最优传输变种**的证据优先阅读地图（2024–2026）。目标不是堆论文标题，而是先建立坐标系（六类 OT 变种如何相互关联、各自解决什么问题），再按会议与理论主线追前沿；所有会议归属只认官方论文集或官方接收记录，正式论文、已接收论文与预印本永远分开标。

## 从这里开始

| 文档 | 内容 |
|---|---|
| [`INDEX.md`](INDEX.md) | 总入口：文档地图、12 篇精读论文一览 |
| [`OT_SURVEY_PROGRESS_REPORT_20260825.html`](OT_SURVEY_PROGRESS_REPORT_20260825.html) | 阶段汇报：需求对照 → 资料库结构图 → 覆盖统计 → 核心发现 → 双口径核验 → 下一步（浏览器打开） |
| [`OT_DEEP_REFERENCE_CATALOG_2026.md`](OT_DEEP_REFERENCE_CATALOG_2026.md) | 深度参考目录：111 篇正式/已接收论文 + 11 篇跟踪预印本，按理论主线、指定会议、课程、博客、软件组织 |
| [`BOOK_READING_GUIDE.md`](BOOK_READING_GUIDE.md) | 十份教材/教程的版本核验、内容解读与 12 周学习路线 |
| [`OT_FRONTIER_2026.md`](OT_FRONTIER_2026.md) | 2026 前沿：FlashSinkhorn、Riemannian OT、barycenter、MMOT、SB / flow matching |
| [`OT_VARIANTS_SURVEY_REPORT.md`](OT_VARIANTS_SURVEY_REPORT.md) | 六类 OT 变种的系统讲解、横向比较与研究建议 |
| [`METHOD_SELECTION_ROADMAP.md`](METHOD_SELECTION_ROADMAP.md) | 从具体问题反推该用哪种 OT 变种与算法路线 |

## 精读论文

12 个 `<arxiv_id>_<slug>/` 子目录，各含 `metadata.json` 与中文 `report.md`（问题 / 方法 / 理论 / 实验数字 / 局限 / 启发）。覆盖 GPU Sinkhorn、Riemannian (entropic) neural OT、exact / unified / signed / adapted barycenter、dynamical MMOT、partial OT、Gromov–Wasserstein、Schrödinger bridge。完整元数据见 [`PAPERS_MANIFEST.json`](PAPERS_MANIFEST.json)。

## 证据分级与会议覆盖

- **[P] Proceedings** 正式论文集 · **[A] Accepted** 官方 OpenReview 已接收但论文集未归档 · **[R] Preprint** 预印本 · **[B] Book/Notes** 教材讲义。
- 正式/已接收论文分会议：ICML 32（含 2026 已接收 16）、ICLR 21、AAAI 18、NeurIPS 16、CVPR 15、ICCV 5、ECCV 4；预印本 11。数字为 2026-08-25 程序化逐节统计，见汇报 §3。
- 时效复检：NeurIPS 2026、ECCV 2026 论文集尚未发布，不用预印本占位；复检日期记录在目录文档头。

## 关于 PDF

仓库**不含**论文 PDF 与抽取全文（版权与体积），只含笔记与元数据。教材的来源、许可与校验记录见 [`book/OPEN_SOURCE_BOOKS.md`](book/OPEN_SOURCE_BOOKS.md)。原始工作区在本地 `~/Desktop/research/ot_variants_survey`，更新后运行 `scripts/sync_from_survey.sh` 同步到本仓库。

*维护：[asimfish](https://github.com/asimfish)。*
