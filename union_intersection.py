def intersection(list_1,list_2) :
    new_list = []
    for unit_1 in list_1 :
        for unit_2 in list_2 :
            if unit_1 == unit_2 :
                new_list.append(unit_1)
    return new_list


def union(list_3,list_4) :
    newer_list = []
    if len(list_3) >= len(list_4) :
        length = len(list_3)
        small_length = len(list_4)
    else :
        length = len(list_4)
        small_length = len(list_3)
    i = 0 
    while i < length :
        newer_list.append(list_3[i])
        newer_list.append(list_4[i])
        i += 1
    return newer_list

assert union([1,2,'a','b'], [2,3,'a']) == [1,2,3,'a','b']
print('PASSED')