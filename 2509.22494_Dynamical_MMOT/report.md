# 中文阅读报告：A Dynamical Formulation of MMOT

## 1. 与 Benamou–Brenier 的差别

Benamou–Brenier 固定 source/target marginals，让单个分布流从 \(\mu_0\) 走到 \(\mu_1\)。本文让一个定义在 product space 上的 coupling flow 从 source coupling \(p\) 出发；终点 coupling 不预先固定，只要求其各个 marginals 等于 \(\mu_1,\ldots,\mu_K\)。

## 2. 核心表述

对合适的 convex/semi-convex cost \(L\)，求

\[
\min_{\pi,v}\int_0^1\int L(v(t,x))\,d\pi_t(x)\,dt
\]

满足 product space 上的 continuity equation、初始 coupling 与终点 marginal constraints。

用 momentum \(m=\pi v\) 和 perspective function 可把目标与约束写成 convex optimization。

## 3. 理论意义

- 覆盖一般（半）凸 multi-marginal cost；
- 即使二边情形，也覆盖一部分经典 Benamou–Brenier translation-invariant cost 之外的问题；
- translation-invariant 情形可从动态最优解得到 static MMOT 的 quasi-Monge solution；
- 解释了 dynamic flow 与 joint coupling 结构的关系。

## 4. 数值

作者离散时间/空间并使用 primal–dual proximal splitting。在 \(d=1,K=3\) 的 quadratic cost 上，与解析 monotone maps 比较。

当前实验属于 proof-of-concept：

- \(N_t=N_x=10\)；
- 数千次迭代；
- 作者观察到离散 \(\pi\) 可能出现负值，细化 temporal grid 可缓解；
- 通用高维/多边缘可扩展性尚未展示。

## 5. 与 Multi_OT_book 的关系

Multi_OT Ch.6 从 generalized incompressible flow、Euler/Arnold/Brenier 原理得到多时间边缘问题。本文扩大了可处理 cost 的范围，并强调 convex dynamic formulation 与 quasi-Monge recovery。

## 6. 开放问题

- 保持 positivity 的稳定离散化；
- 高维 product space 的降维/结构化 solver；
- 与 entropic regularization、SB 的系统比较；
- 从低正则 dynamic coupling 稳定抽取 map；
- graph/Markov structure 下的 message passing。

