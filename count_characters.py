def count_characters(string) :
    ed_string = string.casefold()
    new_dict = {}
    for char in ed_string :
        amount = 0
        for character in ed_string :
            if char == character :
                amount += 1
        new_dict[char] = amount
    return new_dict

print(count_characters('A cat!!!'))
