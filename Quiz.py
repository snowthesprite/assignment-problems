def counting_across_rows_matrix_elements(M,N) :
    return [[(M - row) * (N - col) for col in range(N)] for row in range(M)]

def return_7() : 
    return [num  for num in range(1001) if num % 7 == 0]

def if_3() :
    return [num for num in range(1001) for n in str(num) if n == '3']

def word_4(string) :
    return [word for word in string.split(' ') if len(word) < 4]
 
print(word_4('hey live hope fun funny nice'))

