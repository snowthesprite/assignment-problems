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
    i = 0
    while i < len(numbers) :
        simplified.append((numbers[i] - b) / a)
        i += 1
    print(simplified)
    part_trans = []
    for num in simplified :
        part_trans.append(alphabet[num])
    translation = ''.join(emp_list)
    return translation


print(decode([5, 3, 9, 5, 43], 2, 3))