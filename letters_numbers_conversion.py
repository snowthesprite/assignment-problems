refrence = ' abcdefghijklmnopqrstuvwxyz'

def convert_to_numbers(samp_str) :
    translation = []
    for char in samp_str :
        translation.append(refrence.index(char))
    return translation

def convert_to_letters(samp_num) : 
    part_trans = []
    for num in samp_num :
        part_trans.append(refrence[num])
    translation = ''.join(part_trans)
    return translation

sample_1 = 'a cat'
sample_2 = [1,0,3,1,20]

print('Is {} the correct conversion of "{}" to numbers'.format(convert_to_numbers(sample_1),sample_1))
assert convert_to_numbers(sample_1) == [1,0,3,1,20], 'No, its not the correct conversion'
print('Yes, it is the correct conversion')
print('')

print('Is "{}" the correct conversion of {} to letters'.format(convert_to_letters(sample_2),sample_2))
assert convert_to_letters(sample_2) == 'a cat', 'No, its not the correct conversion'
print('Yes, it is the correct conversion')
print('')
