import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20.0,100)

def upward_draw():
    '''
    先创建一个空的二维数组，然后利用向上迭代法储存并返回2，5，10阶函数值
    '''
    j = np.zeros((11, len(x)))
    j[0] = np.sin(x) / x
    j[1] = np.sin(x)/x**2 - np.cos(x)/x
    for l in range(1, 10):
        j[l+1] = (2*l + 1)/x*j[l] - j[l-1]
    return j[2], j[5], j[10]

def downward_draw(l_start=50):
    '''
    从第50阶开始，指定第50阶为0，第49阶为一个极小数，由这两阶向下迭代得出各阶函数式，
    此时每一阶与真实值有一个scale的倍数关系，利用第0阶求出scale，最后返回真实的2，5，10阶函数值
    '''
    j = np.zeros((l_start + 1, len(x)))
    j[l_start] = 0
    j[l_start-1] = 1e-30
    for l in range(l_start - 1, 0, -1):
        j[l-1] = (2*l + 1)/x*j[l] - j[l+1]
    scale = np.sin(x) / j[0]
    return j[2]*scale, j[5]*scale, j[10]*scale


j_up_2, j_up_5, j_up_10 = upward_draw()
j_down_2, j_down_5, j_down_10 = downward_draw()

#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig , (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))

#向上迭代图
ax1.plot(x, j_up_2, color='red', label='j_2' ) 
ax1.plot(x, j_up_5, color='blue', label='j_5' )
ax1.plot(x, j_up_10, color='green', label='j_10')
ax1.set_title('向上迭代球贝塞尔函数')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True)

#向下迭代图
ax2.plot(x, j_down_2, color='red', label='j_2' ) 
ax2.plot(x, j_down_5, color='blue', label='j_5' )
ax2.plot(x, j_down_10, color='green', label='j_10')
ax2.set_title('向下迭代球贝塞尔函数')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid(True)

plt.show()