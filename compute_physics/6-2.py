import numpy as np

A = np.array([
    [1.3, 6.3, -3.5, 2.8],
    [5.6, 0.9, 8.1, -1.3],
    [7.2, 2.3, -4.4, 0.5],
    [1.5, 0.4, 3.7, 5.9]
], dtype=float)
b = np.array([1.8, 16.6, 15.1, 36.9], dtype=float)

def lu_decomposition(A, b):
    n = len(b)
    L = np.eye(n)
    U = np.zeros((n, n))
    
    for i in range(n):      # 将原矩阵拆分为上下两个三角矩阵
        for j in range(i, n):       # 计算上三角矩阵
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
            
        for j in range(i+1, n):     # 计算下三角矩阵
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
            
    
    y = np.zeros(n)
    for i in range(n):                  # 正向替换
        y[i] = b[i] - sum(L[i, k] * y[k] for k in range(i))
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):        # 反向替换
        x[i] = (y[i] - sum(U[i, k] * x[k] for k in range(i+1, n))) / U[i, i]
        
    return L, U, x

L_matrix, U_matrix, x_lu = lu_decomposition(A, b)
print("下三角矩阵:\n", L_matrix)
print("上三角矩阵:\n", U_matrix)
print("分解法求得的结果:", x_lu)


'''
下三角矩阵:
 [[ 1.          0.          0.          0.        ]
 [ 4.30769231  1.          0.          0.        ]
 [ 5.53846154  1.24215773  1.          0.        ]
 [ 1.15384615  0.26180006 -0.12102633  1.        ]]
上三角矩阵:
 [[  1.3          6.3         -3.5          2.8       ]
 [  0.         -26.23846154  23.17692308 -13.36153846]
 [  0.           0.         -13.80477866   1.58944591]
 [  0.           0.           0.           6.35964713]]
分解法求得的结果: [ 3. -2.  1.  5.]
'''