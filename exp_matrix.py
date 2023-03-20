# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:20:21 2023

@author: Eric
"""

import numpy as np
from numpy import linalg as la

A = np.array([[-1,4,-2], [-3,4,0], [-3,1,3]])

def matrixMul(a, n):
    if (n <= 1):
        return a
    else:
        return np.matmul(matrixMul(a, n-1), a)

def funk(a):
    return a + 1
    
B = matrixMul(A, 7)
#print(B)
#print(la.eig(B))

print(funk(3))