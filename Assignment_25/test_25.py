from gradient_descent import *

#a) Minimum is x = 1, y = 0

function = lambda x, y : 1 + x ** 2 + y ** 2

print(gradient_descent(function, (1,2)))