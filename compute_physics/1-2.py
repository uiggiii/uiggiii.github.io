import math

#设定初始值
arctanz = 0     
z = 1.0/math.sqrt(3.0)
k = 1

while True :
    delta = ((-1)**(k+1) * z**(2*k-1)) / (2*k-1)    #delta为第k项
    if abs(delta) <=1e-12:
        break
    arctanz += delta
    k += 1

print (f"pi为 {6*arctanz:.12f}")