import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

L = 1e-8
x0 = L / 2
sigma = 1e-10
k = 5e10
hbar = 1.0546e-34
me = 9.109e-31
ht = 1e-18
N = 1000
hx = L / N

x = np.linspace(0, L, N + 1)
psi0 = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k * x)
psi0[0] = 0
psi0[-1] = 0

# 初始波函数归一化
norm_factor = np.sqrt(np.sum(np.abs(psi0)**2) * hx)
psi = psi0 / norm_factor

# 构造稀疏矩阵
alpha = hbar / (2 * me)
r = 1j * alpha * ht / (2 * hx**2)

diag_main_A = (1 + 2 * r) * np.ones(N - 1)
diag_off_A = -r * np.ones(N - 2)
matrix_A = diags([diag_off_A, diag_main_A, diag_off_A], [-1, 0, 1], format='csc')

diag_main_B = (1 - 2 * r) * np.ones(N - 1)
diag_off_B = r * np.ones(N - 2)
matrix_B = diags([diag_off_B, diag_main_B, diag_off_B], [-1, 0, 1], format='csc')

target_steps = [0, 300, 500, 800, 2000]
results = {}

psi_inner = psi[1:-1]
step = 0

while step <= max(target_steps):
    if step in target_steps:
        full_psi = np.zeros(N + 1, dtype=complex)
        full_psi[1:-1] = psi_inner
        results[step] = full_psi.copy()
        
    # 求解线性方程组演化到下一步
    right_side = matrix_B.dot(psi_inner)
    psi_inner = spsolve(matrix_A, right_side)
    step += 1

# 绘制波函数实部、虚部及模平方图像
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

for step in target_steps:
    axes[0].plot(x, np.real(results[step]), label=f'时间步={step}')
    axes[1].plot(x, np.imag(results[step]))
    axes[2].plot(x, np.abs(results[step])**2)

axes[0].set_ylabel('实部')
axes[1].set_ylabel('虚部')
axes[2].set_ylabel('模平方')
axes[2].set_xlabel('坐标')
axes[0].legend(loc='upper right')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.tight_layout()
plt.show()