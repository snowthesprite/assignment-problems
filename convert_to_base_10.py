def convert_to_base_10(num):
    translation = 0
    num_str = str(num)
    i = len(num_str) - 1
    while i >= 0 :
        translation += int(num_str[i]) * 2 ** ((len(num_str) - 1)-i)
        i -= 1
    return translation

print(convert_to_base_10(10011))
