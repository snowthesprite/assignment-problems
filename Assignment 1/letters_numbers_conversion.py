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
    newStr = ''.join(emp_list)
    return newStr

sample_1 = 'a cat'
sample_2 = [1,0,3,1,20]

print('convert "{}" to numbers'.format(sample_1))
print('{} --> {}'.format(sample_1, convert_to_numbers(sample_1)))

print('convert {} to letters'.format(sample_2))
print('{} --> {}'.format(sample_2, convert_to_letters(sample_2)))
