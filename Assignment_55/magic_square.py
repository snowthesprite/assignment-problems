def check_diagonals(arr) :
    sum = 0
    for index in range(3) :
        element = arr[index][index]
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
            if any(element in col for col in arr if arr[col_index] != col): 
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
    arr = [[None, None, None], [None, None, None], [None, None, None]]
    for row_index in range(3) :
        for col_index in range(3) :
            arr[row_index][col_index] = 1
            print(arr, "\n")
            test_arr = arr.copy()
            runs = 0
            while not is_valid(test_arr) :
                test_arr[row_index][col_index] += 1
                if test_arr[row_index][col_index] >= 10 :
                    runs += 1
                    test_arr = arr.copy()
                    test_arr[row_index][col_index - 1] += runs
            arr = test_arr
                