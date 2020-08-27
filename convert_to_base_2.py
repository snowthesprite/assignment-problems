import math

def convert_to_base_2(num):
    translation = 0
    num_len = math.ceil(math.log(num,2))
    i = num_len - 1
    while i > 0 :
        if translation == 0: 
            translation += 10 ** i
        return math.log(num - (2 ** i),2)



print(convert_to_base_2(19))