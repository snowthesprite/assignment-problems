def zero_of_tangent_line(c) :
    #Func is f(x) = x^3 + x - 1
    y = c ** 3 + c - 1
    slope = (3 * c ** 2) + 1
    point = -(y - slope * c) / slope
    return point

def estimate_solution(precision) :
    point_2 = zero_of_tangent_line(0.5)
    while True :
        point_1 = zero_of_tangent_line(point_2)
        point_2 = zero_of_tangent_line(point_1)
        if point_1 - point_2 <= precision and point_2 - point_1 <= precision :
            return point_2
        