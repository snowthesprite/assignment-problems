def guess_summation(func, start_term, max_term) :
    sum_guess = 0
    for term in range(start_term, max_term) :
        sum_guess += func(term)
    return sum_guess