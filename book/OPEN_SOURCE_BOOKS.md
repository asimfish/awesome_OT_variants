# 开源教材来源与许可记录

本文件记录目录内由本次调研新增的开放教材。它既是可复现下载记录，也是后续分享、引用和再分发时的许可提醒。

## Discrete Stochastic Processes

| 字段 | 内容 |
|---|---|
| 作者 | Robert G. Gallager |
| 版本 | Draft of 2nd Edition，2011-01-31 |
| 对应课程 | MIT 6.262, *Discrete Stochastic Processes*, Spring 2011 |
| 本地文件 | `Discrete_Stochastic_Processes_Gallager_MIT_OCW.pdf` |
| 页数 | 392 |
| 文件大小 | 5,148,697 bytes |
| SHA-256 | `0adf9c96acdb3457aaf1a9a923c32f04348f79f0488181c0d365a7095e88790f` |
| 官方课程页 | <https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/> |
| 官方许可说明 | <https://ocw.mit.edu/pages/privacy-and-terms-of-use/> |
| 许可 | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（CC BY-NC-SA 4.0）；以 MIT OCW 当前许可页为准 |

### 本地文件如何生成

MIT OCW 将正文按前言、七章和附录分别提供。这里下载的是课程页链接到的九份官方 PDF，并按原顺序合并为一个便于检索的文件；没有增删正文。合并后使用 Ghostscript 10.07.1 重建交叉引用表，解决原始分章 PDF 合并时的 xref 警告。

校验结果：

- `pdfinfo`：392 页、未加密、无可疑对象；
- 首尾页均可由 `pdftotext` 正常抽取；
- 末页保留 MIT OpenCourseWare 来源和 Terms of Use 提示。

### 使用与引用提醒

- 分享或改编时保留作者、课程、MIT OpenCourseWare 和许可归属；
- 该许可包含“非商业”和“相同方式共享”要求；
- 学术引用宜引用作者、书名、版本和 MIT OCW 课程页，不要只引用本地文件名；
- 本记录不是法律意见；若用途超出个人学习或学术研究，应再次核对 MIT OCW 最新条款。
