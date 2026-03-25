import numpy as np
import matplotlib.pyplot as plt

def solve_harmonic_oscillator(h, T=40):
    '''
    定义简谐振子递推函数，用x_list,v_list,e_list分别储存位移x，速度v和能量偏差率e，假定omega=1
    '''
    j = 0
    t = 0
    x_list = [1]
    v_list = [0]
    e_list = [0]
    while t < T :
        x_list.append(x_list[j] + h * v_list[j])
        v_list.append(v_list[j] - h * x_list[j])
        e_list.append(v_list[j]**2 + x_list[j]**2 - 1)
        j += 1
        t += h
    return x_list,v_list,e_list

X_0 , V_0 , E_0 = solve_harmonic_oscillator(0.05)     # 步长h=0.05
X_1 , V_1 , E_1 = solve_harmonic_oscillator(0.1)     # 步长h=0.1
X_2 , V_2 , E_2 = solve_harmonic_oscillator(0.2)     # 步长h=0.2
T_0 , T_1 , T_2 = np.linspace(0,40.05,802) , np.linspace(0,40,401) , np.linspace(0,40,201)    
'''
在while循环800次后，多个0.05的浮点值相加的结果为39.999999999999865，循环仍未结束，
因此得到了801个数据点，为了减小误差，这里将T_0设置为在0到40.05线性排列
'''

# 绘制图像
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig , (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))

ax1.plot( X_0 , V_0 , color = 'blue' , label = 'h=0.05')
ax1.plot( X_1 , V_1 , color = 'green' , label = 'h=0.1')
ax1.plot( X_2 , V_2 , color = 'red' , label = 'h=0.2')
ax1.set_title('简谐振动不同步长轨迹图')
ax1.set_xlabel('位移x')
ax1.set_ylabel('速度v')
ax1.legend()
ax1.grid(True)

ax2.plot( T_0 , E_0 , color = 'blue' , label = 'h=0.05')
ax2.plot( T_1 , E_1 , color = 'green' , label = 'h=0.1')
ax2.plot( T_2 , E_2 , color = 'red' , label = 'h=0.2')
ax2.set_title('能量损失率')
ax2.set_xlabel('时间t')
ax2.set_ylabel('损失率')
ax2.legend()
ax2.grid(True)

plt.show()