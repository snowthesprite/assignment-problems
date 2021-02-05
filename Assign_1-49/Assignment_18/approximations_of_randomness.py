#exists because I'm lazy: from here
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

def percentage_of_value(sample) :
    percentage = []
    all_tests = sample.split(' ')
    for num_heads in range(5) :
        succeeded_tests = 0
        for test in all_tests :
            amount_of_heads = 0
            for outcome in test :
                if outcome == 'H' :
                    amount_of_heads += 1
            if amount_of_heads == num_heads :
                succeeded_tests += 1
        percentage.append(succeeded_tests/20)
    return percentage

#to here

def most_accurate(dic_tests) :
    percentage = [0.0625, 0.25, 0.375, 0.25, 0.0625]
    kl_dict = {}
    for keys, values in dic_tests.items() :
        kl_dict[keys] = kl_divergence(percentage_of_value(values), percentage)
    sorted_ppl = []
    for keys in kl_dict :
        i = 0
        run = False
        while i < len(sorted_ppl)  :
            if kl_dict.get(keys) <= kl_dict.get(sorted_ppl[i]) and not run :
                sorted_ppl.insert(i, keys)
                run = True
            i += 1
        if sorted_ppl == [] or not run :
            sorted_ppl.append(keys)
    return sorted_ppl