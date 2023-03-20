# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:11:38 2023

@author: ericd
"""

import numpy as np
import numpy.linalg as la
A = [[2.88, -2.4], [3.6, -3]]

print(la.eig(A))

# x(t)= c_1 * 0.64 * e ^ -3.5e-15t + c_2 * 0.62 * e ^ -0.12t
# y(t)= c_1 * 0.77 * e ^ -3.5e-15t + c_2 * 0.78 * e ^ -0.12t

#t->inf:
    #x(t)= 0 + 0
    #y(t)= 0 + 0