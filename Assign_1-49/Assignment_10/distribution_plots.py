from random import random
from Assignment_7.monte_carlo_coin_flips import monte_carlo_probability, probability, find_factorial

import matplotlib.pyplot as plt

plt.style.use('bmh')
plt.plot([heads for heads in range(9)],[probability(heads, 8) for heads in range(9)],linewidth=2.5)
plt.plot([heads for heads in range(9)], [monte_carlo_probability(heads, 8) for heads in range(9)],linewidth=0.75)
plt.plot([heads for heads in range(9)], [monte_carlo_probability(heads, 8) for heads in range(9)],linewidth=0.75)
plt.plot([heads for heads in range(9)], [monte_carlo_probability(heads, 8) for heads in range(9)],linewidth=0.75)
plt.plot([heads for heads in range(9)], [monte_carlo_probability(heads, 8) for heads in range(9)],linewidth=0.75)
plt.plot([heads for heads in range(9)], [monte_carlo_probability(heads, 8) for heads in range(9)],linewidth=0.75)
plt.legend(['True','MC 1','MC 2','MC 3','MC 4','MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 4 Coin Flips')
plt.savefig('plot.png')
