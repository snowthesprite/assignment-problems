from card_sort import *
from shapes_2 import *


print()
sq = Square(5,'green')
print('Square desctiption')
sq.describe()
sq.render()
print()

tri = RightTriangle(5,2,'blue')
print('Triangle desctiption: ')
print()
tri.describe()
print()
tri.render()

rect = Rectangle(5,2,'red')
print('Rectangle desctiption: ')
print()
rect.describe()
print()
rect.render()


print('Does card_sort correctly sort the lists?')
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13], 'Did not sort [12, 11, 13, 5, 6] propperly'

assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [-3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7], 'Did not sort [5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1] propperly'

print('Yes it does!')