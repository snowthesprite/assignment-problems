import math
def calc_standard_normal_probability(a,b,n,rule) :
    funct = lambda x : math.pow(math.e, (-x**2)/2) / math.sqrt(2 * math.pi)
    step_size = (b - a) / n
    step = a
    prediction = 0
    step_number = 0
    if rule == "left endpoint" :
        while step_number < n :
            prediction += funct(step)
            step += step_size
            step_number += 1
        return prediction * step_size

    elif rule == "right endpoint" :
        step += step_size
        while step_number < n :
            prediction += funct(step) 
            step += step_size
            step_number += 1
        return prediction * step_size

    elif rule == "midpoint" :
        while step_number < n :
            step_2 = step + step_size
            prediction += funct((step + step_2)/2) 
            step += step_size
            step_number += 1
        return prediction * step_size 
    
    elif rule == "trapezoidal" :
        prediction += funct(step) * 0.5
        step += step_size
        while step < b :
            prediction += funct(step) 
            step += step_size
        prediction += funct(step) * 0.5
        return prediction * step_size
    
    elif rule == "simpson" :
        prediction += funct(step) 
        step += step_size
        while step < b :
            if step_number % 2 == 0 :
                coefficent = 2
            else :
                coefficent = 4
            prediction += funct(step) * coefficent
            step += step_size
            step_number += 1
        prediction += funct(step)
        return prediction * (step_size / 3)