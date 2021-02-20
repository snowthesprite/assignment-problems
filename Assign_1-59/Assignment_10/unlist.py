def unlist_nonrecursive(x) :
    while True :
        if type(x) == int :
            return x
        for blank in range(len(x)) :
            for blank_2 in range(len(x)) : 
                if type(x[blank]) == int and type(x[-blank_2]) == list :
                    return x
        x = x[0]
    
def unlist_recursive(x) :
    if type(x) == int :
        return x
    for blank in range(len(x)) :
        for blank_2 in range(len(x)) : 
            if type(x[blank]) == int and type(x[-blank_2]) == list :
                return x
    return unlist_recursive(x[0])


assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]

assert unlist_nonrecursive([[[[1]]]]) == 1

assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]

assert unlist_recursive([[[[1]]]]) == 1