alphabet = ' abcdefghijklmnopqrstuvwxyz'
def encode(string, a, b) :
    translation = []
    for char in string :
        translation.append(alphabet.index(char))
    i = 0
    while i < len(translation) :
        translation[i] = a * translation[i] + b
        i += 1
    return translation


def decode(numbers, a, b) :
    part_trans = []
    for num in numbers :
        simplified = (num - b) / a
        if (num - b) % a != 0 or simplified < 0 or simplified > 26 :
            return False
        part_trans.append(alphabet[int(simplified)])
    translation = ''.join(part_trans)
    return translation

def general_message_decode(num_list) :
    all_translations = []
    c = 1
    while c <= 100 :
        d = 0
        while d <= 100 :
            if decode(num_list, c , d) != False :
                all_translations.append(decode(num_list, c , d))
            d += 1
        c += 1
    return all_translations
        
general_message_translation = general_message_decode([377,717,71,513,105,921,581,547,547,105,377,717,241,71,105,547,71,377,547,717,751,683,785,513,241,547,751])

print('Encode test:')
print('Is {} the correct translation of {}'.format(encode('a cat', 2, 3), 'a cat'))
assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43], 'No, it is not the right translation'
print('Yes, it is the correct translation')
print('')

print('Decode test:')
print('Is {} the correct translation of {}'.format(decode([5, 3, 9, 5, 43], 2, 3), [5, 3, 9, 5, 43]))
assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat', 'No, it is not the right translation'
print('Yes, it is the correct translation')
print('')

print('Is {} the correct answer to {}'.format(decode([1, 3, 9, 5, 43], 2, 3),[1, 3, 9, 5, 43]))
assert decode([1, 3, 9, 5, 43], 2, 3) == False, 'No, it is not the right answer'
print('Yes it is the correct answer')
print('')

print('Is {} the correct answer to {}'.format(decode([5, 3, 9, 5, 44], 2, 3),[5, 3, 9, 5, 44]))
assert decode([5, 3, 9, 5, 44], 2, 3) == False, 'No, it is not the right answer'
print('Yes it is the correct answer')
print('')


print(general_message_translation[1])