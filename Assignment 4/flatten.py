def flatten(dictionary):
    flat_dict = {}
    for keys_1 in dictionary:
        for keys_2 in dictionary[keys_1]:
            new_name = keys_1 + '_' + keys_2
            flat_dict[new_name] = dictionary[keys_1][keys_2]

    return flat_dict

colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

print('Does the flatten() function properly flatten the colors dictionary?')
assert flatten(colors) == {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}, 'No, flatten() did not properly flatten colors'
print('Yes, flatten did properlt flatten colors')

print('')