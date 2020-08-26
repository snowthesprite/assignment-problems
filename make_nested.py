def make_nested(dictionary):
    nest_dictionary = {}
    for x in dictionary:
        classifiers = x.split('_')
        if nest_dictionary.get(classifiers[0]) == None:
            nest_dictionary[classifiers[0]] = {}
        print(nest_dictionary)
        nest_dictionary[classifiers[0]].update({classifiers[1] : dictionary[x]})

    return nest_dictionary

colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
  }

print(make_nested(colors))
