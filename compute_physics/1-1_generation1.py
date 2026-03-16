import math

A_k = 3.0    #内接六边形周长为3
k = 6

while True:
    B_k = 1.0 / math.sqrt(1.0 / (A_k**2) - 1.0 / (k**2))    #外切正6k边形周长
    
    if B_k - A_k < 1e-11:
        break
        
    A_k = k * math.sqrt(2 * (1 - math.sqrt(1 - (A_k / k)**2)))    #内接正12k边形周长
    k *= 2

pi_approx = (A_k + B_k) / 2    #取两周长平均值为pi的计算所得值

print(f"pi: {pi_approx:.12f}")
print(f"边数k: { k}")


"""
计算之后发现误差过大，可能是因为递推式中有大量开方的计算，导致了精度丢失
"""