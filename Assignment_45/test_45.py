from standard_normal_probability_2 import *
import matplotlib.pyplot as plt
''''
print(calc_standard_normal_probability(0, 1, 6, "left endpoint"))
print()
print(calc_standard_normal_probability(0, 1, 100, "right endpoint"))
print()
print(calc_standard_normal_probability(0, 1, 100, "midpoint"))
print()
print(calc_standard_normal_probability(0, 1, 100, "trapezoidal"))
print()
print(calc_standard_normal_probability(0, 1, 20, "simpson"))
print()
'''
keys = ["left endpoint", "right endpoint", "midpoint", "trapezoidal", "simpson"]

plt.style.use('bmh')
x_points = []
y_points = {key : [] for key in keys}
for subinterval_number in range(2, 21) :
    x_points.append(subinterval_number)
    for key in keys :
        y_points[key].append(calc_standard_normal_probability(0, 1, subinterval_number, key))
''''
for key in keys :
    plt.plot(x_points, y_points[key])
plt.legend(keys)
'''
plt.plot(x_points, y_points[keys[0]])
plt.plot(x_points, y_points[keys[1]])
plt.savefig('Assignment_45/eulerplot.png')