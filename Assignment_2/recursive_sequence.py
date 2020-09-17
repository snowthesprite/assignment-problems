def first_n_terms(n) :
    start_list = [5]
    i = 1
    while i < n :
        start_list.append(3 * start_list[i-1] - 4)
        i += 1
    return start_list

def nth_term(n) :
    if n == 1 :
        return 5
    return 3 * nth_term(n-1) - 4


print('Is {} the right numbers for up to the 10th term in the sequence?'.format(first_n_terms(10)))
assert first_n_terms(10) == [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051] , 'No it is not the right numbers'
print('Yes')

print('')

print('Is {} the right number for the 10th term in the sequence?'.format(nth_term(10),10))
assert nth_term(10) == 59051, 'No it is not the right number'
print('Yes')
