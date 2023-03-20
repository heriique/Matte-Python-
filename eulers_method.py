# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:53:02 2022

@author: Eric
"""
import math

# Estimating y in the equation dy/dx = f(x,y)

# Step size
h = 0.5

# Steps (including zero step)
n = 6

x = [0] * n
y = [0] * n
# Initial values
x[0] = 0 # x0
y[0] = 2 # y0 = y(x0)

def f(x, y):
    return 1 - math.sqrt(y)

print("{:<20} {:<20} {:<20} {:<20}".format('n', 'x_n', 'y_n', 'f(x_n, y_n)'))
print('-'*80)

for i in range(n):
    fi = f(x[i], y[i])
    print("{:<20} {:<20} {:<20} {:<20}".format(i, x[i], y[i], fi))
    if i == n - 1:
        break
    x[i + 1] = x[i] + h   
    y[i + 1] = y[i] + h * fi
    
    

