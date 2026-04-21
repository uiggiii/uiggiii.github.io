import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import h, c, k


file = r'C:\Users\Lenovo\Documents\GitHub\uiggiii.github.io\compute_physics\cmb-data.txt'
data = np.loadtxt(file)
nu_data = data[:, 0]
I_data = data[:, 1]

# 统一单位
h = h * 1e7 
c = c * 100 
k = k * 1e7 

def intensity(nu, T):
    numerator = 2 * h * (nu**3) * (c**2)
    denominator = np.exp((h * c * nu) / (k * T)) - 1
    return numerator / denominator

# 设定初始猜测温度为2.7K
popt, pcov = curve_fit(intensity, nu_data, I_data, p0=[2.7])
T_fit = popt[0]

print(f"拟合得到的温度为: {T_fit:.4f} K")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制拟合曲线
plt.scatter(nu_data, I_data, label='观测数据', color='black', s=15)
nu_fit_range = np.linspace(min(nu_data), max(nu_data), 200)
plt.plot(nu_fit_range, intensity(nu_fit_range, T_fit), label=f'拟合曲线 (T={T_fit:.4f}K)', color='red')

plt.xlabel('波数 ($cm^{-1}$)')
plt.ylabel('辐射强度 ($erg \cdot s^{-1} \cdot cm^{-1} \cdot sr^{-1}$)')
plt.title('宇宙微波背景辐射')
plt.legend()
plt.grid(True)
plt.show()