import numpy as np
import matplotlib.pyplot as plt

N = 10**6
steps = 100
choices = [-1, 0, 1]
probs = [1/6, 2/6, 3/6]

# 蒙特卡洛模拟生成 N 个粒子在 100 秒内的随机步数
all_steps = np.random.choice(choices, size=(N, steps), p=probs)
final_positions = np.sum(all_steps, axis=1)

# 计算(15, 25)特定区间内的概率
count_in_range = np.sum((final_positions > 15) & (final_positions < 25))
prob_in_range = count_in_range / N
print(f"经过100秒后，任意一个粒子落在 (15, 25) 区间里的概率为: {prob_in_range:.4f}")

plt.figure(figsize=(10, 6))
bins = range(min(final_positions), max(final_positions) + 2)
plt.hist(final_positions, bins=bins, density=True, alpha=0.7, color='steelblue', edgecolor='black')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.title('10^6个粒子在经过100秒后的位置分布')
plt.xlabel('坐标位置 x')
plt.ylabel('出现频率')
plt.grid(True, alpha=0.3)
plt.show()