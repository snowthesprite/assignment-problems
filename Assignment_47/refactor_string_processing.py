string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
split_strings = [x.split(',') for x in string.split('\n')]
string_arr = []
for string_part in split_strings :
    fixed_string_part = []
    for element in string_part :
        if '"' in element :
            fixed_element = element[1:-1]
        elif '.' in element :
            fixed_element = float(element)
        else:
            fixed_element = int(element)
        fixed_string_part.append(fixed_element)
    string_arr.append(fixed_string_part)
print(string_arr)
