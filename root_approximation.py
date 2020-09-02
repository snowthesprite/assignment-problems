def update_bounds(bounds) :
    new_bounds = [[bounds[0],(bounds[0] + bounds[1]) / 2],[(bounds[0] + bounds[1]) / 2,bounds[1]]]
    for bound in new_bounds :
        if bound[0] ** 2 < 2 and bound[1] ** 2 > 2 :
            return bound

def estimate_root(precision, bound) :
    print(bound)
    if bound[1] - bound[0] <= precision :
        return (bound[0] + bound[1]) / 2
    return estimate_root(precision, update_bounds(bound))


