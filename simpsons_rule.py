# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:33:18 2022

@author: Eric
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:14:24 2022

@author: Eric
"""

import numpy as np

a = -1
b = 1
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = (1 + x**3)**0.5

I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) \
            + 4*sum(f[1:n-1:2]) + f[n-1])
print(I_simp)