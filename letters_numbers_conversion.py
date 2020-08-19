ref = ' abcdefghijklmnopqrstuvwxyz'

def convert_to_numbers(samp_str) :
    num_list = []
    for char in samp_str :
        num_list.append(ref.index(char))
    return num_list

def convert_to_letters(samp_num) : 
    emp_list = []
    for num in samp_num :
        emp_list.append(ref[num])
    newStr = ''.join(emplist)
    return newStr