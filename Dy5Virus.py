# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:52:48 2018

@author: L
"""

import matplotlib.pyplot as plt
VirusNumber = 1
hours = 1
#首先计算要多少小时免疫系统才能反应
while(VirusNumber <= 1000000):
    VirusNumber = VirusNumber * 2
    hours += 1
print(hours,VirusNumber)
#结果为21小时小时之后免疫系统开始反应
#计算不注射抗生素多少小时会死掉
while(VirusNumber <= 1000000000000):
    VirusNumber = VirusNumber * 1.5 - 200000
    hours += 1
print(hours)
#结果为57小时后，病人会死亡
#注射抗生素的情况,从第21小时开始
def antibiotic(x):
    curve = []
    VirusNumber = 1048576
    for i in range(0,x):#尚未注射
        curve.append(VirusNumber)
        VirusNumber = VirusNumber * 1.5 - 200000
    while VirusNumber >= 0 and VirusNumber <= 1000000000000:
            VirusNumber = VirusNumber * 1.5 - 500000000
            curve.append(VirusNumber)
    plt.plot(curve)  
    if VirusNumber >1000000000000:
        return '死亡'
    if VirusNumber < 0:
        return '存活'
for i in range(1,25):
    print("第%d个小时注射会%s"%(i,antibiotic(i)))
