import numpy as np
import matplotlib.pyplot as plt

omega = 1.0
t_start = 0.0
t_end = 100.0
dt = 0.05
t = np.arange(t_start, t_end, dt)
k_a = 0.1
y_a = np.zeros((len(t), 2))
y_a[0] = [1.0, 0.0]

def rk4_step(func, y, t_val, dt_val, k_damp):
    k1 = func(t_val, y, k_damp)
    k2 = func(t_val + 0.5 * dt_val, y + 0.5 * dt_val * k1, k_damp)
    k3 = func(t_val + 0.5 * dt_val, y + 0.5 * dt_val * k2, k_damp)
    k4 = func(t_val + dt_val, y + dt_val * k3, k_damp)
    return y + (dt_val / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

# 受阻尼谐振子的导数函数，y[0] 是位移, y[1] 是速度
def oscillator_deriv(t_val, y, k_damp):
    dy0 = y[1]
    dy1 = -omega**2 * y[0] - k_damp * y[1]
    return np.array([dy0, dy1])

# (a) 计算阻尼系数为 0.1 的情况
for i in range(len(t) - 1):
    y_a[i+1] = rk4_step(oscillator_deriv, y_a[i], t[i], dt, k_a)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, y_a[:, 0], label=f"k={k_a}")
plt.title("四阶龙格-库塔求解受阻尼谐振子")
plt.xlabel("时间")
plt.ylabel("位移")
plt.grid(True)
plt.legend()


# (b) 测试不同的阻尼系数值，寻找无振荡效应的临界点
k_values = [0.5, 1.0, 1.5, 2.0, 3.0]
plt.subplot(1, 2, 2)

for kv in k_values:
    y_b = np.zeros((len(t), 2))
    y_b[0] = [1.0, 0.0]
    for i in range(len(t) - 1):
        y_b[i+1] = rk4_step(oscillator_deriv, y_b[i], t[i], dt, kv)
    plt.plot(t, y_b[:, 0], label=f"k={kv}")

plt.title("不同阻尼系数对比 (k>=2.0时振荡消失)")
plt.xlabel("时间")
plt.ylabel("位移")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()