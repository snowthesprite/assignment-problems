import math

def convert_to_base_2(num):
    number = num
    translation = 0
    while number > 0 :
        print(number)
        power = math.floor(math.log(number,2))
        translation += 10 ** power
        number -= 2 ** power
    return translation



print(convert_to_base_2(19))