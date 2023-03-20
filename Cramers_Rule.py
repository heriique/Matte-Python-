# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:17:20 2022

@author: ercr1608
"""
# Naive/simple implementation of Cramer's rule. For efficiency, use Gaussian
# elimination instead.

import numpy as np

n = 5 # matrix size

# Define your A matrix here
A = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        A[i, j] = (i + 1)**(n - 1 - j)
        
# Define your b vector here
b = [0, 0, 0, 1, 1]

detA = np.linalg.det(A)

# Which x_i do you want to find?
i = 2

# B is a copy of A where the ith row is replaced by b.
B = A.copy()
B[:, i] = b

detB = np.linalg.det(B)
x = detB/detA

print("detB=" + str(detB))
print("x=" + str(x))
print(str(-43/8))

#Alternative way to build B (using less memory since we don't copy A):
#left = A[:, :i]
#right = A[:, i + 1:]
#B = [left, b, right]


