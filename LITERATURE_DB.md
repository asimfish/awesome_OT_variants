# Literature DB: OT Variants Survey

## arXiv:2412.16385 — Collision-based Dynamics for Multi-Marginal Optimal Transport

- **Year**：2024
- **URL**：https://arxiv.org/abs/2412.16385
- **Variant**：Multi-marginal OT
- **Summary**：提出基于 Boltzmann kinetics 类比的 collision-based dynamics，用随机二元样本交换近似求解离散 OT 与 MMOT。算法通过只交换样本索引保持边缘分布，针对 `L_p`-Wasserstein 代价给出 `O(nK^2N_p)` 复杂度估计。实验在 toy problem 和图像数据集上显示近似指数收敛、低内存和相对 Sinkhorn/EMD 的效率优势。
- **Claims**：随机局部 swap 可扩展到多边缘；边缘按构造保持；大规模多图像 marginal 可用于估计 Wasserstein 距离结构。
- **Limitations**：stationary solution 不等价于严格全局最优；收敛率主要由类比和实验支持；复杂代价和高语义任务仍需验证。
- **round_added**：1

## arXiv:2602.05976 — The Signed Wasserstein Barycenter Problem

- **Year**：2026
- **URL**：https://arxiv.org/abs/2602.05976
- **Variant**：Wasserstein barycenter
- **Summary**：研究带正负权重的 signed Wasserstein barycenter。负权破坏经典 barycenter 的凸性和测地凸性，因此需要新理论。论文证明一般代价下存在性，在单正权重情形给出凸插值与唯一性方向结果，并建立任意正负权重的 Kantorovich potentials min-max 对偶框架。
- **Claims**：signed barycenter 可用于 measure-valued regression 和 Wasserstein gradient flow 高阶数值格式；saddle point 可诱导 signed barycenter；stationary point 可在充分条件下升级为全局最优。
- **Limitations**：高维数值算法尚未系统展开；唯一性和全局最优依赖较强条件；负权带来本质非凸。
- **round_added**：1

## arXiv:2410.16718 — Learning Partial Graph Matching via Optimal Partial Transport

- **Year**：2024/2026 version
- **URL**：https://arxiv.org/abs/2410.16718
- **Variant**：Partial OT
- **Summary**：将 partial graph matching 表述为 optimal partial transport，引入 weighted total variation 和 matching bias，允许节点匹配或不匹配。理论上证明存在 partial assignment 型最优解，并将问题嵌入 linear sum assignment，用 Hungarian algorithm 精确求解，复杂度 `O(n^3)`。
- **Claims**：OPGM/OPGM-rs 在 SPair-71K、IMCPT、PPI 网络匹配中多数优于基线，并具有较低推理时间。
- **Limitations**：对标注质量和噪声敏感；`ρ` 参数对匹配/不匹配边界关键；依赖前端图特征和 affinity 学习质量。
- **round_added**：1

## arXiv:2408.08233 — The Z-Gromov-Wasserstein Distance

- **Year**：2024
- **URL**：https://arxiv.org/abs/2408.08233
- **Variant**：Gromov-Wasserstein
- **Summary**：提出 Z-Gromov-Wasserstein 距离，用一般度量空间 `Z` 中的关系值统一多种 GW-like 距离。证明标准 GW、Fused GW、Fused Network GW、spectral GW 等均为特例，并建立 metric、separability、completeness、contractibility、geodesicity、lower bounds 和 `R^n` 近似理论。
- **Claims**：Z-GW 是结构化对象 OT 的统一框架；许多既有 GW 变体的性质可由 `Z` 的性质统一推出。
- **Limitations**：通用数值算法仍初步；朴素计算需四维数组，时间/空间可达 `O(n^2m^2)`；测地、曲率和最优耦合结构仍有开放问题。
- **round_added**：1

## arXiv:2603.18992 — Foundations of Schrödinger Bridges for Generative Modeling

- **Year**：2026
- **URL**：https://arxiv.org/abs/2603.18992
- **Variant**：Schrödinger Bridge
- **Summary**：长篇 guide，将 SB 作为生成建模的统一理论框架。围绕最小相对熵路径测度原则，从静态 SB、动态 SB、path measure、随机最优控制、Doob h-transform、Markovian/reciprocal projection 推导到 diffusion SB matching、simulation-free score/flow matching、adjoint matching 和离散 CTMC SB。
- **Claims**：SB 可统一理解 diffusion models、flow matching 和 stochastic control；核心原则是满足边缘约束时对参考过程的 minimal-entropy deviation。
- **Limitations**：不是穷尽式算法综述；实验不是重点；数学门槛较高。
- **round_added**：1

## arXiv:2604.22453 — Adapted Wasserstein Barycenters of Gaussian Processes

- **Year**：2026
- **URL**：https://arxiv.org/abs/2604.22453
- **Variant**：Causal/adapted OT
- **Summary**：研究离散时间高斯过程的 adapted Wasserstein barycenter。证明存在性、高斯性、唯一性，并通过 adapted Bures-Wasserstein 几何和 Cholesky factor 列分解将问题化为多个 classical Bures-Wasserstein barycenter 子问题。给出 fixed-point characterization 和 alternating minimization algorithm。
- **Claims**：adapted barycenter 能保留时间信息结构；AR(1) 实验显示其在 Cholesky factor 层面捕捉参数符号，而 classical barycenter 在 covariance 层面可能丢失。
- **Limitations**：主要限于离散时间高斯过程；非高斯和连续时间情形仍开放；应用验证有待拓展。
- **round_added**：1

## arXiv:2509.22494 — A dynamical formulation of multi-marginal optimal transport

- **Year**：2025
- **URL**：https://arxiv.org/abs/2509.22494
- **Variant**：Multi-marginal OT
- **Summary**：检索摘要显示，该文提出 multi-marginal optimal transport 的 primal-dual dynamical formulation，面向 semi-convex cost，并扩展 Benamou-Brenier 风格动态 OT 到更一般代价与多边缘情形。
- **Claims**：MMOT 不只能用静态联合耦合或离散排列理解，也可通过动态 formulation 研究。
- **Limitations**：本轮仅基于 arXiv 检索摘要做扩展清单定位，尚未下载全文精读。
- **round_added**：2

## arXiv:2510.04602 — Wasserstein Gradient Flows for Scalable and Regularized Barycenter Computation

- **Year**：2025/2026 version
- **URL**：https://arxiv.org/abs/2510.04602
- **Variant**：Wasserstein barycenter
- **Summary**：检索摘要显示，该文关注 scalable and regularized barycenter computation，并以 Wasserstein gradient flows 作为计算视角。
- **Claims**：barycenter 计算可通过 gradient-flow/regularization 路线改善可扩展性。
- **Limitations**：本轮尚未下载全文；需进一步核查具体算法、复杂度和实验。
- **round_added**：2

## arXiv:2411.02198 — Metric properties of partial and robust Gromov-Wasserstein distances

- **Year**：2024
- **URL**：https://arxiv.org/abs/2411.02198
- **Variant**：Partial OT + Gromov-Wasserstein
- **Summary**：检索摘要显示，该文研究 partial and robust GW distances 的 metric properties，直接连接 partial OT 的 outlier/partial matching 与 GW 的结构对象比较。
- **Claims**：partial/robust GW 可为存在异常点、部分重叠或质量不完整的结构对象比较提供理论基础。
- **Limitations**：本轮尚未下载全文；需进一步核查其 metric 条件和与 Z-GW 的关系。
- **round_added**：2

## arXiv:2502.09934 — Fused Partial Gromov-Wasserstein for Structured Objects

- **Year**：2025
- **URL**：https://arxiv.org/abs/2502.09934
- **Variant**：Partial OT + Fused GW
- **Summary**：检索摘要显示，该文面向 structured data/graphs，提出 fused partial GW，同时比较节点特征和结构关系，并允许部分匹配。
- **Claims**：在结构对象中，partial matching 与 fused structural/feature matching 应联合建模。
- **Limitations**：本轮尚未下载全文；需后续验证 benchmark、算法细节和适用规模。
- **round_added**：2

## arXiv:2506.10168 — Momentum Multi-Marginal Schrödinger Bridge Matching

- **Year**：2025
- **URL**：https://arxiv.org/abs/2506.10168
- **Variant**：Schrödinger Bridge + Multi-marginal OT
- **Summary**：检索摘要显示，该文面向从稀疏 sample snapshots 推断复杂系统轨迹的问题，提出 momentum multi-marginal SB matching。
- **Claims**：pairwise bridge/flow matching 对多时间点快照不足，multi-marginal SB 可直接处理多个中间边缘约束。
- **Limitations**：本轮尚未下载全文；需进一步核查 momentum 变量、训练目标和应用实验。
- **round_added**：2

## arXiv:2602.15396 — Efficient Generative Modeling beyond Memoryless ... / Adjoint Schrödinger Bridge Matching

- **Year**：2026
- **URL**：https://arxiv.org/abs/2602.15396
- **Variant**：Schrödinger Bridge
- **Summary**：检索摘要显示，该文提出 Adjoint Schrödinger Bridge Matching，关注 memoryless forward process 导致的高曲率轨迹和 noisy score targets 问题。
- **Claims**：更有信息的参考过程或 adjoint matching 可能改善生成路径质量和训练效率。
- **Limitations**：本轮尚未下载全文；标题在检索摘要中被截断，需下载后确认完整标题和方法细节。
- **round_added**：2

## arXiv:2406.19810 — A Probabilistic View on the Adapted Wasserstein Distance

- **Year**：2024
- **URL**：https://arxiv.org/abs/2406.19810
- **Variant**：Causal/adapted OT
- **Summary**：检索摘要显示，该文从概率视角解释 adapted Wasserstein distance，并明确关联 causal optimal transport 与 adapted Wasserstein distance。
- **Claims**：adapted Wasserstein 可通过概率/耦合结构更直观地理解，是深入 causal OT 的基础入口。
- **Limitations**：本轮尚未下载全文；需进一步核查具体 probabilistic characterization。
- **round_added**：2

## arXiv:2303.14085 — Optimal transport and Wasserstein distances for causal models

- **Year**：2023
- **URL**：https://arxiv.org/abs/2303.14085
- **Variant**：Causal OT
- **Summary**：检索摘要显示，该文在底层有向图 causal structure 下定义 OT 变体，不同图结构对应不同 OT 问题，完全连接图退化为标准 OT。
- **Claims**：causal model 的结构信息可直接进入 OT 距离定义，而不只是事后解释。
- **Limitations**：年份稍早于本轮主窗口，但作为 causal OT 背景文献重要；尚未全文精读。
- **round_added**：2

## arXiv:2602.03067 — FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU

- **Year / status**：2026，ICML 2026 Oral
- **URL**：https://arxiv.org/abs/2602.03067
- **Variant**：Entropic OT / GPU systems
- **Summary**：把平方欧氏代价下的 log-domain Sinkhorn 更新改写为 attention-like biased LogSumExp，以 Triton fused kernel 流式计算，不物化 cost matrix 或 transport plan。forward、analytic gradient 和 HVP 均可使用线性显存。
- **Claims**：论文在 A100 的特定设置下报告最高 `32×` forward、`161×` end-to-end 加速；显存由 dense `O(nm)` 降为 `O((n+m)d)`。
- **Limitations**：算术量仍为 dense pairwise 的 `O(nmd)`；当前公开 API 聚焦平方欧氏代价；收益依赖硬件、维度、长宽比、精度与迭代数。
- **round_added**：3

## arXiv:2602.03566 — Riemannian Neural Optimal Transport

- **Year / status**：2026，arXiv preprint
- **URL**：https://arxiv.org/abs/2602.03566
- **Variant**：Riemannian optimal transport
- **Summary**：以连续神经 prepotential 和 intrinsic `c`-transform 学习紧致黎曼流形上的 amortized、非熵 OT map，并说明离散样本 map 近似会遭遇维数灾难。
- **Claims**：在正则性条件下给出维数友好的连续近似分析，并支持 out-of-sample map evaluation。
- **Limitations**：依赖紧致流形和较强正则性；内层 `c`-transform 优化昂贵；不是一般流形上的黑盒精确求解器。
- **round_added**：3

## arXiv:2605.04255 — Entropic Riemannian Neural Optimal Transport

- **Year / status**：2026，arXiv preprint
- **URL**：https://arxiv.org/abs/2605.04255
- **Variant**：Riemannian entropic OT / Schrödinger problem
- **Summary**：学习 intrinsic Schrödinger potential，以 Gibbs coupling 表示流形上的 entropic OT，并在 Cartan–Hadamard 流形上通过 barycentric projection 提取 map，在更一般情形使用 heat-smoothed surrogate。
- **Claims**：避免离散流形 Sinkhorn 的显式二次耦合存储，并在球面、旋转群、SPD、刚体群和双曲空间上实验。
- **Limitations**：固定正温度对应 coupling 而非无正则精确 map；投影依赖几何条件；SE(3) docking 实验只处理刚体位姿细化。
- **round_added**：3

## arXiv:2505.13660 — Sobolev Gradient Ascent for Optimal Transport

- **Year / status**：2025/2026，ICLR 2026
- **URL**：https://arxiv.org/abs/2505.13660
- **Variant**：Exact Wasserstein barycenter
- **Summary**：在规则网格上优化无约束 concave dual，以负 Laplacian 的逆构造齐次 Sobolev 梯度，从而计算无熵偏差的 barycenter，并避免显式 `c`-concavity 投影。
- **Claims**：每轮复杂度 `O(mn log n)`；给出次线性收敛率；二维、三维实验优于若干 exact baselines。
- **Limitations**：规则网格导致高维 curse；实现重点是 2D/3D；“exact”指目标无熵正则，并非有限步得到解析精确解。
- **round_added**：3

## arXiv:2605.11270 — A Unified Approach for Computing Wasserstein Barycenters

- **Year / status**：2026，arXiv preprint
- **URL**：https://arxiv.org/abs/2605.11270
- **Variant**：Exact discrete/continuous Wasserstein barycenter
- **Summary**：以 Fisher–Rao 几何上的 primal mirror descent 统一离散、连续和混合输入；每轮调用 semi-discrete OT 子问题，并保持连续 barycenter iterate。
- **Claims**：给出 `O(log T / sqrt(T))` 型收敛率，可在同一框架处理 heterogeneous measures。
- **Limitations**：目前数值实现集中在 2D/3D；semi-discrete 子问题仍可能是主要瓶颈；正式同行评审状态待定。
- **round_added**：3

## arXiv:2509.22494 — A dynamical formulation of multi-marginal optimal transport（精读更新）

- **Year / status**：2025，arXiv preprint
- **URL**：https://arxiv.org/abs/2509.22494
- **Variant**：Dynamical multi-marginal OT
- **Summary**：对半凸 multi-marginal cost，在乘积空间建立只约束端点边缘的 coupling flow；通过动量变量给出凸动态表述，连接 quasi-Monge 结构，并提出 proximal splitting 数值方案。
- **Claims**：把 Benamou–Brenier 的动态思路推广到一类非 pairwise 的 MMOT cost；提供一维 proof-of-concept 和公开代码。
- **Limitations**：当前数值主要是一维示例；离散密度可能出现轻微负值；高维扩展与复杂度优势尚未验证。
- **round_added**：3（替代 Round 2 的摘要级定位）
