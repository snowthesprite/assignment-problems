a_repet = 0
b_repet = 0
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
    global a_repet
    global b_repet
    a_ran = False
    b_ran = False
    length = len(given_list)
    a = []
    b = []
    if length > 1 :
        for element in range(length) :
            if element < (length / 2):
                a.append(given_list[element])
            elif element >= length / 2 :
                b.append(given_list[element])
        print(a_repet, b_repet)
        print(a, b)
        print('len', len(a), len(b))
    if len(a) > 1 and len(b) > 1 :
        a_repet += 1
        a_list = [merge_sort(a)]
        print('ran')
        print(1, a, b)
        #sorted_list_a = merge(a,b)
        #print('a', sorted_list_a)
        b_repet += 1
        b_list = [merge_sort(b)]
        #print(a_list, b_list)
    '''
    if len(a) > 1 :
        coward1 = merge_sort(a)
        a_ran = True
    if a_ran :
        print('ran1')
        sorted_list_a = merge(a,b)
        print(sorted_list_a)
    if len(b) > 1 :
        coward2 = merge_sort(b)
    if b_ran :
        print('ran2')
        sorted_list_b = merge(a,b)
        print(sorted_list_b)
    #'''
    '''
    if len(a) > 1 and len(b) > 1 :
        a_repet += 1
        a_list = [merge_sort(a)]
        b_repet += 1
        b_list = [merge_sort(b)]
        #print(a_list, b_list)
    #'''