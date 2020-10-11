#exists because I'm lazy
import math

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

def most_accurate(dic_tests) :
    percentage = [0.0625, 0.25, 0.375, 0.25, 0.0625]
    kl_dict = {}
    for keys, values in dic_tests.items() : 
        heads_percentage = []
        all_tests = values.split(' ')
        for num_heads in range(5) :
            succeeded_tests = 0
            for test in all_tests :
                amount_of_heads = 0
                for outcome in test :
                    if outcome == 'H' :
                        amount_of_heads += 1
                if amount_of_heads == num_heads :
                    succeeded_tests += 1
            heads_percentage.append(succeeded_tests/20)
        return heads_percentage