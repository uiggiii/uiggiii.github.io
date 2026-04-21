import numpy as np

A = np.array([
    [1.3, 6.3, -3.5, 2.8],
    [5.6, 0.9, 8.1, -1.3],
    [7.2, 2.3, -4.4, 0.5],
    [1.5, 0.4, 3.7, 5.9]
], dtype=float)
b = np.array([1.8, 16.6, 15.1, 36.9], dtype=float)

def gauss_seidel(A, b, max_iter=1000, tol=1e-6):
    n = len(b)
    x = np.zeros(n)

    for k in range(max_iter):
        max_diff = 0.0      #数值变化的最大幅度
        
        for i in range(n):
            s1 = sum(A[i, j] * x[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            new_xi = (b[i] - s1 - s2) / A[i, i]
            max_diff = max(max_diff, abs(new_xi - x[i]))
            x[i] = new_xi
        if max_diff < tol:
            print(f"迭代法在第 {k+1} 次计算后达到稳定。")
            return x

    print("迭代法未在最大次数内达到稳定状态。")
    return x

print("迭代法求得的结果:", gauss_seidel(A, b))


'''
迭代法在第 232 次计算后达到稳定。
迭代法求得的结果: [nan nan nan nan]
'''