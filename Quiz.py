run_through_1 = False
run_through_2 = False
final_check = False
sorted_list_1 = []
sorted_list_2 = []
half_done = []
half_done_2 = []

def merge(x,y) : 
    ran = False
    x_index = 0
    y_index = 0
    merged_list = []
    while True :
        if x_index >= len(x) and y_index < len(y) :
            merged_list.append(y[y_index])
            y_index += 1
            ran = True
        elif y_index >= len(y) and x_index < len(x) :
            merged_list.append(x[x_index])
            x_index += 1
            ran = True
        elif x_index >= len(x) and y_index >= len(y) :
            return merged_list
        if not ran : 
            x_element = x[x_index]
            y_element = y[y_index]
            if x_element <= y_element :
                merged_list.append(x_element)
                x_index += 1
            elif y_element < x_element :
                merged_list.append(y_element)
                y_index += 1

def merge_sort(input_list):
    if len(input_list) > 1:
        halfway_index = round(len(input_list) / 2)
        left_half = input_list[:halfway_index]
        right_half = input_list[halfway_index:]
        sorted_left_half = merge_sort(left_half)
        sorted_right_half = merge_sort(right_half)
        return merge(sorted_left_half, sorted_right_half)
    else:
        return input_list


assert merge_sort([4,8,7,7,4,2,3,1]) == [1,2,3,4,4,7,7,8]
