def count_characters(string) :
    lowercase_string = string.casefold()
    count_dict = {}
    for char in lowercase_string :
        amount = 0
        for character in lowercase_string :
            if char == character :
                amount += 1
        count_dict[char] = amount
    return count_dict

test_str = 'A cat!!!'

print('is {} the right amount of each character for "{}"?'.format(count_characters(test_str),test_str))
assert count_characters(test_str) == {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}, 'No it is not the right amount of each character'
print('Yes')

print('')
