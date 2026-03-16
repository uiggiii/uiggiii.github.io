import numpy as np
import matplotlib.pyplot as plt

#设置参数
wavelength = 300e-9
a = 3e-6
d = 9e-6
N = 4
I0 = 1.0

theta = np.linspace(-0.2, 0.2, 2000) + 1e-16    #防止分母为0

u = (np.pi * a * np.sin(theta)) / wavelength
v = (np.pi * d * np.sin(theta)) / wavelength

diffraction = (np.sin(u) / u)**2
interference = (np.sin(N * v) / np.sin(v))**2
I = I0 * diffraction * interference

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 5))
plt.plot(theta, I, color='blue', label='总光强')
plt.plot(theta, I0 * N**2 * diffraction, color='red', linestyle='--', label='包络线')
plt.title('多缝衍射光强分布')
plt.xlabel('衍射角')
plt.ylabel('光强')
plt.legend()
plt.grid(True)
plt.show()