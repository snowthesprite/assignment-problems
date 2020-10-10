from zero_of_tangent_line import *

print('Does zero_of_tangent_line properly estimate the zero for 0.5')

assert round(zero_of_tangent_line(0.5), 6) == 0.714286, 'No it does not'
print('Yes it does!')
print('')

print('Does estimate_solution properly estimate the zero within 0.01 precision?')

assert round(estimate_solution(0.01), 7) == 0.6823284, 'No it does not'
print('Yes it does!')
