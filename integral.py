import numpy as np
n = 1000

x = np.linspace(0, np.pi, n) # n punkter

f = np.sin(x)

#print(f)

integral = sum(f) * np.pi / (n-1)

print(integral)
