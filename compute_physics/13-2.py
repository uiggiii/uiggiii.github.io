import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def epidemic_model(state, t, k, l):
    x, y, z = state
    dx_dt = -k * x * y
    dy_dt = k * x * y - l * y
    dz_dt = l * y
    return [dx_dt, dy_dt, dz_dt]

def solve_and_plot():
    x0 = 10**6
    y0 = 1
    z0 = 0
    initial_state = [x0, y0, z0]

    t = np.linspace(0, 300, 2000)

    # 设置死亡比率系数
    l = 0.01
    # 选取三个不同的传播系数
    k_values = [1e-8, 3e-8, 5e-8]
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for i, k in enumerate(k_values):
        result = odeint(epidemic_model, initial_state, t, args=(k, l))
        x, y, z = result.T

        ax = axes[i]
        ax.plot(t, x, label='健康人数')
        ax.plot(t, y, label='生病人数')
        ax.plot(t, z, label='死亡人数')
        ax.set_title(f'传播系数 k = {k}')
        ax.set_xlabel('时间')
        ax.set_ylabel('人数')
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

solve_and_plot()