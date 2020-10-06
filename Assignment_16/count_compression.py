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

def count_decompression(compressed_string) :
    listed_string = []
    for count in compressed_string :
        for _ in range(count[1]) :
            listed_string.append(count[0])
    return ''.join(listed_string)
