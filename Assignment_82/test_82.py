from sudoku_solver import *

finished_sudoku = solve_sudoku()

print('-----------------')
for index in range(0,6,2) :
    s_1 = finished_sudoku[index]
    s_2 = finished_sudoku[index + 1]
    for h in range(0,6,3) :
        print('| {} {} {} | {} {} {} |'.format(s_1[h],s_1[h+1],s_1[h+2],s_2[h],s_2[h+1],s_2[h+2]))
    print('-----------------')
