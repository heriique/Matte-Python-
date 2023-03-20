# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:03:17 2023

@author: ericd
"""

import numpy as np
z = (5 - 9j) * (3 + 1j) ** 3 / (1 + 2j) ** 5
print(np.imag(z))