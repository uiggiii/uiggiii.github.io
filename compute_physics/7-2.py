import numpy as np
import matplotlib.pyplot as plt

x_max = 7.0
dx = 0.01
# 定义量子谐振子的导数函数，y[0] 对应波函数 u, y[1] 对应导数 du/dx
def qho_deriv(x_val, y, n_level):
    dy0 = y[1]
    dy1 = -(2 * n_level + 1 - x_val**2) * y[0]
    return np.array([dy0, dy1])

def rk4_step(func, y, x_val, dx_val, n_level):
    k1 = func(x_val, y, n_level)
    k2 = func(x_val + 0.5 * dx_val, y + 0.5 * dx_val * k1, n_level)
    k3 = func(x_val + 0.5 * dx_val, y + 0.5 * dx_val * k2, n_level)
    k4 = func(x_val + dx_val, y + dx_val * k3, n_level)
    return y + (dx_val / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

# 从原点向外积分
def solve_qho_symmetric(n_level):
    x_pos = np.arange(0, x_max + dx, dx)
    y_pos = np.zeros((len(x_pos), 2))
    if n_level % 2 == 0:
        y_pos[0] = [1.0, 0.0]
    else:
        y_pos[0] = [0.0, 1.0]
    for i in range(len(x_pos) - 1):
        y_pos[i+1] = rk4_step(qho_deriv, y_pos[i], x_pos[i], dx, n_level)
        
    u_pos = y_pos[:, 0]
    
    if n_level % 2 == 0:
        u_neg = u_pos[1:][::-1]
    else:
        u_neg = -u_pos[1:][::-1]
        
    x_neg = -x_pos[1:][::-1]
    
    x_full = np.concatenate((x_neg, x_pos))
    u_full = np.concatenate((u_neg, u_pos))
    
    return x_full, u_full

n_values = [1, 2, 5, 10, 15]

plt.figure(figsize=(15, 10))

for idx, n in enumerate(n_values):
    x_arr, u_arr = solve_qho_symmetric(n)

    prob_density = u_arr**2
    norm_factor = np.trapz(prob_density, x_arr)
    prob_density = prob_density / norm_factor
    classical_prob = np.zeros_like(x_arr)
    # 仅在经典允许区内计算
    valid_region = (2 * n + 1 - x_arr**2) > 0 
    classical_prob[valid_region] = 1.0 / np.sqrt(2 * n + 1 - x_arr[valid_region]**2)
    norm_classical = np.trapz(classical_prob[valid_region], x_arr[valid_region])
    classical_prob[valid_region] /= norm_classical

    plt.subplot(3, 2, idx + 1)
    plt.plot(x_arr, prob_density, label="量子概率密度")
    plt.plot(x_arr[valid_region], classical_prob[valid_region], 'r--', label="经典概率分布")
    plt.title(f"能级 n={n}")
    plt.xlabel("位置")
    plt.ylabel("概率密度")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()