from gradient_descent import *

#you didn't want the point last time so I didn't put the answer back into a tuple

function = lambda x, y : 1 + x ** 2 + y ** 2

print('For 1 + x^2 + y^2 :')
print('The predicted Minimum point is (0,0,1)')
print('The calculated Minimum is {}'.format(gradient_descent(function, (1,2))))
print()

function = lambda x, y : 1 + x ** 2 + 2 * x + y ** 2 - 9 * y

print('For 1 + x^2 + 2x + y^2 - 9y :')
print('The predicted Minimum point is (-1, 4.5, -20.25)')

'''
Math behind it:
f(x,y) = 1 + x^2 + 2x + y^2 - 9y
    = x^2 + 2x + 1 + y^2 - 9y
    = (x + 1)^2 + y^2 - 9y
    = (x + 1)^2 + y^2 - 9y + (9/2)^2 - (9/2)^2
    = (x + 1)^2 + y^2 - 9y + 20.25 - 20.25
    = (x + 1)^2 + (y - 4.5)^2 - 20.25
'''

print('The calculated Minimum is {}'.format(gradient_descent(function, (0,0))))