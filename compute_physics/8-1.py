import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def V(x):
    return np.where((x < 0) | (x > 1), 1000, 0)

def schrodinger_equation(x, y, E):
    psi, dpsi = y
    d2psi = (V(x) - E) * psi
    return [dpsi, d2psi]

# 定义打靶法的目标函数，输入一个猜测的能量值，返回积分到右侧边界时的波函数绝对值
def shoot(E):
    sol = solve_ivp(schrodinger_equation, [-1, 2], [0, 0.01], args=(E,), 
                    rtol=1e-10, atol=1e-12)
    return sol.y[0, -1]

root1 = root_scalar(shoot, bracket=[5, 15], xtol=1e-12)
E1 = root1.root

root2 = root_scalar(shoot, bracket=[25, 45], xtol=1e-12)
E2 = root2.root

# 在 x=0.3 处拼接，避开中心波节
def get_stable_wavefunction(E, x_match=0.3):
    x_L = np.linspace(-1, x_match, 250)
    x_R = np.linspace(2, x_match, 250) 
    
    sol_L = solve_ivp(schrodinger_equation, [-1, x_match], [0, 0.01], args=(E,), dense_output=True)
    psi_L = sol_L.sol(x_L)[0]
    
    sol_R = solve_ivp(schrodinger_equation, [2, x_match], [0, -0.01], args=(E,), dense_output=True)
    psi_R = sol_R.sol(x_R)[0]
    
    scale = psi_L[-1] / psi_R[-1] 
    psi_R_scaled = psi_R * scale
    
    x_full = np.concatenate((x_L, x_R[::-1][1:]))
    psi_full = np.concatenate((psi_L, psi_R_scaled[::-1][1:]))
    
    psi_full = psi_full / np.sqrt(np.trapezoid(psi_full**2, x_full))
    return x_full, psi_full

x_eval1, psi1 = get_stable_wavefunction(E1)
x_eval2, psi2 = get_stable_wavefunction(E2)

if psi1[np.argmax(np.abs(psi1))] < 0:
    psi1 = -psi1
if psi2[np.argmax(np.abs(psi2[:250]))] < 0:
    psi2 = -psi2

plt.figure(figsize=(10, 6))

plt.plot(x_eval1, psi1, label=rf"$\psi_1(x), E_1 = {E1:.4f}$", color='blue')
plt.plot(x_eval2, psi2, label=rf"$\psi_2(x), E_2 = {E2:.4f}$", color='red')
plt.plot(x_eval1, V(x_eval1)/300, 'k--', label=r"$V(x)/300$")

plt.xlim(-1.1, 2.1)
plt.xlabel(r"$x$")
plt.ylabel(r"$\psi(x)$")
plt.title("Finite square well: shooting method")
plt.legend(loc='lower left')
plt.grid(True)

plt.show()