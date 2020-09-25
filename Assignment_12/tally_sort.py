def minimum(list_numbers) :
    minimum_number = list_numbers[0]
    for number in list_numbers :
        if minimum_number > number :
            minimum_number = number
    return minimum_number

def maximum(list_numbers) :
    maximum_number = list_numbers[0]
    for number in list_numbers :
        if maximum_number < number :
            maximum_number = number
    return maximum_number

def tally_sort(num_list) :
    mini = minimum(num_list)
    new_num_list = [num - mini for num in num_list]
    maxi = maximum(new_num_list)
    tally = [0 for _ in range(maxi + 1)]
    for num in new_num_list :
        tally[num] += 1
    sorted_list = []
    for num in tally :
        for _ in range(num) : 
            sorted_list.append(tally.index(num) + mini)
        tally[tally.index(num)] = False
    
    return sorted_list