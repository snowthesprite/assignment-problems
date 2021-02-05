def is_symmetric(string) :
    i = 0
    while i < len(string) :
        if string[i] != string[len(string)-(i+1)]:
            return False
        i += 1
    return True

test_1 = 'racecar'
test_2 = 'batman'

print('Is {} symmetric?'.format(test_1))
assert is_symmetric(test_1) == True, 'No, its not symmetric but it should be'
print('Yes, {} is symmetric'.format(test_1))
print('')

print('Is {} symmetric?'.format(test_2))
assert is_symmetric(test_2) == False, 'Yes, its symmetric but it shouldnt be'
print('No, {} is not symmetric'.format(test_2))
print('')
