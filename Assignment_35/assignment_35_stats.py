def guess_summation(func, start_term, max_term) :
    sum_guess = 0
    for term in range(start_term, max_term) :
        sum_guess += func(term)
    return sum_guess

def certanty(percent, funct, bound) :
    chance = 0
    while chance < percent :
        chance +=  funct(bound)
        bound += 1
    return bound