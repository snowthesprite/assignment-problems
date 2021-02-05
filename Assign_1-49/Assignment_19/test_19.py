from zero_of_tangent_line import *

def f(x):
        return x**3 + x - 1

answer = zero_of_tangent_line(f, 0.5, 0.001)
print("Does zero_of_tangent_line correctly assume the zero point?")
assert round(answer,6) == 0.714286, 'No it does not'
print("Yes it does!")
print()

print("Does estimate_solution correctly estimate where the given equation equals zero?")
answer = estimate_solution(f, 0.5, 0.001, 0.01)
assert round(answer, 6) == 0.682328, 'No it does not'
print("Yes it does!")
print()
