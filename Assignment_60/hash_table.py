def hash_function(string) :
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sum = 0
    for char in string :
        sum += alphabet.index(char)
    return sum % 5

def insert(arr, key, value) :
    index = hash_function(key)
    arr[index].append((key, value))

def find(arr, key) :
    index = hash_function(key)
    for pair in arr[index] :
        if pair[0] == key :
            return pair[1]