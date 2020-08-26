def make_nested(dictionary):
    new_dictionary = {}
    for x in dictionary:
        classifiers = x.split('_')
        print(new_dictionary)
        new_dictionary.update({classifiers[0] : {classifiers[1] : dictionary[x]}})

    return new_dictionary

colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
  }

print(make_nested(colors))
