def intersection(list_1,list_2) :
    new_list = []
    for unit_1 in list_1 :
        for unit_2 in list_2 :
            if unit_1 == unit_2 :
                new_list.append(unit_1)
    return new_list


def union(list_3,list_4) :
    emp_list = list_3
    for unit_4 in list_4 :
        if unit_4 not in emp_list :
            emp_list.append(unit_4)
    return emp_list

print(union([1,2,'a','b'],[2,3,'a']))
#assert union([1,2,'a','b'], [2,3,'a']) == [1,2,3,'a','b']
