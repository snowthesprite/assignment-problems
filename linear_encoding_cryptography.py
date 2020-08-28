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
    simplified = []
    part_trans = []
    for num in numbers :
        simplified.append(int((num - b) / a))
    for intiger in simplified :
        part_trans.append(alphabet[intiger])
    translation = ''.join(part_trans)
    return translation


print(decode([5, 3, 9, 5, 43], 2, 3))