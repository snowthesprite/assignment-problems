def minimum(list_numbers) :
    minimum_number = list_numbers[0]
    for number in list_numbers :
        if minimum_number > number :
            minimum_number = number
    return minimum_number


def simple_sort(num_list) : 
    sorted_elements = []
    length = len(num_list)
    print(length)
    i = 0
    while i < length :
        print('run')
        mini = minimum(num_list)
        sorted_elements.append(mini)
        num_list.remove(mini)
        i += 1
    return sorted_elements

def swap_sort(x) : 
    length = len(X)
    i = 0
    sorted_elements = []
    ran = False
    while i < length - 1 : 
        element_0 = x[i]
        element_1 = x[i + 1]
        if element_0 > element_1 :
            sorted_elements.append(element_1)
            x[i] = element_1
            x[i + 1] = element_0
            ran = True
        elif element_0 <= element_1 :
            sorted_elements.append(element_0)
        i += 1
    if ran :
        return swap_sort(sorted_elements)
    return sorted_elements



print(simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]))