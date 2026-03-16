import numpy as np
import matplotlib.pyplot as plt

#参数设置
alpha = 78.5/180 * np.pi    #以自转轴为y轴，alpha则为地磁偏移角
R_E = 6.37
B_0 = 3.12e-5

#创建坐标网格
x = np.linspace(-40,40,200)
y = np.linspace(-40,40,200)
X,Y = np.meshgrid(x,y)

#将极坐标参数正交化
R = np.sqrt(X**2 + Y**2)
theta = np.arctan2(Y,X)
U_r = -2 * B_0 * (R_E / R)**3 * np.cos(theta)
V_theta = -1 * B_0 * (R_E / R)**3 * np.sin(theta)
U = U_r * np.cos(theta + alpha) - V_theta * np.sin(theta + alpha)
V = U_r * np.sin(theta + alpha) - V_theta * np.cos(theta + alpha)

#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.streamplot(X, Y, U, V, density=2,color=U)
plt.title('地球磁场分布模拟')
plt.grid(True)
plt.show()

