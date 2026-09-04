# 中文阅读报告：Entropic Riemannian Neural Optimal Transport

## 1. 目标

离散 manifold Sinkhorn 可用 intrinsic cost，但每个新 support 都要形成 \(N^2\) cost matrix；neural OT 可 amortize，却通常面向 Euclidean map。本文要把二者合并。

## 2. 方法

作者在 manifold 上使用 entropic OT semidual：

- 只学习 target-side Schrödinger potential；
- 通过 intrinsic cost 恢复 Gibbs conditional law；
- minibatch 训练，不依赖全 support size；
- 对 Cartan–Hadamard manifold 使用 conditional Fréchet mean；
- 对 stochastically complete manifold 使用 heat-smoothed conditional surrogate。

固定 \(\varepsilon>0\) 下，论文证明 hypothesis class 可恢复 entropic coupling；在相应条件下给出 barycentric surrogate 的 \(L^2\) recovery，以及 heat smoothing 的稳定性和小 heat-time 偏差消失。

## 3. 实验

覆盖：

- \(\mathbb S^2\)；
- \(\mathrm{SO}(3)\)；
- \(\mathrm{SPD}(3)\)；
- \(\mathrm{SE}(3)\)；
- \(\mathbb H^2\)。

相对 discrete manifold Sinkhorn，训练内存/时间主要由 minibatch 决定，对大 support 更有利。论文还用一个共享模型做 protein–ligand pose ensemble 的 \(\mathrm{SE}(3)\) refinement。

## 4. 应怎样解释输出

正温度 EOT 的自然对象是 coupling：

\[
\pi_\varepsilon(y\mid x)
\propto \exp((g(y)-c(x,y))/\varepsilon)\,\beta(dy).
\]

Fréchet mean 或 heat-smoothed mode 是 conditional distribution 的点摘要。若 conditional 多峰，这个摘要会丢失不确定性；不能把它与真正的 Monge map 等同。

## 5. 局限

- 理论不覆盖 \(\varepsilon\to0\)；
- barycentric uniqueness 依赖非正曲率等条件；
- 需高效 geodesic distance 和稳定 LogSumExp；
- docking 只是已有 rigid poses 的 refinement，不含 torsion，也不是生成式 docking；
- 当前主要是预印本结果，仍需更多独立复现。

