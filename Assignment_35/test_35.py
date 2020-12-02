from assignment_35_stats import *

def function(k) :
    return 1/k**5

guess = guess_summation(function, 25, 100000)
print(1/guess)
