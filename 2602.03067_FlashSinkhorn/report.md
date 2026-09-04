# 中文阅读报告：FlashSinkhorn

## 1. 定位

- 论文：FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU
- 状态：ICML 2026 Oral；arXiv v3，2026-05-21
- 主题：entropic OT、GPU systems、Triton、implicit differentiation

这不是新 OT 距离，也不是更快收敛的 fixed-point method。它优化的是 stabilized log-domain Sinkhorn 在 GPU 上的 IO 路径。

## 2. 核心改写

平方欧氏代价满足

\[
-\|x_i-y_j\|^2
=2x_i^\top y_j-\|x_i\|^2-\|y_j\|^2.
\]

把行/列范数吸收到 shifted dual potentials 后，一个 Sinkhorn half-step 成为带 bias 的 row-wise LogSumExp。这与 attention 的 score normalization 同构，因此可以使用：

- SRAM tiling；
- online max/sum-exp；
- kernel fusion；
- 不物化 \(n\times m\) score/cost/plan。

## 3. 主要贡献

1. fused Triton kernel 执行 forward Sinkhorn updates；
2. streaming \(PV\)、\(P^\top V\) 支持 plan application；
3. analytic/implicit gradient，避免反传所有 Sinkhorn iterates；
4. streaming conjugate-gradient HVP；
5. OTDD 与 shuffled regression 等 downstream 评估。

内存由 dense \(O(nm)\) 降为 \(O((n+m)d)\)。算术量仍需遍历 pairwise interaction，约为每轮 \(O(nmd)\)。

## 4. 实验结论

作者在 A100-80GB 上报告：

- forward 最高 \(32\times\)；
- end-to-end 最高 \(161\times\)；
- 对大点云的 gradient/HVP 提升尤其明显；
- HVP 峰值内存随 \(n\) 近似线性。

附录表明加速依赖 regime：小 \(d\) 时 KeOps 可有竞争力；当 dense tensor 能放入显存且 \(d\) 很大时，tensorized backend 可能更快；极端 rectangular pair 的收益会下降。

## 5. 与 OT_book 的关系

数学原型就是 OT_book Ch.4：

\[
P_\varepsilon=\operatorname{diag}(u)K\operatorname{diag}(v).
\]

OT_book 关注 KL projection、收敛与稳定化；FlashSinkhorn 增加了 2026 年的 systems 视角：相同 FLOPs/相同 fixed point 可以因 HBM traffic、kernel launch 和 fusion 而有巨大速度差。

## 6. 局限

- 高层 API 主要支持 \(p=2\) squared Euclidean cost；
- 不直接覆盖一般 geodesic、learned cost、GW；
- 求的是 fixed \(\varepsilon>0\) EOT，不是 exact OT；
- 单轮更快不消除小 \(\varepsilon\) 导致的迭代数增加；
- speedup 不可脱离硬件、精度、backend 与 stopping rule 引用。

## 7. 复现检查

复现时必须同时比较固定迭代与相同 marginal tolerance，并报告：

- PyTorch/Triton/CUDA/GPU；
- fp32/TF32 等精度模式；
- JIT warm-up；
- forward、backward、HVP；
- 峰值显存、marginal residual 与 objective。

