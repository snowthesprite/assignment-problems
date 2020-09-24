from random import random

def find_factorial(n) :
    if n == 1 or n == 0 : 
        return 1
    return n * find_factorial(n - 1)

def probability(num_heads, num_flips) :
    total_outcomes = 2 ** num_flips
    numerator = find_factorial(num_flips)
    denominator = (find_factorial(num_heads) * (find_factorial(num_flips - num_heads)))
    head_outcomes = numerator / denominator
    return head_outcomes/total_outcomes


def monte_carlo_probability(num_heads, num_flips, test_amount) :
    all_tests = []
    succeeded_tests = 0
    for test in range(test_amount) :
        is_heads = []
        for heads in range(num_flips):
            heads_tails = random()
            if heads_tails >= 0.5 :
                is_heads.append(True)
            else:
                is_heads.append(False)
        all_tests.append(is_heads)
    for test in all_tests :
        amount_of_heads = 0
        for outcome in test :
            if outcome :
                amount_of_heads += 1
        if amount_of_heads == num_heads :
            succeeded_tests += 1
    return succeeded_tests/test_amount
