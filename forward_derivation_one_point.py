import numpy as np

def f(x):
    return (1+np.e**(x*x))**(1/3)

h = 1e-8

print((f(1+h)-f(1))/h)

