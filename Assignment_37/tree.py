def get_children(parent, tree_list) :
    children = []
    for pair in tree_list: 
        if pair[0] == parent :
            children.append(pair[1])
    return children

def get_parents(child, tree_list) :
    parents = []
    for pair in tree_list :
        if pair[1] == child :
            parents.append(pair[0])
    return parents

def get_root(tree_list) :
    for pair in tree_list :
        for parent_child in pair :
            check = get_parents(parent_child, tree_list)
            if check == [] :
                return list(parent_child)