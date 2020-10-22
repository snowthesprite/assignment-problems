def merge(x,y) : 
    ran = False
    x_index = 0
    y_index = 0
    merged_list = []
    while True :
        if x_index >= len(x) and y_index > len(y) :
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