# 中文阅读报告：FRBary

## 1. 问题

现有 solver 往往分裂为：

- point-cloud/free-support；
- common regular grid；
- neural continuous density。

本文希望用同一算法处理 discrete、absolutely continuous 及混合输入，并保持 unregularized Wasserstein barycenter 目标。

## 2. 方法

FRBary 在概率密度的 Fisher–Rao geometry 下做 primal mirror descent。每轮：

1. 从当前连续 barycenter iterate 到每个输入求 semi-discrete 或 continuous OT；
2. 用得到的势/first variation 更新 density；
3. 维持非负与归一化。

即使输入全是 point clouds，iterates 仍是 absolutely continuous density，最终在目标意义下收敛到离散 barycenter。

## 3. 理论

在 compact convex domain 上，论文对连续、离散和混合输入给出 objective convergence，典型 rate 为

\[
O(\log T/\sqrt T).
\]

假设比一些对偶网格方法更弱，但每轮 semi-discrete OT 的实际复杂度仍取决于维度、支持数与实现。

## 4. 实验

包括：

- MNIST density + heart density + Swiss-roll point cloud 的异构输入；
- MNIST exact-barycenter 对比；
- 2D/3D Gaussian point clouds；
- RGB color-palette averaging。

实验展示了连续输出、异构输入和精度优势；不是对任意高维数据可扩展性的证明。

## 5. 局限

- 当前实现重点仍是 2D/3D；
- density discretization/parameterization 会影响实际性能；
- semi-discrete OT 与采样可能成为瓶颈；
- 神经密度版本需要训练与 Langevin sampling，增加新的近似层。

## 6. 与 SGA 的互补

- SGA：dual、Sobolev geometry、同一规则网格、FFT；
- FRBary：primal、Fisher–Rao geometry、异构离散/连续输入；
- 二者都追求 exact objective，但各自的可扩展边界不同。

