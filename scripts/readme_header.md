# Awesome OT Variants

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Proceedings papers](https://img.shields.io/badge/proceedings%20%2B%20accepted-{proceedings}-orange.svg)](#3-20242026-正式会议论文目录) [![Preprints](https://img.shields.io/badge/tracked%20preprints-{preprints}-lightgrey.svg)](#4-20252026-前沿预印本不要与会议论文混写) [![Deep reads](https://img.shields.io/badge/deep--read%20reports-{deep_reads}-green.svg)](INDEX.md) [![Last recheck](https://img.shields.io/badge/venue%20recheck-{recheck}-blueviolet.svg)](#02-用户指定会议的时间覆盖)

An evidence-first (Chinese) reading map of **optimal transport variants**, 2024–2026: entropic / GPU Sinkhorn, unbalanced & partial OT, Wasserstein barycenters, multi-marginal OT, Gromov–Wasserstein, Riemannian OT, Schrödinger bridges & flow matching, statistical OT. The full reference catalog is rendered below; the repo also ships a vetted textbook guide and {deep_reads} deep-read paper reports. Sister repo: [awesome_diffusion_OT](https://github.com/asimfish/awesome_diffusion_OT).

**最优传输变种**的证据优先阅读地图（2024–2026）。目标不是堆论文标题，而是先建立坐标系（六类 OT 变种如何相互关联、各自解决什么问题），再按会议与理论主线追前沿；所有会议归属只认官方论文集或官方接收记录，正式论文 **[P]**、已接收论文 **[A]**、预印本 **[R]**、教材 **[B]** 永远分开标。

## 仓库导航

| 文档 | 内容 |
|---|---|
| 本页下方 | 深度参考目录全文（与 [`OT_DEEP_REFERENCE_CATALOG_2026.md`](OT_DEEP_REFERENCE_CATALOG_2026.md) 同源，由 `scripts/build_readme.py` 生成） |
| [`INDEX.md`](INDEX.md) | 文档地图与 {deep_reads} 篇精读论文一览；每篇在 `<arxiv_id>_<slug>/` 下有 `metadata.json` 与中文 `report.md` |
| [`OT_SURVEY_PROGRESS_REPORT_20260825.html`](OT_SURVEY_PROGRESS_REPORT_20260825.html) | 阶段汇报：需求对照 → 资料库结构图 → 覆盖统计 → 核心发现 → 双口径核验 → 下一步（浏览器打开） |
| [`BOOK_READING_GUIDE.md`](BOOK_READING_GUIDE.md) | 十份教材/教程的版本核验、内容解读与 12 周学习路线 |
| [`OT_FRONTIER_2026.md`](OT_FRONTIER_2026.md) | 2026 前沿：FlashSinkhorn、Riemannian OT、barycenter、MMOT、SB / flow matching |
| [`OT_VARIANTS_SURVEY_REPORT.md`](OT_VARIANTS_SURVEY_REPORT.md) | 六类 OT 变种的系统讲解、横向比较与研究建议 |
| [`METHOD_SELECTION_ROADMAP.md`](METHOD_SELECTION_ROADMAP.md) | 从具体问题反推该用哪种 OT 变种与算法路线 |
| [`book/OPEN_SOURCE_BOOKS.md`](book/OPEN_SOURCE_BOOKS.md) | 开源教材的来源、许可与校验记录 |

仓库**不含**论文 PDF 与抽取全文（版权与体积），只含笔记与元数据。原始工作区在本地 `~/Desktop/research/ot_variants_survey`，更新后运行 `scripts/sync_from_survey.sh` 同步并重建本页。*维护：[asimfish](https://github.com/asimfish)。*

## 目录

{toc}

---

