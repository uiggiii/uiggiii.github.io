import numpy as np

A = np.array([
    [1.3, 6.3, -3.5, 2.8],
    [5.6, 0.9, 8.1, -1.3],
    [7.2, 2.3, -4.4, 0.5],
    [1.5, 0.4, 3.7, 5.9]
], dtype=float)
b = np.array([1.8, 16.6, 15.1, 36.9], dtype=float)

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):      # 寻找当前列从对角线开始往下，绝对值最大的元素所在行的索引
        max_row = np.argmax(abs(A[i:n, i])) + i
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
            
    x = np.zeros(n)
    for i in range(n-1, -1, -1):        #倒序往上进行回代求解
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

print(gauss_elimination(A, b))

'''
 [ 3 -2  1  5]
 '''