print('Does simple sort properly sort the list of numbers?')
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], 'No it doesnt sort the elements'
print('Yes it does sort the elements')
print('')

print('Does swap sort properly sort the list of numbers?')
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], 'No it doesnt sort the elements'
print('Yes it does sort the elements')