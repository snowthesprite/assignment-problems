def estimate_derivative(f, c, delta) : 
    return (f((c + 0.5 * delta)) - f((c - 0.5 * delta))) / delta

def zero_of_tangent_line(f, c) :
    #Func is f(x) = x^3 + x - 1
    y = f(c)
    slope = estimate_derivative(f, c)
    point = -(y - slope * c) / slope
    return point

def estimate_solution(precision) :
    point_2 = zero_of_tangent_line(0.5)
    while True :
        point_1 = zero_of_tangent_line(point_2)
        point_2 = zero_of_tangent_line(point_1)
        if point_1 - point_2 <= precision and point_2 - point_1 <= precision :
            return point_2