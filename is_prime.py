def is_prime(num) :
    i = 2
    while i < num/2 :
        if num % i == 0 :
        return False
    i += 1
    return True