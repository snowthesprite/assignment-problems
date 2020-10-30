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

def merge_sort(given_list) :
    global run_through_1
    global run_through_2
    global final_check
    global sorted_list_1
    global sorted_list_2
    global half_done
    global half_done_2
    #yes I used globals sue me
    #actually dont
    #I like my grade
    #This is why I don't code off my meds
    length = len(given_list)
    a = []
    b = []
    if length > 1 :
        for element in range(length) :
            if element < (length / 2):
                a.append(given_list[element])
            elif element >= length / 2 :
                b.append(given_list[element])
    if len(a) == 1 and len(b) == 1:
        if not run_through_1 and not run_through_2 :
            sorted_list_1 = merge(a,b)
            run_through_1 = True
        elif run_through_1 and not run_through_2 :
            sorted_list_2 = merge(a,b)
            run_through_2 = True
        if run_through_1 and run_through_2 and not final_check :
            half_done = merge(sorted_list_1, sorted_list_2)
            run_through_1 = False
            run_through_2 = False
            final_check = True
        elif run_through_1 and run_through_2 and final_check :
            half_done_2 = merge(sorted_list_1,sorted_list_2)
            run_through_1 = False
            run_through_2 = False
            final_check = False
    if len(a) > 1 and len(b) > 1 :
        a = merge_sort(a)
        b = merge_sort(b)

    #Only works here? ¯\_(ツ)_/¯ 
    if not run_through_1 and not run_through_2 and not final_check :
        finished_list = merge(half_done,half_done_2)
        return finished_list