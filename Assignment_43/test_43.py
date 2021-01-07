from random_draw import *

test_1 = [0.5, 0.5]
test_2 = [0.25, 0.25, 0.5]
test_3 = [0.05, 0.2, 0.15, 0.3, 0.1, 0.2]
repititions = 1000

print('Expected value for {} is 0.5'.format(test_1))

average_value = 0
passes = 0
while passes < repititions :
    average_value += random_draw(test_1)
    passes += 1
average_value = average_value/repititions

print('Calcuted value for {} is {}'.format(test_1, average_value))
print()

print('Expected value for {} is 1.25'.format(test_2))

average_value = 0
passes = 0
while passes < repititions :
    average_value += random_draw(test_2)
    passes += 1
average_value = average_value/repititions

print('Calcuted value for {} is {}'.format(test_2, average_value))
print()

print('Expected value for {} is 2.8'.format(test_3))

average_value = 0
passes = 0
while passes < repititions :
    average_value += random_draw(test_3)
    passes += 1
average_value = average_value/repititions

print('Calcuted value for {} is {}'.format(test_3, average_value))
print()
