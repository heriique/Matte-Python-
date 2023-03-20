import numpy as np

#uten numpy
s = 0
n = 1000000 # segmenter
a = 0
b = 1

for i in range(n):
    s = s + np.exp(-(i/n)**2)/n

print(s)

#med numpy
x = np.linspace(a, b, n, endpoint=False)
f = np.exp(-x**2)
integral = sum(f) * (b - a) / n
print(integral)
