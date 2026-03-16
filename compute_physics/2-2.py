import numpy as np
import matplotlib.pyplot as plt

#使用字典存储数据
sunspot_record={'date':[],'total_number':[],'standard_deviation':[],'observation_number':[]}

#从sunspot.txt导入数据
with open('SunSpot.txt','r',encoding='utf-8') as file:
    for line in file:
        data = line.strip().split()
        if data[4] == '-1' :
            continue        #排除异常数据
        sunspot_record['date'].append(float(data[3]))
        sunspot_record['total_number'].append(int(data[4]))
        sunspot_record['standard_deviation'].append(float(data[5]))
        sunspot_record['observation_number'].append(int(data[6]))      #存储数据

#制图
plt.plot('date','total_number',data=sunspot_record,color='blue',label='total number')
plt.plot('date','standard_deviation',data=sunspot_record,color='red',label='standard deviation')
plt.plot('date','observation_number',data=sunspot_record,color='green',label='observations number')
plt.title('sunspot record')
plt.xlabel('years')
plt.ylabel('')
plt.grid(True)
plt.legend()
plt.show()