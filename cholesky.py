# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 19:03:14 2018

@author: LeeDD
"""

import numpy as np
import math


mat = [[4,12,-16], [12,37,-43],[-16,-43,98]]
n = 3;

for j in range(n):
    mat[j][j] = math.sqrt(mat[j][j])
    
    for i in range(j+1, n):
        mat[i][j] = mat[i][j] / mat[j][j]
    
    for k in range(j+1, n):
        for i in range(k, n):
            mat[i][k] = mat[i][k] - mat[i][j]*mat[k][j]
    