# 中文阅读报告：Riemannian Neural Optimal Transport

## 1. 问题

离散 manifold OT 需要随 support size 构造离散 cost/map，难以 out-of-sample；直接把 Euclidean neural OT 搬到流形又不能保证 map 落在 manifold 或遵守 intrinsic geometry。

论文先给出负面结果：任何以离散方式近似 manifold OT map 的方法，为达到固定精度，参数数目会随 manifold dimension 指数增长。

## 2. 方法

RNOT 不离散 transport map，而是：

1. 用 neural network 参数化连续 prepotential；
2. 通过 intrinsic \(c\)-transform 强制 \(c\)-concavity；
3. 从势函数恢复 manifold-valued OT map；
4. 训练后对新 source point 直接评价。

对于非仿射 piecewise-linear activation，论文给出势函数与 map approximation 的网络规模/深度上界，并通过稳定性把 potential error 传到 map error。

## 3. 结果

实验覆盖 sphere、torus 与 continental-drift 案例。dimension sweep 中，离散/soft \(c\)-transform baseline 随维度退化，RNOT 相对稳定。论文附录扩展了更高维结果。

RNOT 的主要意义是提供一个 dimension-friendly 的连续参数化路线，而不是证明 manifold OT 已在任意高维上工程可解。

## 4. 局限

- 理论集中于 compact manifolds；
- approximation rate 依赖 regularity；
- 每次训练需要迭代 inner minimization 求 \(c\)-transform；
- 实验中训练时间明显高于部分 baseline；
- 对更广 cost、noncompact manifold 与 inner solve amortization 仍待研究。

## 5. 与 Entropic RNOT 的区别

- RNOT 目标是 non-entropic Monge map；
- Entropic RNOT 的自然输出是 Gibbs coupling；
- 前者 inner \(c\)-transform 较重，后者通过 semidual/minibatch 获得更平滑的训练；
- 后者若需要 point output，必须再做 barycentric projection 或 heat-smoothed mode。

