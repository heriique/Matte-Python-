import numpy as np

#uten numpy
s = 0
n = 1000000 # segmenter
a = -1
b = 1

print(s)

#med numpy
x = np.linspace(a, b, n, endpoint=False)
f = 2* np.sqrt(1 + 16*x**2/(1**2))
integral = sum(f) * (b - a) / n
print(integral)
# Write your code here :-)
