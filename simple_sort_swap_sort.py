def minimum(list_numbers) :
    minimum_number = list_numbers[0]
    for number in list_numbers :
        if minimum_number > number :
            minimum_number = number
    return minimum_number


def simple_sort(num_list) : 
    sorted_elements = []
    length = len(num_list)
    i = 0
    while i < length :
        mini = minimum(num_list)
        sorted_elements.append(mini)
        num_list.remove(mini)
        i += 1
    return sorted_elements

def swap_sort(x) : 
    length = len(x)
    i = 0
    ran = False
    while i < length - 1 : 
        element_0 = x[i]
        element_1 = x[i + 1]
        if element_0 > element_1 :
            x[i] = element_1
            x[i + 1] = element_0
            ran = True
        i += 1
    if ran :
        return swap_sort(x)
    return x

print('Does simple sort properly sort the list of numbers?')
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], 'No it doesnt sort the elements'
print('Yes it does sort the elements')
print('')

print('Does swap sort properly sort the list of numbers?')
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], 'No it doesnt sort the elements'
print('Yes it does sort the elements')