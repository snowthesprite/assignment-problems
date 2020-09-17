def is_prime(num) :
    i = 2
    while i < num/2 :
        if num % i == 0 :
            return False
        i += 1
    return True

num_1 = 59
num_2 = 51

print('Is {} prime?'.format(num_1))
assert is_prime(num_1) == True, 'No, its not but it should be'
print('Yes, {} is prime'.format(num_1))
print('')

print('Is {} prime?'.format(num_2))
assert is_prime(num_2) == False, 'Yes, it is but it shouldnt be'
print('No, {} is not prime'.format(num_2))