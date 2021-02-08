from magic_square import *

#arr = [[1,1,1], [None,None,None], [None,None,None]]

#print(is_valid(arr))
''''
print('Does is_valid work?')

arr1 = [[1,2,None],
           [None,3,None],
           [None,None,None]]

assert is_valid(arr1) == True, 'False where it should be True'

arr2 = [[1,2,None],
           [None,3,None],
           [None,None,4]]

assert is_valid(arr2) == False, 'True where it should be False'

arr3 = [[1,2,None],
           [None,3,None],
           [5,6,4]]

assert is_valid(arr3) == False, 'True where it should be False'

arr4 = [[None,None,None],
           [None,3,None],
           [5,6,4]]

assert is_valid(arr4) == True, 'False where it should be True'

print('Yes it does')

#make_arr()
'''