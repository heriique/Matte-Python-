# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:28:24 2023

@author: Eric
"""

import numpy as np
from numpy import linalg as la

A = np.array([[4,0,1,-1], [0,4,0,1], [2,1,3,1], [1,1,1,0]])

print(la.eig(A))