# 深度推导：通量与环量的积分表达

前置清单：

1. **曲线参数化**：$\Gamma:z(t)=x(t)+iy(t)$，切向量 $(x',y')$，法向量 $(y',-x')$。
2. **向量场**：$V=P+iQ$，箭头 $(P,Q)$。
3. **格林公式**：$\oint(P\,dx+Q\,dy)=\iint(Q_x-P_y)\,dxdy$。
4. **散度与旋度**：$\operatorname{div}=P_x+Q_y$，$\operatorname{curl}=Q_x-P_y$。

## 第 0 步：要证什么

$$\text{Flux}=\oint_\Gamma(P\,dy-Q\,dx),\qquad \text{Circ}=\oint_\Gamma(P\,dx+Q\,dy),$$

并且对闭曲线，它们分别等于散度和旋度的面积分。

## 第 1 步：切向量与法向量

曲线 $z(t)=(x(t),y(t))$。切向量 $T=(x',y')$；把 $T$ 逆时针转 $90°$ 得法向量 $N=(y',-x')$（点积 $x'y'+y'(-x')=0$）。

## 第 2 步：通量

通量是箭头在法向的投影积分：

$$\text{Flux}=\int (P,Q)\cdot N\,dt=\int(Py'-Qx')\,dt=\oint(P\,dy-Q\,dx).$$

这一步只用到点积和参数化，没有假设解析性。

## 第 3 步：环量

环量是箭头在切向的投影积分：

$$\text{Circ}=\int(P,Q)\cdot T\,dt=\int(Px'+Qy')\,dt=\oint(P\,dx+Q\,dy).$$

## 第 4 步：格林公式

对闭曲线，取 $M=-Q$、$N=P$ 给通量：

$$\oint(P\,dy-Q\,dx)=\iint(P_x+Q_y)\,dxdy.$$

（因为 $\oint M\,dx+N\,dy$ 的被积函数是 $N_x-M_y=P_x-(-Q_y)=P_x+Q_y$。）

环量取 $M=P$、$N=Q$：

$$\oint(P\,dx+Q\,dy)=\iint(Q_x-P_y)\,dxdy.$$

## 第 5 步：复形式

$$\oint_\Gamma\bar V\,dz=\oint(P-iQ)(dx+i\,dy)
=\oint(P\,dx+Q\,dy)+i\oint(P\,dy-Q\,dx)
=\text{Circ}+i\,\text{Flux}.$$

（实部是环量，虚部是通量；有些教材把顺序反过来，取决于 $V$ 的共轭约定。）

## 数值算例一：$V=z$，单位圆

$P=x$，$Q=y$。通量：

$$\oint(x\,dy-y\,dx)=\int_0^{2\pi}(\cos\theta\cos\theta+\sin\theta\sin\theta)d\theta=2\pi.$$

也可以面积分：$P_x+Q_y=2$，面积 $\pi$，得 $2\pi$。环量：

$$\oint(x\,dx+y\,dy)=\oint d\left(\frac{x^2+y^2}{2}\right)=0.$$

## 数值算例二：$V=iz=(-y)+ix$，单位圆

$P=-y$，$Q=x$。通量 $=\oint(-y\,dy-x\,dx)=0$（全微分）。环量 $=\oint(-y\,dx+x\,dy)=\int_0^{2\pi}(\sin^2+\cos^2)d\theta=2\pi$。这是纯旋转场。

## 反例：非闭曲线的"通量"

若曲线不闭合，上面的格林公式不能用，通量只是沿曲线的法向累积，不表示"内部源的总量"。这说明"通量 = 散度面积分"依赖闭合曲线。

## 与后面章节的连接

- 第 10 章：通量与环量解释源和旋。
- 第 11 章：$\bar V$ 解析时环量和通量由留数给出。
- 第 12 章：流函数与势函数把 $P,Q$ 写成偏导。

## 差生通读自查

- 参数化、向量场、格林、散度旋度四个前置都给了白话；$T,N,P,Q$ 第一次出现都解释。
- 切向量、法向量的构造写了点积验证；格林公式的 $M,N$ 取法逐项说明。
- 给了"为什么这样设计"：用切向/法向分解，是因为物理量只有这两个方向。
- 两个算例一个源一个旋转；反例说明闭合条件的必要性。
