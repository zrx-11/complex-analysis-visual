# 深度推导：柯西–黎曼方程从哪来、管什么

前置清单：

1. **偏导数**：固定 $y$ 对 $x$ 求导记 $u_x$；固定 $x$ 对 $y$ 求导记 $u_y$。
2. **差商**：$f'(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h}$，$h$ 是复数，可从任意方向趋于 0。
3. **除以复数**：$\frac{1}{i}=-i$，所以除以 $i$ 等于乘 $-i$。
4. **二元泰勒一阶展开**：$\Delta u\approx u_x\Delta x+u_y\Delta y$。

## 第 0 步：要证什么

1. 若 $f=u+iv$ 在 $z_0$ 复可导，则 $u_x=v_y$、$u_y=-v_x$。
2. 反过来，若 $u,v$ 的偏导连续且满足这两条，则 $f$ 复可导，且 $f'=u_x+iv_x$。
3. 这两条等价于"局部效果是一个乘子（伸扭）"。

## 第 1 步：沿水平方向取差商

取 $h=t$ 为实数：

$$\frac{f(z_0+t)-f(z_0)}{t}=\frac{[u(x+t,y)-u(x,y)]+i[v(x+t,y)-v(x,y)]}{t}.$$

$t\to0$ 时，两个差商分别趋向 $u_x$ 与 $v_x$：

$$A_{\text{水平}}=u_x+iv_x.$$

这一步只用偏导数的定义。

## 第 2 步：沿竖直方向取差商

取 $h=it$：

$$\frac{f(z_0+it)-f(z_0)}{it}=\frac{\Delta u+i\Delta v}{it}.$$

分母是 $it$，除以它等于乘 $\frac{1}{i}\frac{1}{t}=-i\frac1t$。于是

$$A_{\text{竖直}}=-i(u_y+iv_y)=v_y-iu_y.$$

最后一步展开：$-i(u_y+iv_y)=-iu_y+v_y$，实部 $v_y$、虚部 $-u_y$。

## 第 3 步：两个方向必须给同一个复数

复导数要求 $h$ 沿**任何**方向趋于 0 时差商都趋向同一个 $A$。水平、竖直只是其中两条路，所以

$$u_x+iv_x=v_y-iu_y.$$

比较实部、虚部：

$$u_x=v_y,\qquad v_x=-u_y.$$

这就是 CR。注意第二个式子常写成 $u_y=-v_x$，是同一个等式。

## 第 4 步：CR 的几何内容

把 $f$ 看成 $(x,y)\mapsto(u,v)$，它的雅可比矩阵是

$$J=\begin{pmatrix}u_x&u_y\\v_x&v_y\end{pmatrix}.$$

CR 代入后：

$$J=\begin{pmatrix}a&-b\\b&a\end{pmatrix},\qquad a=u_x,\ b=v_x.$$

这种矩阵正好是"乘以复数 $a+ib$"的矩阵：它把向量 $(t,s)$ 变成 $(at-bs,\ bt+as)$，即长度乘 $\sqrt{a^2+b^2}$、角度加 $\arctan(b/a)$。所以 CR 的几何意思就是"雅可比是旋转加伸缩，没有剪切"。

反过来，若 $J$ 是这种形状，则 $u_x=v_y$、$u_y=-v_x$，即 CR。两条路在这里合流：**CR ⇔ 局部伸扭 ⇔ 保角**。

## 第 5 步：CR 推出调和性

对 CR 再求一次导：

$$u_{xx}=(v_y)_x=v_{yx},\qquad u_{yy}=(-v_x)_y=-v_{xy}.$$

偏导连续时 $v_{yx}=v_{xy}$，所以

$$u_{xx}+u_{yy}=0.$$

同理 $v_{xx}+v_{yy}=0$。即 $u,v$ 都是**调和函数**（拉普拉斯方程 $\Delta u=0$）。第 12 章讲流体与调和函数时，这条是出发点：解析函数的实部、虚部都是调和函数，且互为共轭调和函数。

## 第 6 步：极坐标形式

设 $z=re^{i\theta}$，$f=u+iv$。CR 在极坐标下写成

$$u_r=\frac1r v_\theta,\qquad v_r=-\frac1r u_\theta.$$

导数公式是

$$f'(z)=e^{-i\theta}(u_r+iv_r).$$

**例子**：$f(z)=z^2=r^2e^{2i\theta}$，$u=r^2\cos2\theta$，$v=r^2\sin2\theta$。$u_r=2r\cos2\theta$，$\frac1r v_\theta=\frac1r(-2r^2\sin2\theta)=-2r\sin2\theta$——等等，这两条不相等，说明我写反了符号。正确的极坐标 CR 是 $u_r=\frac1r v_\theta$？代 $z^2$：$v_\theta=2r^2\cos2\theta$，$\frac1r v_\theta=2r\cos2\theta=u_r$，对上了。刚才把 $v$ 的 $\theta$ 导数算错成 $-2r^2\sin2\theta$，实际 $v=r^2\sin2\theta$ 对 $\theta$ 求导是 $2r^2\cos2\theta$。修正后 CR 成立。$f'=e^{-i\theta}(2r\cos2\theta+i2r\sin2\theta)=2re^{i\theta}=2z$，与幂法则一致。

## 数值算例一：$f=z^2$ 在 $z=1+i$

$u=x^2-y^2$，$v=2xy$。在 $(1,1)$：$u_x=2$、$v_y=2$、$u_y=-2$、$v_x=2$。CR 两条都成立。$f'=u_x+iv_x=2+2i=2z$，对。

## 数值算例二：$f=e^z$ 在 $z=0$

$u=e^x\cos y$，$v=e^x\sin y$。在 $(0,0)$：$u_x=1$、$v_y=1$、$u_y=0$、$v_x=0$。CR 成立，$f'=1$。在任意点：$u_x=e^x\cos y=v_y$，$u_y=-e^x\sin y=-v_x$，$f'=e^x\cos y+ie^x\sin y=e^z$。

## 反例：$\bar z$ 两个方向不一致

$f=\bar z=x-iy$，$u=x$、$v=-y$。水平差商 $1$，竖直差商 $-1$，不相等；CR 给 $u_x=1$、$v_y=-1$，第一条就破了。几何上 $\bar z$ 是反射，把方向反过来，不是"旋转 + 伸缩"，所以不解析。

## 与后面章节的连接

- 第 5 章：$f'$ 的极坐标公式用来"可视微分"$\log z$、$z^n$、$e^z$。
- 第 9 章：柯西定理的证明用 CR 把围道积分化成面积分（格林公式）。
- 第 12 章：$u,v$ 调和、互为共轭，是流体势函数与流函数的关系。

## 差生通读自查

- 偏导、差商、除以 $i$ 三条前置都给了白话；$u_x,v_y$ 第一次出现说明了含义。
- 水平、竖直两个差商的每一步都写出来了，包括除以 $i$ 等于乘 $-i$。
- 给了"为什么这样设计"：CR 不是计算口诀，而是"雅可比必须是旋转伸缩矩阵"的代数翻译。
- 极坐标例子中途发现自己算错并当场修正，保留了检查过程；两个数值算例都能手算。
