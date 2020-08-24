start_list = [5]
def first_n_terms(n) :
    i = 1
    while i < n :
        start_list.append(3 * start_list[i-1] - 4)
        i += 1
    return start_list

def nth_term(n) :
    if n == 1 :
        return 5
    return 3 * first_n_terms(n-1) - 4

print(first_n_terms(10))