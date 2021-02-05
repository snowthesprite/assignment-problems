from cartesian_product import *

arrays = [['a'], [1,2,3], ['Y','Z']]

print('Does the cartesian_product work?')
assert cartesian_product(arrays) == [['a',1,'Y'], ['a',2,'Y'], ['a',3,'Y'], ['a',1,'Z'], ['a',2,'Z'], ['a',3,'Z']], 'No, the cartesian_product does not work'
print('Yes, it does!')
print()