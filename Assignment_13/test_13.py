import sys
sys.path.append('Assignment_12')
from shapes import *
import matplotlib.pyplot as plt
from detecting_biased_coins import *
sys.path.append('Assignment_7')
from monte_carlo_coin_flips import *


print()
sq = Square(5,'green')
sq.describe()
sq.render()
print()

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

plt.style.use('bmh')
plt.plot([heads for heads in range(4)], [probability(heads,3) for heads in range(4)])
plt.plot([heads for heads in range(4)], finding_probability(coin_1))
plt.plot([heads for heads in range(4)], finding_probability(coin_2))
plt.plot([heads for heads in range(4)], finding_probability(coin_3))
plt.legend(['True','Coin 1','Coin 2','Coin 3'])
plt.savefig('Assignment_13/plot.png')

print('Coin 1 is biased towards Tails')
print()
print('Coin 2 is pretty fair')
print()
print('Coin 3 is biased twoards Heads')