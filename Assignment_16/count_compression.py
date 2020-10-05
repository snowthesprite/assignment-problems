def count_compression(string) :
    count_list = []
    repeat = string[0]
    count = 0
    for letter in string :
        if repeat != letter :
            count_list.append((repeat, count))
            repeat = letter
            count = 0
        count += 1
    count_list.append((repeat, count))
    return count_list
