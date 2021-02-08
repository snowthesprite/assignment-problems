def check_diagonals(arr) :
    sum = 0
    for index in range(3) :
        element = arr[index][index]
        if element == None :
            return True
        sum += element
    if sum != 15 :
        return False
    sum = 0
    for index in reversed(range(3)) :
        element = arr[2 - index][index]
        if element == None :
            return True
        sum += element
    return sum == 15

def check_rows(arr) :
    for row_index in range(3) :
        sum = 0
        for col_index in range(3) :
            element = arr[row_index][col_index]
            if element == None :
                return True
            if any(element in row for row in arr if arr[row_index] != row) : 
                return False
            sum += element
        if sum != 15 :
            return False
    return True

def check_cols(arr) :
    for col_index in range(3) :
        sum = 0
        for row_index in range(3) :
            element = arr[row_index][col_index]
            if element == None :
                return True
            if any(element in col for col in [[arr[x][col] for x in range(3)] for col in range(3) if col != col_index]): 
                return False
            sum += element
        if sum != 15 :
            return False
    return True
            
            
def is_valid(arr) :
    diags = check_diagonals(arr)
    rows = check_rows(arr)
    cols = check_cols(arr)
    #print(diags, rows, cols)
    if diags and rows and cols :
        return True
    return False

def make_arr() :
    arr = [[None for _ in range(3)] for __ in range(3)]
    for num1 in range(1,10):
        arr[0][0] = num1
        #print(arr)
        if not is_valid(arr):
            continue
        for num2 in range(1,10): 
            arr[0][1] = num2
            #print(arr)
            if not is_valid(arr):
                arr[0][1] = None
                arr[0][2] = None
                continue
            for num3 in range(1,10):
                arr[0][2] = num3
                #print(arr)
                if not is_valid(arr):
                    arr[0][2] = None
                    arr[1][0] = None
                    continue
                for num4 in range(1,10):
                    arr[1][0] = num4
                    #print(arr)
                    if not is_valid(arr):
                        arr[1][0] = None
                        arr[1][1] = None
                        continue
                    for num5 in range(1,10):
                        arr[1][1] = num5
                        #print(arr)
                        if not is_valid(arr):
                            arr[1][1] = None
                            arr[1][2] = None
                            continue
                        for num6 in range(1,10):
                            arr[1][2] = num6
                            #print(arr)
                            if not is_valid(arr):
                                arr[1][2] = None
                                arr[2][0] = None
                                continue
                            for num7 in range(1,10):
                                arr[2][0] = num7
                                #print(arr)
                                if not is_valid(arr):
                                    arr[2][0] = None
                                    arr[2][1] = None
                                    continue
                                for num8 in range(1,10):
                                    arr[2][1] = num8
                                    #print(arr)
                                    if not is_valid(arr):
                                        arr[2][1] = None
                                        arr[2][2] = None
                                        continue
                                    for num9 in range(1,10):
                                        arr[2][2] = num9
                                        #print(arr)
                                        if not is_valid(arr):
                                            arr[2][2] = None
                                            continue
                                        return arr
                

''''
def make_arr() :
    arr = [[None for _ in range(3)] for __ in range(3)]
    row_index = 0
    col_index = 0
    restarts = 0
    while row_index < 3 :
        col_index = 0
        print(arr)
        while col_index < 3 :
            arr[row_index][col_index] = 1 
            arr[0][0] = 1 + restarts
            test_arr = [[x for x in arr[_]] for _ in range(3)]
            runs = 0
            while not is_valid(test_arr) :
                test_arr[row_index][col_index] += 1
                if test_arr[row_index][0] >= 10 :
                    test_arr = [[None for _ in range(3)] for __ in range(3)]
                    restarts += 1
                    row_index = 0
                    col_index = 0
                    break
                if test_arr[row_index][col_index] >= 10 :
                    runs += 1
                    test_arr = [[x for x in arr[_]] for _ in range(3)]
                    test_arr[row_index][col_index - 1] += runs
            col_index += 1
            arr = test_arr
        row_index += 1
    print(row_index, col_index)
    return arr
save for a possible later
'''