def convert_to_base_10(num):
    translation = 0
    num_str = str(num)
    i = len(num_str) - 1
    while i >= 0:
        translation += int(num_str[i]) * 2 ** ((len(num_str) - 1)-i)
        i -= 1
    return translation

test = 10011

print('Is {} the correct translation of {} from binary to base-10?'.format(convert_to_base_10(test),test))

#assert convert_to_base_10(test) == 19, "No it is not the right translation"

print("Yes it is the right translation")
print('')
