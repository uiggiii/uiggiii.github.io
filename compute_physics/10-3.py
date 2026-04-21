import numpy as np

n_bi213 = 10**5
n_tl209 = 0
n_pb209 = 0
n_bi209 = 0
t_half_bi213 = 45.6 * 60
t_half_tl209 = 2.2 * 60
t_half_pb209 = 3.3 * 3600

# 计算衰变常数
lambda_bi213 = np.log(2) / t_half_bi213
lambda_tl209 = np.log(2) / t_half_tl209
lambda_pb209 = np.log(2) / t_half_pb209

dt = 1.0  # 步长为1秒
p_bi213 = 1 - np.exp(-lambda_bi213 * dt)
p_tl209 = 1 - np.exp(-lambda_tl209 * dt)
p_pb209 = 1 - np.exp(-lambda_pb209 * dt)

time_sec = 0

# 按照二项分布随机抽取当前一秒内发生衰变的核素数量
while n_bi209 <= n_bi213:
    decay_bi213 = np.random.binomial(n_bi213, p_bi213)
    decay_tl209 = np.random.binomial(n_tl209, p_tl209)
    decay_pb209 = np.random.binomial(n_pb209, p_pb209)

    decay_bi213_to_tl = np.random.binomial(decay_bi213, 0.0209) 
    decay_bi213_to_pb = decay_bi213 - decay_bi213_to_tl

    n_bi213 -= decay_bi213
    n_tl209 += decay_bi213_to_tl - decay_tl209
    n_pb209 += decay_bi213_to_pb + decay_tl209 - decay_pb209
    n_bi209 += decay_pb209
    
    time_sec += dt

print(f"稳定同位素数量超过母核所需时间约为: {time_sec / 60:.2f} 分钟")


'''
>>> 稳定同位素数量超过母核所需时间约为: 112.63 分钟
'''