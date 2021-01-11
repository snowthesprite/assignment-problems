import math
def calc_standard_normal_probability(a,b) :
    funct = lambda x : math.e^(-x^2/2) / math.sqrt(2 * math.pi)
    step_size = 0.001
    step = a
    prediction = 0
    while step < b :
        prediction += funct(step)
        step += step_size
    return prediction
