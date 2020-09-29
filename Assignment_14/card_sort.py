def card_sort(num_list) :
    sorted_num_list = []
    for num in num_list :
        #print('ran')
        i = 0
        run = False
        while i < (len(sorted_num_list) - 1) :
            if num > sorted_num_list[i] and num < sorted_num_list[i + 1] :
                sorted_num_list.insert(i + 1, num)
                run = True
            i += 1
        if sorted_num_list == [] or not run :
            sorted_num_list.append(num)
    return sorted_num_list