# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:15:39 2018

@author: L
"""
import matplotlib.pyplot as plt 
import numpy as np

time = [i for i in range(0,19)]
number = [9.6,18.3,29,47.2,71.1,119.1,174.6,257.3,\
          350.7,441.0,513.3,559.7,594.8,629.4,640.8,\
          651.1,655.9,659.6,661.8]
plt.plot(time,number, color = 'b')
"""
F1 = np.polyfit(time, number, 1)
P1 = np.poly1d(F1)
print(P1)            #45.49 x - 36.56
y1 = np.polyval(F1, time)
plt.plot(time, y1, color = 'r')

F2 = np.polyfit(time, number, 2)
P2 = np.poly1d(F2)
print(P2)            
y2 = np.polyval(F2, time)
plt.plot(time, y2, color = 'y')
"""
F3 = np.polyfit(time, number, 3)
P3 = np.poly1d(F3)
print(P3)            
y3 = np.polyval(F3, time)
plt.plot(time, y3, color = 'g')

#modeling
pn = [9.6,18.3,29,47.2,71.1,119.1,174.6,\
      257.3,350.7,441.0,513.3,559.7,594.8,629.4,\
      640.8,651.1,655.9,659.6]
deltap = [8.7,10.7,18.2,23.9,48,55.5,\
          82.7,93.4,90.3,72.3,46.4,35.1,\
          34.6,11.4,10.3,4.8,3.7,2.2]
pn = np.array(pn)
factor = pn * (665-pn)
f = np.polyfit(factor, deltap, 1)
print(f)

#plot
p0 = 9.6
p_list = []
for i in range(20):
    p_list.append(p0)
    p0 += 0.00081448 * p0 * (665-p0)
    
plt.plot(p_list, color = 'r')


plt.title('Relationship between time and number')#创建标题
plt.xlabel('time')#X轴标签
plt.ylabel('number')#Y轴标签
plt.show()#显示


