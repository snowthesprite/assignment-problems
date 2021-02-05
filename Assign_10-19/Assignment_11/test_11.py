from kl_divergence_for_monte_carlo_simulations import *

import math

p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]

print('Is {} the correct Kullback–Leibler divergence for the values of P and Q?'.format(round(kl_divergence(p,q), 6)))
assert round(kl_divergence(p,q), 6) == -0.096372, 'No it is not'
print('Yes it is')
print()

print('100 samples --> KL Divergence = {}'.format(MC_simulations(8,100)))
print()

print('1,000 samples --> KL Divergence = {}'.format(MC_simulations(8,1000)))
print()

print('10,000 samples --> KL Divergence = {}'.format(MC_simulations(8,10000)))
print()

print('As the number of samples increases, the KL divergence approaches 0 because as the number of tests increases, the accuracy of the MC simulations get more accurate, leading to a lower and lower divergence.')