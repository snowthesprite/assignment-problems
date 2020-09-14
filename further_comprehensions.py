def identity_matrix_elements(n) :
    return [[(1 if col == row else 0)  for col in range(0,n)] for row in range(0,n)]

def counting_across_rows_matrix_elements(m,n) :
    return [[(1 + col + row )  for col in range(0,n)] for row in range(0,m*n,n)]

assert identity_matrix_elements(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

assert counting_across_rows_matrix_elements(3,4) == [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]