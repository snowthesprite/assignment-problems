#def unlist_nonrecursive(x) :
    
def unlist_recursive(x) :
    for blank in range(len(x)) :
        for blank_2 in range(len(x)) : 
            if type(x[blank]) == int and type(x[-blank_2] == list :
                print('run')
                return x
    print(x)
    return unlist_recursive(x[0])

print(unlist_recursive([[[[1], [2,3], 4]]]))
print(unlist_recursive([[[[1]]]])) 

#assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]

#assert unlist_nonrecursive([[[[1]]]]) == 1

#assert unlist_recursive([[[[1], [2,3], 4]]]) == [([1], [2,3], 4)]

#assert unlist_recursive([[[[1]]]]) == 1