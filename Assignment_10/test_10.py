from unlist import unlist_nonrecursive, unlist_recursive

print('Nonrecursive Functions')
print()

print('Is {} the correct unnested version of [[[[1], [2,3], 4]]]?'.format(unlist_nonrecursive([[[[1], [2,3], 4]]])))
assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], 'No, it is not'
print('Yes, it is')
print()

print('Is {} the correct unnested version of [[[[1]]]]?'.format(unlist_nonrecursive([[[[1]]]])))
assert unlist_nonrecursive([[[[1]]]]) == 1, 'No, it is not'
print('Yes, it is')
print()

print('Recursive Functions')
print()

print('Is {} the correct unnested version of [[[[1], [2,3], 4]]]?'.format(unlist_recursive([[[[1], [2,3], 4]]])))
assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], 'No, it is not'
print('Yes, it is')
print()


print('Is {} the correct unnested version of [[[[1]]]]?'.format(unlist_recursive([[[[1]]]])))
assert unlist_recursive([[[[1]]]]) == 1, 'No, it is not'
print('Yes, it is')
print()
