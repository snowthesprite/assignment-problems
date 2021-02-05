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