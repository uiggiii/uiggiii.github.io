import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h,c,k

cmb_data={'wave_number':[],
          'temperature':[]}
doc_path = r'C:\Users\Lenovo\Documents\GitHub\uiggiii.github.io\compute_physics\cmb-data.txt'

h = h * 1e7  # 转换为 erg*s
c = c * 100  # 转换为 cm/s
k = k * 1e7  # 转换为 erg/K

with open (doc_path,'r',encoding='utf-8') as file:
    for line in file:
        data = line.strip().split()
        nu = float(data[0])
        I = float(data[1])
        if I<0 :
            continue
        T = (h*c*nu) / (k*np.log(2*h*nu**3*c**2/I + 1))
        cmb_data['wave_number'].append(nu)
        cmb_data['temperature'].append(T)


plt.plot('wave_number','temperature',data=cmb_data)
plt.xlabel('wave number ($cm^{-1}$)')
plt.ylabel('temperature (K)')
plt.grid(True)
plt.show()