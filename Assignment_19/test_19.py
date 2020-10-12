from zero_of_tangent_line import *

def f(x):
        return x**3 + x - 1

answer = zero_of_tangent_line(f, 0.5)
assert round(answer,6) == 0.714286
answer = estimate_solution(f, 0.5, 0.01)
assert round(answer, 6) == 0.682328