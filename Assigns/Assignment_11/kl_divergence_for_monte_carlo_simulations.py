import math
import sys
sys.path.append('Assignment_7')
from monte_carlo_coin_flips import *

def kl_divergence(p, q) : 
    sum_p_q = 0
    for element in range(len(p)) :
        p_element = p[element]
        q_element = q[element]
        if p_element != 0 and q_element != 0 :
            logarithm = math.log(p_element/q_element)
            divergence = p_element * logarithm
            sum_p_q += divergence
    return sum_p_q

def MC_simulations(head_amount, test_amount) :
    MC_sim = []
    true_distribution = []
    for heads in range(head_amount + 1) :
        MC_sim.append(monte_carlo_probability(head_amount, 8, test_amount))
        true_distribution.append(probability(head_amount, 8))
    return kl_divergence(MC_sim, true_distribution)