def estimate_x_derivative(f, point, delta) : 
    return (f((point[0] + 0.5 * delta), point[1]) - f((point[0] - 0.5 * delta), point[1])) / delta

def estimate_y_derivative(f, point, delta) : 
    return (f(point[0],( point[1] + 0.5 * delta)) - f(point[0], (point[1] - 0.5 * delta))) / delta

def gradient_descent(f, inital_point, alpha=0.01, delta=0.0001, iterations=10000) :
    current_point = [inital_point[0], inital_point[1], f(inital_point[0], inital_point[1])]
    base_iterations = 0
    while base_iterations <= iterations :
        f_x = estimate_x_derivative(f, current_point, delta)

        f_y = estimate_y_derivative(f, current_point, delta)

        current_point[0] = current_point[0] - alpha * f_x

        current_point[1] = current_point[1] - alpha * f_y

        current_point[2] = f(current_point[0], current_point[1])
        base_iterations += 1
    return current_point[2]