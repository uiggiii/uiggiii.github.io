import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar

# 定义拉格朗日插值函数
def lagrange(x_data, y_data, x_target):
    result_list = []
    n = len(x_data)
    for x in x_target:
        total_sum = 0
        for i in range(n):
            term = y_data[i]
            for j in range(n):
                if i != j:
                    term *= (x - x_data[j]) / (x_data[i] - x_data[j])
            total_sum += term
        result_list.append(total_sum)
    return np.array(result_list)

r_data = np.array([0.90, 1.05, 1.20, 1.35, 1.50, 1.65, 1.80, 2.00, 2.30])
v_data = np.array([1.84, 0.43, -0.64, -1.28, -1.50, -1.36, -1.04, -0.64, -0.28])

# 三次样条插值
cs_spline = CubicSpline(r_data, v_data)

# 寻找平衡位置
res = minimize_scalar(cs_spline, bounds=(r_data.min(), r_data.max()), method='bounded')
re = res.x
ve = res.fun

# 计算有效弹性系数
k_val = cs_spline.derivative(nu=2)(re)

print("-" * 30)
print(f"计算结果报告：")
print(f"平衡位置 : {re:.4f} A")
print(f"势阱最低能量 : {ve:.4f} eV")
print(f"有效弹性系数 : {k_val:.4f} eV/A^2")
print("-" * 30)

r_fine = np.linspace(r_data.min(), r_data.max(), 500)

v_lag_manual = lagrange(r_data, v_data, r_fine)
v_spl = cs_spline(r_fine)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 7))
plt.scatter(r_data, v_data, color='red', zorder=5, label='原始数据点')
plt.plot(r_fine, v_lag_manual, '--', color='gray', alpha=0.7, label='拉格朗日插值')
plt.plot(r_fine, v_spl, '-', color='blue', linewidth=2, label='三次样条插值')
plt.plot(re, ve, 'go', zorder=6, label=f'平衡位置 (re={re:.2f})')
plt.title('双原子分子势能曲线') 
plt.xlabel('核间距 r / A')
plt.ylabel('势能 V(r) / eV')
plt.ylim(-2, 2.5)
plt.axhline(0, color='black', linewidth=0.5, linestyle=':')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

'''
计算结果报告：
平衡位置 : 1.5080 A
势阱最低能量 : -1.5005 eV
有效弹性系数 : 16.8148 eV/A^2
'''