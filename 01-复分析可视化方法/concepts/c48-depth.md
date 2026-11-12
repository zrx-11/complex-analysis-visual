# 深度推导：Blasius 公式从哪里来

前置清单：

1. **伯努利方程**：$p+\frac12\rho|V|^2=$ 常数。
2. **复势**：$\Omega'=\bar V=u-iv$。
3. **边界受力**：$dF=-p\,n\,ds$，$n\,ds=(dy,-dx)$。
4. **留数**：$\oint z^{-1}dz=2\pi i$。

## 第 0 步：要证什么

$$F_x-iF_y=\frac{i\rho}{2}\oint_\Gamma(\Omega')^2\,dz.$$

## 第 1 步：压力与速度

伯努利：$p=p_0-\frac12\rho|V|^2$。常数 $p_0$ 沿闭合边界积分的合力为零（均匀压力不产生净力），所以只算 $-\frac12\rho|V|^2$ 的贡献。

## 第 2 步：合力的复数写法

边界小段 $ds$，外法向 $n\,ds=(dy,-dx)$。压力指向内部，所以

$$dF=-p\,n\,ds=-p\,(dy,-dx).$$

分量：

$$dF_x=-p\,dy,\qquad dF_y=p\,dx.$$

于是

$$F_x-iF_y=-\oint p\,dy-i\oint p\,dx=-\oint p\,(dy+i\,dx).$$

注意 $dy+i\,dx=i(dx-i\,dy)=i\,\overline{dz}$。所以

$$F_x-iF_y=-i\oint p\,\overline{dz}.$$

## 第 3 步：用速度表示压力

代入 $p=p_0-\frac12\rho|V|^2$：

$$F_x-iF_y=-i\oint\left(p_0-\frac12\rho|V|^2\right)\overline{dz}.$$

$p_0$ 项是常数乘 $\oint\overline{dz}=0$（闭曲线），消失。剩下

$$F_x-iF_y=\frac{i\rho}{2}\oint|V|^2\overline{dz}.$$

## 第 4 步：把 |V|² 写成 Ω'

在边界（流线）上，$\Omega'=\bar V=u-iv$，且 $|V|^2=\Omega'\overline{\Omega'}$。对无旋不可压流，沿流线有 $\overline{\Omega'}\,dz=\Omega'\,\overline{dz}$（因为速度与边界相切，$V\,dz$ 为实数；等价地 $|V|^2\overline{dz}=\Omega'^2 dz$）。代入：

$$F_x-iF_y=\frac{i\rho}{2}\oint_\Gamma(\Omega')^2\,dz.$$

这就是 Blasius 公式。

## 第 5 步：力矩

对力矩 $M=\oint (x\,dF_y-y\,dF_x)$，同样整理得

$$M=\operatorname{Re}\left[-\frac{\rho}{2}\oint_\Gamma z(\Omega')^2\,dz\right].$$

推导与力类似，多一个 $z$ 因子。

## 数值算例：绕圆柱的升力

圆柱半径 $a$，来流 $U$，环量 $\Gamma$。复势

$$\Omega=U\left(z+\frac{a^2}{z}\right)+\frac{i\Gamma}{2\pi}\log z.$$

求导：

$$\Omega'=U\left(1-\frac{a^2}{z^2}\right)+\frac{i\Gamma}{2\pi z}.$$

平方后，$1/z$ 的系数（留数）来自 $U\cdot\frac{i\Gamma}{2\pi z}$ 的交叉项两倍：

$$\operatorname{Res}=\frac{iU\Gamma}{\pi}.$$

于是

$$F_x-iF_y=\frac{i\rho}{2}\cdot2\pi i\cdot\frac{iU\Gamma}{\pi}
=\frac{i\rho}{2}\cdot(-2U\Gamma)=-i\rho U\Gamma.$$

所以 $F_x=0$，$F_y=\rho U\Gamma$。升力 $L=\rho U\Gamma$，阻力为零。这就是库塔–儒可夫斯基定理。

## 反例：无环量时无升力

$\Gamma=0$，则留数为 0，$F=0$。对称圆柱在理想流中不受力（达朗贝尔佯谬）。真实流体有粘性，会有阻力；升力需要环量（攻角或旋转）。

## 与后面章节的连接

- 第 12 章：机翼用儒可夫斯基映射 + Blasius 算升力。
- 第 11 章：留数是这里唯一的计算工具。
- 第 10 章：压力与速度平方的关系来自伯努利。

## 差生通读自查

- 伯努利、复势、边界受力、留数四个前置都给了白话；$p,n,ds$ 第一次出现都解释。
- 从 $dF$ 到复数形式，$dy+i\,dx=i\overline{dz}$ 单独验证；$p_0$ 项消失单独说明。
- 给了"为什么这样设计"：把压力写成速度平方，是为了让复势的导数进入积分，从而能用留数。
- 算例完整算出圆柱升力；反例说明无环量无升力。
