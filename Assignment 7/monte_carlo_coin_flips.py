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
    all_tests = []
    succeeded_tests = 0
    for test in range(1000) :
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
    return succeeded_tests/1000

print('Is {} the correct probability of 5 heads in 8 coin flips?'.format(probability(5,8)))
assert probability(5,8) == 0.21875, 'No, it is not the right outcome'
print('Yes, it is the right probability')
print('')

print('Test 1 Monte Carlo Probability: {}'.format(monte_carlo_probability(5,8)))
print('Test 2 Monte Carlo Probability: {}'.format(monte_carlo_probability(5,8)))
print('Test 3 Monte Carlo Probability: {}'.format(monte_carlo_probability(5,8)))
print('Test 4 Monte Carlo Probability: {}'.format(monte_carlo_probability(5,8)))
print('Test 5 Monte Carlo Probability: {}'.format(monte_carlo_probability(5,8)))

