import random
def random_draw(distribution) :
    cumulative_distribution = [distribution[0]] 
    index = 1
    while index < len(distribution) :
        next_element = cumulative_distribution[index - 1] + distribution[index]
        cumulative_distribution.append(next_element)
        index += 1
    random_number = random.random()
    index = 0
    while index < len(cumulative_distribution) :
        if cumulative_distribution[index] > random_number :
            return index
        index += 1