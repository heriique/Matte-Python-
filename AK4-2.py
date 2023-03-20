# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:36:27 2022

@author: Eric
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.0, 1.0, 0.1)
plt.plot(x, x**2*np.sin(x)*np.cos(x), 'r-')
plt.show()