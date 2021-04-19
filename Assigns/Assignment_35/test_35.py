from assignment_35_stats import *

def function(k) :
    return 1/k**5

guess = guess_summation(function, 25, 100000)
print(1/guess)

def function(k) :
    return (1.4432 * 10 ** 6)/k**5

print(certanty(0.95, function, 25))

def function(n) :
    return 1/n ** 4

guess = guess_summation(function, 68, 100000)
print(1/guess)

def function(n) :
    return (9.22742 * 10**5)/n**4

print(certanty(0.95, function, 68))
