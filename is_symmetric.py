def is_symmetric(string) :
    i = 0
    while i < len(string) :
        if string[i] != string[len(string)-(i+1)]:
            return False
        i += 1
    return True
