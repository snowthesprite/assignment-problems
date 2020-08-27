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

print(flatten(colors))