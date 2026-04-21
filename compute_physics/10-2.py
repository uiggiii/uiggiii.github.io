import numpy as np

dim = 10
N = 10**7

# 在超立方体内生成均匀分布的随机点
points = np.random.uniform(-1, 1, (N, dim))
r_squared = np.sum(points**2, axis=1)

# 统计落在超球体内部的点数（即满足 x_1^2 + ... + x_10^2 < 1）
inside_count = np.sum(r_squared < 1)

p = inside_count / N
V_box = 2**dim
V_mc = V_box * p        #超球体的体积估计值

# 误差评估
error = V_box * np.sqrt(p * (1 - p) / N)
V_theory = (np.pi**5) / 120

print(f"计算得到的单位超球体体积: {V_mc:.6f}")
print(f"计算结果的评估误差: +/- {error:.6f}")
print(f"理论精确体积: {V_theory:.6f}")
print(f"实际偏差: {abs(V_mc - V_theory):.6f}")