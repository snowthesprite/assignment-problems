def estimate_derivative(f, c, delta) : 
    return (f((c + 0.5 * delta)) - f((c - 0.5 * delta))) / delta

def gradient_descent(f,x0,alpha=0.01,delta=0.0001,iterations=10000) :
    point = f(x0)
    base_iterations = 0
    while base_iterations >= iterations :
        f_prime = estimate_derivative(f, point, delta)
        point = point - alpha * f_prime
        base_iterations += 1
    return point