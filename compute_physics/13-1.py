import numpy as np
import matplotlib.pyplot as plt


def plot_sine_map():
    # 设置正弦映射的参数，重点观察分叉区域
    r_values = np.linspace(0.6, 1.0, 1000)
    iterations = 1000
    last_iterations = 100
    x = np.ones(len(r_values)) * 0.1
    lyapunov = np.zeros(len(r_values))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

    for i in range(iterations):
        x = r_values * np.sin(np.pi * x)

        if i >= iterations - last_iterations:
            ax1.plot(r_values, x, ',k', alpha=0.2)
        # 累加对数导数以计算指数
        derivative = np.abs(r_values * np.pi * np.cos(np.pi * x))
        lyapunov += np.log(np.maximum(derivative, 1e-10))

    lyapunov /= iterations

    ax1.set_title("正弦映射的分叉图")
    ax1.set_ylabel("系统状态")
    ax2.plot(r_values, lyapunov, 'k-', lw=1)
    ax2.axhline(0, color='r', linestyle='--')
    ax2.set_title("正弦映射的李雅普诺夫指数")
    ax2.set_xlabel("控制参数")
    ax2.set_ylabel("指数值")
    plt.tight_layout()
    plt.show()

def plot_logistic_map():
    # 设置逻辑斯蒂映射的参数进行对比讨论
    mu_values = np.linspace(2.5, 4.0, 1000)
    iterations = 1000
    last_iterations = 100
    x = np.ones(len(mu_values)) * 0.1
    lyapunov = np.zeros(len(mu_values))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

    for i in range(iterations):
        # 逻辑斯蒂映射公式
        x = mu_values * x * (1 - x)
        if i >= iterations - last_iterations:
            ax1.plot(mu_values, x, ',k', alpha=0.2)
        derivative = np.abs(mu_values * (1 - 2 * x))
        lyapunov += np.log(np.maximum(derivative, 1e-10))

    lyapunov /= iterations

    ax1.set_title("逻辑斯蒂映射的分叉图")
    ax1.set_ylabel("系统状态")
    ax2.plot(mu_values, lyapunov, 'k-', lw=1)
    ax2.axhline(0, color='r', linestyle='--')
    ax2.set_title("逻辑斯蒂映射的李雅普诺夫指数")
    ax2.set_xlabel("控制参数")
    ax2.set_ylabel("指数值")
    plt.tight_layout()
    plt.show()


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



plot_sine_map()
plot_logistic_map()