def is_symmetric(string) :
    i = 0
    while i < len(string) :
        if string[i] != string[len(string)-(i+1)]:
            return False
        i += 1
    return True

test_1 = 'batman'
print('Test: Is {} symmetric?'.format(test_1))
print(is_symmetric(test_1))