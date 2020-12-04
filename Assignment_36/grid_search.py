def cartesian_product(arrays) :
    points = [[]]
    for arr in arrays :
        new_points = []
        for element in arr :
            for index in range(len(points)) :
                new_point = points[index].copy()
                new_point.append(element)
                new_points.append(new_point)
        points = new_points
    return points

def grid_search(objective_function, grid_lines) :
    intersect_points = cartesian_product(grid_lines)
    lowest_points = intersect_points[0]
    lowest_value = objective_function(*intersect_points[0])
    for point in intersect_points :
        value = objective_function(*point)
        if lowest_value > value :
            lowest_value = value
            lowest_points = point
    return lowest_points