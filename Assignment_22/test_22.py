from gradient_descent import *
import math

def f(x):
    return x**2 + 2*x - 1

print(gradient_descent(f, 0))

def g(x):
    return ((x**2) * math.cos(x))/ math.exp(math.sin(x))

print(gradient_descent(g, 0))