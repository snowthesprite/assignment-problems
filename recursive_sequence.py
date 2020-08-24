def first_n_terms(n) :
    if n == 1 :
        return 5
    return 3 * first_n_terms(n-1) - 4

#def nth_term() :
    
print(first_n_terms(10))