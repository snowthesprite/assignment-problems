def is_prime(num) :
    i = 2
    while i < num/2 :
        if num % i == 0 :
        return False
    i += 1
    return True

num_1 = 59
num_2 = 51

print('Test: Is {} prime?'.format(num_1))
print(is_prime(num_1))

print('Test: Is {} prime?'.format(num_2))
print(is_prime(num_2))
