import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import quad
import matplotlib.pyplot as plt

C1 = 1.0
C2 = 1.44e4 

def wien_model(T, b):
    return b / T

def blackbody_spectrum(lam, T):
    with np.errstate(divide='ignore', over='ignore'):
        return (C1 / lam**5) / (np.exp(C2 / (lam * T)) - 1)

# ---(a)维恩位移定律的数值验证---
temperatures = np.linspace(2000, 6000, 41) 
lambda_max_list = []

for T in temperatures:
    lams = np.linspace(0.1, 5.0, 10000) 
    intensity = blackbody_spectrum(lams, T)
    max_idx = np.argmax(intensity)
    lambda_max_list.append(lams[max_idx])


# 使用 curve_fit 拟合
popt, pcov = curve_fit(wien_model, temperatures, lambda_max_list)
b_fit = popt[0]

print(f"(a) 拟合得到的维恩常数 b ≈ {b_fit:.4f} μm·K")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(8, 5))
plt.scatter(temperatures, lambda_max_list, label='极大值', color='black', s=15)
plt.plot(temperatures, wien_model(temperatures, b_fit), 'r-', label=f'拟合曲线: $\lambda_{{max}} = {b_fit:.2f}/T$')
plt.xlabel('T(K)')
plt.ylabel('峰值波长 $\lambda_{max}$ ($\mu m$)')
plt.title('韦恩位移定律验证')
plt.legend()
plt.grid(True)

# ---(b)数值积分计算可见光波段强度---
T_target = 5000 
lambda_start = 0.3
lambda_end = 0.8  
intensity_visible, error = quad(blackbody_spectrum, lambda_start, lambda_end, args=(T_target,))

print(f"(b) 当 T = {T_target}K 时：")
print(f"    可见光波段 (0.3 - 0.8 μm) 的总辐射强度为: {intensity_visible:.6e}")
print(f"    积分估计误差为: {error:.6e}")

plt.show()

'''
输出结果：
(a) 拟合得到的维恩常数 b ≈ 2900.1985 μm·K
(b) 当 T = 5000K 时：
    可见光波段 (0.3 - 0.8 μm) 的总辐射强度为: 4.412600e-02
    积分估计误差为: 3.042397e-14
'''