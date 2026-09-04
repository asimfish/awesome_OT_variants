# 中文阅读报告：Learning Partial Graph Matching via Optimal Partial Transport

## 1. 基本信息

- **论文标题**：Learning Partial Graph Matching via Optimal Partial Transport
- **arXiv**：2410.16718
- **对应 OT 变种**：Partial OT / Optimal Partial Transport
- **本地文件**：`paper.pdf`、`paper.txt`

## 2. 论文要解决的问题

图匹配通常假设两个图之间存在完整的一一对应。但真实任务中，经常只有部分节点有对应关系：

- 图像关键点存在遮挡、缺失或错误标注；
- 生物网络中部分蛋白没有对应物；
- 两个对象只局部相似；
- outlier 节点不应被强制匹配。

Partial graph matching 因此需要同时决定：哪些节点匹配、哪些节点不匹配、匹配关系是什么。论文认为现有深度图匹配方法常依赖 dummy node、ILP 或先估计匹配数量 `k`，可能带来复杂度高、误差传播或表示扭曲。

本文目标是：**用 optimal partial transport 建立一个既能表达未匹配节点，又能高效精确求解的 partial graph matching 目标。**

## 3. 核心方法

论文引入带 weighted total variation 的 optimal partial transport 目标。其基本思想是：

- `C_ij` 表示节点 `i` 和节点 `j` 的匹配代价；
- `α_i` 和 `β_j` 表示节点被匹配/不匹配的偏置或重要性；
- 参数 `ρ` 控制匹配代价与不匹配惩罚之间的权衡；
- 若 `C_ij > ρ(α_i + β_j)`，则该边不应匹配。

论文证明在 unit-weighted 情况下，存在一个最优解是合法 partial assignment，即每个节点最多匹配一个节点，或者保持 unmatched。

最关键的算法步骤是：把 partial graph matching 嵌入到 linear sum assignment problem。作者通过添加 dummy elements 构造新的代价矩阵，再用 Hungarian algorithm 求解线性分配，最后通过闭式映射 `h` 得到原 partial matching 的最优解。

## 4. 主要贡献

- **新的 partial matching 目标**：用 optimal partial transport 平衡匹配节点与未匹配节点。
- **理论可解性**：证明目标存在 partial assignment 型最优解。
- **嵌入线性分配问题**：将 partial graph matching 转换为 linear sum assignment，从而用 Hungarian algorithm 精确求解。
- **三次复杂度**：最坏时间复杂度为 `O(n^3)`。
- **深度学习集成**：将该求解模块与图神经网络/affinity matrix 学习结合，形成 OPGM/OPGM-rs 方法。

## 5. 实验与结果理解

论文在三类任务上验证：

- **图像关键点匹配**：SPair-71K、IMCPT 50/100、Pascal VOC Keypoint。
- **PPI 网络匹配**：评估在不同噪声比例下的节点正确率。
- **效率分析**：比较不同 partial matching head 的推理时间。

在 SPair-71K 上，OPGM-rs 取得最高平均 F1（57.7 ± 0.2），优于 NGM-v2、GCAN、AFAT-U、AFAT-I 等基线。在 IMCPT 100 上，OPGM-rs 的平均 F1 也优于主要基线，同时推理时间明显更低。PPI 网络匹配中，OPGM-rs 在各噪声水平下表现稳定优于 SIGMA 和 StableGM，但高噪声时差距缩小。

论文还分析了参数敏感性：`ρ` 很关键，太小会过度限制有效匹配，太大会允许错误匹配；正则参数 `λ` 的影响相对较小。

## 6. 与 Partial OT 的关系

这篇论文展示了 partial OT 在图匹配中的一个清晰应用：未匹配节点不是事后剔除，而是在运输目标中被直接建模。Partial OT 的优势在于，它让“是否匹配”成为优化问题的一部分，而不是强制所有节点都进入匹配。

## 7. 局限与开放问题

- **标注质量敏感**：论文承认在标注不可靠、语义模糊或高噪声情况下性能下降。
- **参数 `ρ` 需要调节**：它直接影响匹配/不匹配边界。
- **主要验证在特定图匹配框架内**：推广到更大规模动态图、异构图或多模态结构仍需验证。
- **理论目标与深度特征质量耦合**：即使 partial OT 求解精确，前端 affinity/cost 学得不好仍会影响最终匹配。

## 8. 对后续研究的启发

对于机器人视觉、轨迹关键点、任务阶段对齐等存在缺失和 outlier 的问题，这篇论文提示我们：不要强制全量匹配，而应显式建模 unmatched 的成本。它也说明 partial OT 可以与神经网络模块结合，作为可解释的匹配层或后处理层。
