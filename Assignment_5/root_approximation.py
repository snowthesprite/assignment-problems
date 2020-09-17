def update_bounds(bounds) :
    new_bounds = [[bounds[0],(bounds[0] + bounds[1]) / 2],[(bounds[0] + bounds[1]) / 2,bounds[1]]]
    for bound in new_bounds :
        if bound[0] ** 2 < 2 and bound[1] ** 2 > 2 :
            return bound

def estimate_root(precision, bound) :
    if bound[1] - bound[0] <= precision :
        return (bound[0] + bound[1]) / 2
    return estimate_root(precision, update_bounds(bound))

print('Is {} the correct updated bounds for [1, 2]'.format(update_bounds([1,2])))
assert update_bounds([1, 2]) == [1, 1.5], 'No, its not the correct updated bounds'
print('Yes, it was the correct updated bounds')
print('')

print('Is {} the correct updated bounds for [1, 1.5]'.format(update_bounds([1, 1.5])))
assert update_bounds([1, 1.5]) == [1.25, 1.5], 'No, its not the correct updated bounds'
print('Yes, it was the correct updated bounds')
print('')

print('Is {} a good estimate for the square root of 2?'.format(estimate_root(0.1,[1,2])))
assert estimate_root(0.1,[1,2]), 'No, its not a good estimate'
print('Yes, it was a good estimate')
print('')
