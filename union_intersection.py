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

test_list_1 = [1,2,'a','b']
test_list_2 = [2,3,'a']

print('Is the intersection of {} and {} equal to {}'.format(test_list_1,test_list_2,intersection(test_list_1,test_list_2)))
assert intersection(test_list_1,test_list_2) == [2,'a'], 'The intersection was wrong'
print('Yes')

print('')

print('Is the union of {} and {} equal to {}'.format(test_list_1,test_list_2,union(test_list_1,test_list_2)))
assert union([1,2,'a','b'], [2,3,'a']) == [1,2,'a','b',3], 'The union was wrong'
print('Yes')

print('')
