# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:30:41 2018

@author: L
"""

import matplotlib.pyplot as plt
def drawCurve(a,CurrentLevel):#a即前文中的系数a，CurrentLevel即Xn
    RegentLevel = []
    for i in range(30):
        RegentLevel.append(CurrentLevel)
        CurrentLevel = (a*CurrentLevel-a*(CurrentLevel**2) )
    Time = [i for i in range(30)]
    #plt.plot(Time, RegentLevel)
    #plt.scatter(Time, RegentLevel)
    plt.hist(RegentLevel,bins = 100)
    
factor = [1.5, 2.5, 3, 3.4, 3.5, 3.8]
for j in factor:
    for i in range(1,100):
        drawCurve(j,i/100)
    
    plt.annotate('a = ' + str(j),xy = (5, 0.4),xytext = (6,0.9),
                 arrowprops = dict(facecolor = 'black',shrink = 0.02))
    plt.xlabel('time')#X轴标签
    plt.ylabel('RegentLevel')#Y轴标签
    plt.show()