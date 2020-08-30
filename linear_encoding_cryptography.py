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

def fancy_decode(num_list) :
    all_translations = []
    a = 1
    b = 0
    while a <= 100 :
        while b <= 100 :
            all_translations.append(decode(num_list,a,b))
            b += 1
        a += 1
    return all_translations
        


print(decode([1, 3, 9, 5, 43], 1, 3))