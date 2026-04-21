import numpy as np
import matplotlib.pyplot as plt

# 计算系统总能量
def calc_energy(pos, alpha):
    n = pos.shape[0]
    e_coulomb = 0.0
    for i in range(n):
        for j in range(i+1, n):
            r = np.linalg.norm(pos[i] - pos[j])
            if r < 1e-6: 
                r = 1e-6
            e_coulomb += 1.0 / r
            
    # 计算所有粒子在外加抛物势中的总束缚势能
    e_confine = alpha * np.sum(pos**2)
    return e_coulomb + e_confine

# 系统与算法参数设置
n_particles = 12       # 粒子总数
alpha_val = 1.0        # 束缚势强度参数
r_max = 2.5            # 允许粒子活动的圆形区域最大半径
t_init = 1.0           # 初始“温度”
t_min = 0.001          # 终止“温度”
q_factor = 0.98        # 几何降温因子
steps_per_t = 300      # 在每个温度水平下进行的随机扰动数
delta_step = 0.5       # 单次随机扰动的最大坐标偏移量

# 在指定圆形区域内随机生成粒子的初始坐标
angles = np.random.uniform(0, 2 * np.pi, n_particles)
radii = r_max * np.sqrt(np.random.uniform(0, 1, n_particles))
pos = np.column_stack((radii * np.cos(angles), radii * np.sin(angles)))
pos_init = np.copy(pos)

current_temp = t_init
current_energy = calc_energy(pos, alpha_val)
energy_history = [] 

# 模拟退火主循环
while current_temp > t_min:
    # 在当前温度下执行多次局部微小扰动
    for _ in range(steps_per_t):
        idx = np.random.randint(n_particles) # 随机选取一个需要扰动的粒子
        old_pos = np.copy(pos[idx])          # 记录该粒子原始位置
        
        # 对选定粒子的 x, y 坐标分别施加均匀分布的微小偏移
        pos[idx][0] += np.random.uniform(-delta_step, delta_step)
        pos[idx][1] += np.random.uniform(-delta_step, delta_step)
        
        # 边界条件检查：如果扰动后粒子越过设定边界，则拒绝此次移动
        if np.linalg.norm(pos[idx]) > r_max:
            pos[idx] = old_pos
            energy_history.append(current_energy)
            continue
            
        new_energy = calc_energy(pos, alpha_val)
        delta_e = new_energy - current_energy
        
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / current_temp):
            current_energy = new_energy
        else:
            pos[idx] = old_pos
            
        energy_history.append(current_energy)
        
    current_temp *= q_factor

# 绘制能量随迭代步数下降的曲线图
plt.figure(figsize=(10, 5))
plt.plot(energy_history)
plt.title('系统总能量随迭代步数的变化')
plt.xlabel('迭代步数')
plt.ylabel('总能量')
plt.grid(True)
plt.show()

# 绘制初始构型与最终稳定构型的对比图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
circle1 = plt.Circle((0, 0), r_max, color='gray', fill=False, linestyle='--')
ax1.add_patch(circle1)
ax1.scatter(pos_init[:, 0], pos_init[:, 1])
ax1.set_xlim(-r_max-0.5, r_max+0.5)
ax1.set_ylim(-r_max-0.5, r_max+0.5)
ax1.set_aspect('equal')
ax1.set_title('初始随机构型')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

circle2 = plt.Circle((0, 0), r_max, color='gray', fill=False, linestyle='--')
ax2.add_patch(circle2)
ax2.scatter(pos[:, 0], pos[:, 1])
ax2.set_xlim(-r_max-0.5, r_max+0.5)
ax2.set_ylim(-r_max-0.5, r_max+0.5)
ax2.set_aspect('equal')
ax2.set_title('模拟退火后的稳定构型')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.show()