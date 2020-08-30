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
        print(simplified)
        if (num - b) % a != 0 or simplified < 0 or simplified > 26 :
            return False
        part_trans.append(alphabet[int(simplified)])
    translation = ''.join(part_trans)
    return translation

def fancy_decode(num_list) :
    all_translations = []
    c = 1
    d = 0
    while c <= 5 :
        while d <= 5 :
            if decode(num_list, c , d) != False :
                all_translations.append(decode(num_list, c , d))
            d += 1
        c += 1
    return all_translations
        


#print(fancy_decode([377,717,71,513,105,921,581,547,547,105,377,717,241,71,105,547,71,377,547,717,751,683,785,513,241,547,751],))
print(fancy_decode([5, 3, 9, 5, 43]))