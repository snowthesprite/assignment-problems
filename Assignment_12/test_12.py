from tally_sort import *
from shapes import *

print()
print('Did tally_sort correctly sort the given list?')
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8], 'No it did not'
print('Yes, it did')
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
