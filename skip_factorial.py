def skip_factorial_nonrecursive(n) :
    final_answer = 1
    if n % 2 == 0 :
        end_of_n = 2
    else :
         end_of_n = 1
    while n >= end_of_n :
        final_answer = final_answer * n
        n = n - 2
    return final_answer 

def skip_factorial_recursive(n) :
    if n == 2 or n == 1 : 
        return n
    return n * skip_factorial_recursive(n - 2)

print('Does the nonrecursive skip factorial function work for 6 and 7?')
assert skip_factorial_nonrecursive(6) == 48, 'No, it doesnt work for 6'
assert skip_factorial_nonrecursive(7) == 105, 'No it doesnt work for 7'
print('It does work for both 6 and 7')
print('')

print('Does the recursive skip factorial function work for 6 and 7?')
assert skip_factorial_recursive(6) == 48, 'No, it doesnt work for 6'
assert skip_factorial_recursive(7) == 105, 'No it doesnt work for 7'
print('It does work for both 6 and 7')
print('')
