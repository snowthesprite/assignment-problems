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
    ran = False
    for i in range(len(x) - 1) : 
        element_0 = x[i]
        element_1 = x[i + 1]
        if element_0 > element_1 :
            x[i] = element_1
            x[i + 1] = element_0
            ran = True
    if ran :
        return swap_sort(x)
    return x
