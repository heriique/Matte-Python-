import numpy as np
print("P(a<Z<B)")

n = 1000000 # segmenter
a = -1
b = 1


x = np.linspace(a, b, n, endpoint=False)
f = 1/np.sqrt(2*np.pi)* np.exp(-x**2/2)
integral = sum(f) * (b - a) / n
print(integral)
