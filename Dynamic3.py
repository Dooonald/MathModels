# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:20:39 2018

@author: L
"""

draw = 1000
InitialDeposit = []
TotalDeposit = 0
for i in range(0,96):
    draw = draw/(1+0.0002917)
    print(draw)
    InitialDeposit.append(draw)
TotalDeposit = sum(InitialDeposit)
print(TotalDeposit)
