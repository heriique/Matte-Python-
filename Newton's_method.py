# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 01:17:38 2022

@author: Eric
"""
import numpy as np

# The function to use Newton's method on
def f(x):
    return np.e ** x + x - 3

# Initial guess
x0 = 1

# Stop after this many iterations if not converging to a solution
max_iterations = 10

# Calculates the forward derivative of f at point a, using h (optional) as delta_x
def derivative(f, a, h = 1e-8):
    return (f(a + h) - f(a)) / h

# Finds the next element in the series approximating a solution
def next(f, x):
    return x - f(x) / derivative(f, x)

# List of approximations
x = [x0]
x.append(next(f, x0))

# Length of x
i = 2

# Add to the list until we converge or reach max_iterations
while (x[i - 1] != x[i - 2] and i < max_iterations):
    x.append(next(f, x[i - 1]))
    i += 1
    
if i == max_iterations:
    print("Could not find an accurate solution after {0] iterations", max_iterations)
else:
    print("f(x)=0 for x={0} after {1} iterations".format(x[i - 1], i))