alphabet = ' abcdefghijklmnopqrstuvwxyz'
def encode(string, a, b) :
    translation = []
    for char in string :
        translation.append(alphabet.index(char))
    i = 0
    while i < len(translation) :
        translation[i] = a(translation[i]) + b
        i += 1
    return translation


#def decode(numbers, a, b) :


print(encode('a cat', 2, 3))