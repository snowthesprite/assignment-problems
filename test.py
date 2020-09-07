def nth_term(n) :
    if n == 2 :
        return 3
    elif n == 1 :
        return 0
    return nth_term(n-1) - 2 * nth_term(n-2)

