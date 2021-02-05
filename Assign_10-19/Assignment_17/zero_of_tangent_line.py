def zero_of_tangent_line(c) :
    #Func is f(x) = x^3 + x - 1
    #y = c ** 3 + c - 1
    #slope = (3 * c ** 2) + 1
    y = c ** 2 - 2
    slope = (2 * c)
    point = -(y - slope * c) / slope
    return point

def estimate_solution(precision) :
    point_2 = zero_of_tangent_line(1f())
    while True :
        print(point_2)
        point_1 = zero_of_tangent_line(point_2)
        print(point_1)
        point_2 = zero_of_tangent_line(point_1)
        if point_1 - point_2 <= precision and point_2 - point_1 <= precision :
            return point_2
        