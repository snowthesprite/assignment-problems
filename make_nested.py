def make_nested(dictionary):
    nest_dictionary = {}
    for x in dictionary:
        classifiers = x.split('_')
        if nest_dictionary.get(classifiers[0]) == None:
            nest_dictionary[classifiers[0]] = {}
        nest_dictionary[classifiers[0]].update({classifiers[1] : dictionary[x]})

    return nest_dictionary

colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
  }

#I'm not going to make it say the answer because the answer takes 3 lines and I don't wanna deal with that

print('Does the make_nested function properly nest the colors dictionary?')

assert make_nested(colors) == {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}, 'No it does not properly nest'

print('Yes it properly nests the colors dictionary')
print('')
