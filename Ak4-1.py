# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:15:12 2022

@author: Eric
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 3.0, 0.2)
plt.plot(x, 2 * np.exp(1-x**2/2), 'r--', x, 6-2*2**0.5*x, 'g-')
plt.show()