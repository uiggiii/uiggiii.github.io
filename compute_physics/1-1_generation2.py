import math

A = 3.0
B = 2.0 * math.sqrt(3.0)
k = 6

while B - A >= 1e-11:
    B = (2 * A * B) / (A + B)    #B_{2k}关于A_k的表达式
    A = math.sqrt(A * B)    #A_{2k}与A_k的递推关系
    k *= 2

pi_approx = (A + B) / 2    #取两周长平均值为pi的计算所得值

print(f"平均数: {pi_approx:.12f}")
print(f"边数k: {k}")

