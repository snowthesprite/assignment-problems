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

print(skip_factorial_recursive(7))
