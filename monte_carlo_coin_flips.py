from random import random

def find_factorial(n) :
    if n == 1 : 
        return n
    return n * find_factorial(n - 1)

def probability(num_heads, num_flips) :
    total_outcomes = 2 ** num_flips
    numerator = find_factorial(num_flips)
    denominator = (find_factorial(num_heads) * (find_factorial(num_flips - num_heads)))
    head_outcomes = numerator / denominator
    return head_outcomes/total_outcomes


def monte_carlo_probability(num_heads, num_flips) :
    for test in range(1000) :
        for heads in range 



assert probability(5,8) == 0.21875, 'No, it is not the right outcome'

