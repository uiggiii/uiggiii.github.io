import matplotlib.pyplot as plt

T = 40

# 定义简谐振子递推函数，用x_list和v_list来储存数据点，假定omega=1
def solve_harmonic_oscillator(h ,T = 40 ,):
    j = 0
    t = 0
    x_list = [1]
    v_list = [0]
    while t < T :
        x_list.append(x_list[j] + h * v_list[j])
        v_list.append(v_list[j] - h * x_list[j])
        j += 1
        t += h
    return x_list,v_list

X_0 , V_0 = solve_harmonic_oscillator(0.05)     # 步长h=0.05
X_1 , V_1 = solve_harmonic_oscillator(0.1)     # 步长h=0.1
X_2 , V_2 = solve_harmonic_oscillator(0.2)     # 步长h=0.2


# 绘制图像
plt.plot( X_0 , V_0 , color = 'blue' , label = 'h=0.05')
plt.plot( X_1 , V_1 , color = 'green' , label = 'h=0.1')
plt.plot( X_2 , V_2 , color = 'red' , label = 'h=0.2')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('简谐振动不同步长轨迹图')
plt.xlabel('x')
plt.ylabel('v')
plt.grid(True)
plt.legend()
plt.show()