# 中文阅读报告：Sobolev Gradient Ascent for Wasserstein Barycenter

## 1. 定位

- ICLR 2026 正式论文；
- 目标是规则网格上的 exact、unregularized Wasserstein barycenter；
- 不是 entropic barycenter 或 Sinkhorn divergence barycenter。

## 2. 核心方法

论文构造 constraint-free concave dual，只保留 \(m-1\) 个独立 potentials。Sobolev first variation 通过 inverse Laplacian 预条件：

\[
\nabla_{\dot H^1}D
=(-\Delta)^{-1}\delta D.
\]

这使算法不需要既有 dual 方法中每轮昂贵的 \(c\)-concavity projection。规则网格上：

- fast \(c\)-transform；
- FFT Poisson solve；
- 每轮约 \(O(mn\log n)\)。

## 3. 理论

论文证明 strong duality 与 barycenter characterization，并给出：

- 固定总迭代数/constant step：\(O(T^{-1/2})\)；
- annealed step：\(O(\log T/\sqrt T)\)。

这些 rate 是 dual objective gap 的全局保证，不能直接解读成所有 map/density norm 都同速收敛。

## 4. 实验

比较 debiased Sinkhorn barycenter、convolutional barycenter 和 WDHA。在 2D/3D synthetic、MNIST 等规则网格问题中，SGA 展示较高的 exact-barycenter 精度和较好效率。

## 5. 局限

- grid size 随 domain dimension 指数增长；
- 主要适合 2D/3D compact domain；
- 非均匀 grid 需要替换 fast \(c\)-transform、FFT Poisson 与 pushforward 计算；
- convergence proof 仍需要 potentials 连续与相应 Sobolev 范数有界等条件。

## 6. 与 OT_book 的关系

它延伸了 OT_book Ch.9 的 barycenter 与 Wasserstein variational problem：不再以 entropic Bregman projection 为默认，而是利用对偶的 Sobolev geometry 直接追求原始 barycenter。

