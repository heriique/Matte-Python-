# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:14:24 2022

@author: Eric
"""

import numpy as np

#uten numpy
s = 0
n = 10 # segmenter
a = 0
b = 1

#med numpy
x = np.linspace(a, b, n + 1, endpoint=True)
f = (x + x**3)**0.5
g = lambda y: (y + y**3)**0.5
h = float(b - a)/n
#m = [0] * n
I = 0.0
for i in range(n):
    #m[i] = a + (i + 0.5) * h
    I += g(a + (i + 0.5) * h)
print(I)
