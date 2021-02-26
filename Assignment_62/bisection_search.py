def bisection_search(entry, sorted_list) :
    lowest_index = 0
    highest_index = len(sorted_list) - 1
    while True :
        midpoint = round((lowest_index + highest_index) / 2)
        checkpoint = sorted_list[midpoint]
        if checkpoint > entry : 
            highest_index = midpoint - 1
        elif checkpoint < entry :
            lowest_index = midpoint + 1
        else :
            return midpoint