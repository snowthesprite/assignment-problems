def card_sort(num_list) :
    sorted_num_list = []
    for num in num_list :
        i = 0
        run = False
        while i < len(sorted_num_list) :
            if num > sorted_num_list[i] and not run :
                sorted_num_list.insert(i + 1, num)
                run = True
            elif num < sorted_num_list[i] and not run :
                sorted_num_list.insert(i, num)
                run = True
            i += 1
        if sorted_num_list == [] or not run :
            sorted_num_list.append(num)
    return sorted_num_list