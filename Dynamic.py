# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:44:17 2018

@author: L
"""

import matplotlib.pyplot as plt

def drawCurve(Reagentperday,CurrentLevel):
    RegentLevel = []
    for i in range(15):
        RegentLevel.append(CurrentLevel)
        CurrentLevel = CurrentLevel * 0.5 + Reagentperday
    Time = [i for i in range(15)]
    #print(Time,RegentLevel)
    plt.plot(Time, RegentLevel)
for j in range(1,10):
    for i in range(1,10):
        drawCurve(j,i)
        
    plt.title(str(j) + 'th Relationship between time and RegentLevel')#创建标题
    plt.xlabel('time')#X轴标签
    plt.ylabel('RegentLevel')#Y轴标签
    plt.show()

