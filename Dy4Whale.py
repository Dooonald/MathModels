# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:28:17 2018

@author: L
"""

import matplotlib.pyplot as plt

def whale(a, M, m, k):
    list1 = []
    
    for i in range(1,100):
        list1.append(a)
        a += k*(M - a)*(a - m)
    plt.plot(list1)
    
iniList = [100, 150, 300, 500, 700, 1000, 2000]
for j in iniList:
    whale(j, 1000, 100, 0.0001)