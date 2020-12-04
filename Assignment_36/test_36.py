from grid_search import *

def two_variable_function(x, y):
        return (x-1)**2 + (y-1)**3

x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]

grid_search(two_variable_function, grid_lines)

assert grid_search(two_variable_function, grid_lines) == [0.75, 0.9]