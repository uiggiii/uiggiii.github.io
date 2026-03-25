import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t_data = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
n_data = np.array([1036, 819, 640, 514, 397, 327, 257, 208, 165, 140, 117, 101])
sigma_n = np.sqrt(n_data)

# 定义带有三个未知参数的指数衰减模型
def decay_model(t, n0, lam, b):
    return n0 * np.exp(-lam * t) + b

initial_guess = [1000, 0.05, 50]
popt, pcov = curve_fit(decay_model, t_data, n_data, p0=initial_guess, sigma=sigma_n, absolute_sigma=True)
n0_fit, lam_fit, b_fit = popt

# 取协方差矩阵对角线元素并开根号，获得各参数的误差估计
perr = np.sqrt(np.diag(pcov))
n0_err, lam_err, b_err = perr

# 半衰期
t_half = np.log(2) / lam_fit
t_half_err = (np.log(2) / (lam_fit**2)) * lam_err

# 终端输出各项计算数值
print("参数拟合与误差估计结果：")
print(f"初始净计数 : {n0_fit:.2f} ± {n0_err:.2f}")
print(f"衰变常数 : {lam_fit:.4f} ± {lam_err:.4f}")
print(f"本底计数 : {b_fit:.2f} ± {b_err:.2f}")
print(f"半衰期 : {t_half:.2f} ± {t_half_err:.2f}")

# 生成密集时间数组用于绘制平滑模型曲线
t_fine = np.linspace(0, 110, 500)
n_fit_curve = decay_model(t_fine, n0_fit, lam_fit, b_fit)

# 绘制散点图与拟合曲线
plt.figure(figsize=(10, 6))
plt.errorbar(t_data, n_data, yerr=sigma_n, fmt='ro', label='带有误差的实验数据', capsize=4)
plt.plot(t_fine, n_fit_curve, 'b-', label='最小二乘拟合曲线')
plt.xlabel('时间 / 秒')
plt.ylabel('计数')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

'''
初始净计数 : 1003.28 ± 23.00
衰变常数 : 0.0252 ± 0.0015
本底计数 : 36.30 ± 15.79
半衰期 : 27.50 ± 1.65
'''