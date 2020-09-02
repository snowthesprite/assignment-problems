import math

def convert_to_base_2(num):
    number = num
    translation = 0
    while number > 0 :
        power = math.floor(math.log(number,2))
        translation += 10 ** power
        number -= 2 ** power
    return translation

test = 19

print('Is {} the correct conversion to base 2 from {}?'.format(convert_to_base_2(test),test))
assert convert_to_base_2(test) == 10011, 'No it does not correctly convert'
print('Yes, {} is the correct conversion from {}'.format(convert_to_base_2(test),test))
print('')