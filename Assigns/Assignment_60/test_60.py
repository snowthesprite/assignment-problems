from hash_table import *

arr = [[], [], [], [], []]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(arr, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(arr, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value