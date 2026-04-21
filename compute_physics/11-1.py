import numpy as np
import matplotlib.pyplot as plt

L = 20
J = 1.0
# 计算翻转单个自旋引起的能量变化
def calculate_delta_e(lattice, i, j):
    spin = lattice[i, j]
    neighbors = 0
    if i > 0:
        neighbors += lattice[i-1, j]
    if i < L - 1:
        neighbors += lattice[i+1, j]
    if j > 0:
        neighbors += lattice[i, j-1]
    if j < L - 1:
        neighbors += lattice[i, j+1]
    
    return 2 * J * spin * neighbors
# 执行一次完整的蒙特卡罗步，遍历所有格点
def mcmc_step(lattice, beta):
    for _ in range(L * L):
        i = np.random.randint(0, L)
        j = np.random.randint(0, L)
        delta_e = calculate_delta_e(lattice, i, j)
        
        # 梅特罗波利斯准则
        if delta_e < 0 or np.random.rand() < np.exp(-beta * delta_e):
            lattice[i, j] *= -1

def calculate_total_energy(lattice):
    energy = 0
    for i in range(L):
        for j in range(L):
            spin = lattice[i, j]
            neighbors = 0
            if i < L - 1:
                neighbors += lattice[i+1, j]
            if j < L - 1:
                neighbors += lattice[i, j+1]
            energy -= J * spin * neighbors
    return energy

# 模拟系统演化
def simulate(beta, steps=2000, seed=None):
    if seed is not None:
        np.random.seed(seed)
        
    # 初始化：随机向上或向下
    lattice = np.random.choice([-1, 1], size=(L, L))
    
    # 预热阶段，使系统达到平衡态
    for _ in range(1000):
        mcmc_step(lattice, beta)
        
    # 测量阶段
    energies = []
    spins = []
    for _ in range(steps):
        mcmc_step(lattice, beta)
        energies.append(calculate_total_energy(lattice))
        spins.append(np.sum(lattice))
        
    return np.mean(energies), np.mean(spins)

#验证

print("1. 温度 T=1.0 (beta=1.0) 时的平衡态模拟")
energy, spin = simulate(beta=1.0, seed=42)
print(f"总能量平均值: {energy:.2f}")
print(f"总自旋平均值: {spin:.2f}\n")

print("2. 设定不同的随机数种子检验平衡态总自旋")
for seed in [10, 20, 30]:
    _, spin_val = simulate(beta=1.0, seed=seed)
    print(f"种子 {seed} 的总自旋平均值: {spin_val:.2f}")
print()

print("3. 变化逆温度 beta 在 [1.0, 0.1] 之间")
betas = np.linspace(1.0, 0.1, 10)
energies_list = []
spins_list = []

for b in betas:
    e, s = simulate(beta=b, seed=42)
    energies_list.append(e)
    spins_list.append(abs(s)) # 关注自旋的绝对值（磁化强度大小）
    print(f"逆温度 {b:.1f}: 总能量 = {e:.2f}, 总自旋绝对值 = {abs(s):.2f}")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制结果以辅助讨论
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(betas, energies_list, 'o-')
plt.xlabel("逆温度")
plt.ylabel("系统总能量")
plt.gca().invert_xaxis() # 逆温度减小意味着温度升高

plt.subplot(1, 2, 2)
plt.plot(betas, spins_list, 'ro-')
plt.xlabel("逆温度")
plt.ylabel("总自旋绝对值")
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()


'''
1. 温度 T=1.0 (beta=1.0) 时的平衡态模拟
总能量平均值: -757.43
总自旋平均值: -399.05

2. 设定不同的随机数种子检验平衡态总自旋
种子 10 的总自旋平均值: -399.05
种子 20 的总自旋平均值: -399.08
种子 30 的总自旋平均值: 398.95

3. 变化逆温度 beta 在 [1.0, 0.1] 之间
逆温度 1.0: 总能量 = -757.43, 总自旋绝对值 = 399.05
逆温度 0.9: 总能量 = -754.51, 总自旋绝对值 = 398.00
逆温度 0.8: 总能量 = -748.95, 总自旋绝对值 = 396.02
逆温度 0.7: 总能量 = -735.50, 总自旋绝对值 = 390.88
逆温度 0.6: 总能量 = -704.55, 总自旋绝对值 = 377.01
逆温度 0.5: 总能量 = -606.87, 总自旋绝对值 = 303.69
逆温度 0.4: 总能量 = -397.89, 总自旋绝对值 = 1.75
逆温度 0.3: 总能量 = -264.40, 总自旋绝对值 = 0.97
逆温度 0.2: 总能量 = -161.24, 总自旋绝对值 = 1.33
逆温度 0.1: 总能量 = -76.17, 总自旋绝对值 = 0.10
'''