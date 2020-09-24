def tally_sort(num_list) :
    minimum = min(num_list)
    new_num_list = [num - minimum for num in num_list]
    maximum = max(new_num_list)
    tally = [0 for _ in range(maximum + 1)]
    for num in new_num_list :
        tally[num] += 1
    return tally
