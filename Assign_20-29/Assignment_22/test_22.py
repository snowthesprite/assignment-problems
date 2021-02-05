from gradient_descent import *
import math
'''
def f(x):
    return x**2 + 2*x - 1

print('According to gradient descent, a minimum of f(x) will be {}'.format(gradient_descent(f, 0)))

print()

def g(x):
    return ((x**2) + math.cos(x))/ math.e ** math.sin(x)

print('According to gradient descent, a minimum of g(x) will be {} '.format(gradient_descent(g, 0)))
'''

def f(x):
    return 1 - x**2

print(gradient_descent(f, 2))