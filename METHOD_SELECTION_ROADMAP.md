# OT 变种方法选型与研究路线图

## 1. 快速选型表

| 你的问题 | 首选 OT 变种 | 备选/组合 | 关键判断 |
|---|---|---|---|
| 多个分布要同时对齐 | Multi-marginal OT | Multi-marginal SB | 是否只有静态样本，还是有时间路径？ |
| 多个分布要取中心代表 | Wasserstein barycenter | Adapted barycenter / signed barycenter | 权重是否全为正？对象是否是随机过程？ |
| 存在 outlier、遮挡、缺失对应 | Partial OT | Partial GW / unbalanced OT | 未匹配质量是噪声还是真实质量变化？ |
| 两个对象没有共享坐标系 | Gromov-Wasserstein | Fused GW / Z-GW | 只比较结构，还是结构+属性都要比较？ |
| 要从简单分布生成复杂分布 | Schrödinger Bridge | Flow matching / diffusion OT | 是否需要参考过程和路径级控制解释？ |
| 比较时间序列/随机过程且不能看未来 | Causal/adapted OT | Adapted barycenter / causal SB | 信息流/filtration 是否是任务核心？ |
| 比较图中一个子结构 | Partial fused GW | Partial OT + graph features | 是否需要同时匹配节点属性和边结构？ |
| 从多个时间快照推断轨迹 | Multi-marginal SB | MMOT + dynamic regularization | 中间边缘约束是否重要？ |

## 2. 六类变种的“问题模板”

### 2.1 Multi-marginal OT

**适合问的问题**：

- 多个 domain / task / modality 是否存在共同对齐结构？
- 多个时间点或多组分布能否一次性联合匹配？
- pairwise matching 是否会产生不一致循环？

**不适合时机**：只有两个分布，且没有全局一致性需求时，标准 OT 更简单。

### 2.2 Wasserstein barycenter

**适合问的问题**：

- 多个分布的“平均形状”是什么？
- 多个模型/场景/轨迹分布的代表对象是什么？
- 是否需要在分布空间中做插值、聚类中心或模板？

**注意事项**：signed barycenter 能表达外推，但负权会引入非凸和稳定性问题。

### 2.3 Partial OT

**适合问的问题**：

- 是否只有一部分点/节点/质量真的应该匹配？
- outlier 是否很多？
- 是否有遮挡、缺失、伪关键点或多余节点？

**核心超参**：匹配质量或不匹配惩罚。惩罚太小会漏匹配，太大会强制错匹配。

### 2.4 Gromov-Wasserstein

**适合问的问题**：

- 两个对象是否没有共享坐标？
- 对齐依据是否来自内部距离、邻接、关系或结构？
- 节点属性是否也重要？若重要，使用 fused GW。

**注意事项**：GW 通常非凸，结果依赖初始化和正则化；解释 coupling 时要小心。

### 2.5 Schrödinger Bridge

**适合问的问题**：

- 是否要学习一条从源分布到目标分布的随机路径？
- 是否有自然参考过程/先验动力学？
- 是否希望生成过程最小偏离先验？
- 是否需要连接 diffusion、flow matching、control？

**注意事项**：SB 是路径测度语言，不只是静态距离。若任务没有动态路径需求，直接 OT 或 barycenter 可能足够。

### 2.6 Causal/adapted OT

**适合问的问题**：

- 对象是否是时间序列或随机过程？
- 比较时是否不能使用未来信息？
- 信息结构、filtration、non-anticipativity 是否影响模型含义？

**注意事项**：普通 Wasserstein 把整条路径当静态向量，可能误判动态系统相似性。

## 3. 面向机器人/轨迹研究的组合路线

### 路线 A：路径分布桥接

- **核心工具**：Schrödinger Bridge
- **组合工具**：Multi-marginal SB、causal/adapted OT
- **问题形式**：从 naive / short-horizon / low-budget path distribution 到 coherent long-horizon path distribution。
- **关键实验**：source distribution ablation、budget reduction、trajectory diversity、new map generalization。

### 路线 B：部分轨迹/关键点对齐

- **核心工具**：Partial OT
- **组合工具**：Partial fused GW
- **问题形式**：演示轨迹、视觉关键点或技能阶段存在缺失、遮挡、冗余。
- **关键实验**：outlier rate、missing keypoint rate、partial matching precision/recall。

### 路线 C：任务图/技能图结构比较

- **核心工具**：GW / Fused GW / Z-GW
- **组合工具**：Partial GW
- **问题形式**：比较两个任务结构、技能依赖图或状态转移图。
- **关键实验**：图扰动鲁棒性、节点属性噪声、结构迁移。

### 路线 D：多场景代表模型

- **核心工具**：Wasserstein barycenter
- **组合工具**：Adapted barycenter
- **问题形式**：多个场景、多个时间序列模型或多个策略分布需要一个中心代表。
- **关键实验**：中心模型是否保持动态结构、对极端场景的鲁棒性。

## 4. 三个最值得继续深挖的交叉点

### 4.1 Partial + GW

这条线解决“结构对象只有部分可匹配”的现实问题。对应候选文献包括 `2411.02198`、`2502.09934`、`2406.19767`。它非常适合图、子图、关键点、技能图和多模态结构匹配。

### 4.2 Multi-marginal + SB

这条线解决“多个时间快照/多个边缘约束下的动态路径推断”。对应候选文献 `2506.10168`。它比 pairwise bridge 更适合多时间点科学数据、细胞轨迹、气象、经济系统，也适合多阶段轨迹生成。

### 4.3 Causal/adapted + SB

这条线目前更像开放研究方向。SB 给路径测度和参考过程；causal/adapted OT 给非前视和信息结构。结合后可形成既尊重动态先验、又不偷看未来的路径分布桥。对于机器人策略、金融和多阶段决策尤其重要。

## 5. 下一步建议

若继续做第三轮，建议不要再泛泛扩展六类主题，而是选择一个主线：

1. **机器人/路径分布主线**：下载并精读 `2506.10168`、`2602.15396`、`2406.19810`。
2. **图匹配/结构主线**：下载并精读 `2502.09934`、`2406.19767`、`2411.02198`。
3. **理论统一主线**：下载并精读 `2509.22494`、`2411.02198`、`2406.19810`。
4. **数值算法主线**：下载并精读 `2510.04602`、`2507.09206`、`2508.02364`。

我建议优先走 **机器人/路径分布主线**，因为它与 Schrödinger Bridge、multi-marginal constraints 和 causal/adapted information flow 都有关，最可能服务后续 embodied / trajectory 研究。
