def estimate_derivative(f, c, delta) : 
    return (f((c + 0.5 * delta)) - f((c - 0.5 * delta))) / delta

def zero_of_tangent_line(f, c, delta) :
    y = f(c)
    slope = estimate_derivative(f, c, delta)
    point = -(y - slope * c) / slope
    return point

def estimate_solution(f, initial_guess, delta, precision) :
    point_2 = initial_guess
    while True :
        point_1 = zero_of_tangent_line(f, point_2, delta)
        point_2 = zero_of_tangent_line(f, point_1, delta)
        if point_1 - point_2 <= precision and point_2 - point_1 <= precision :
            return point_2