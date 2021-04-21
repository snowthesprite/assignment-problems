import time as t

def solve_sudoku () :
    sudoku = reset('all')
    box_id = 0
    while box_id < 6 :
        box = sudoku[box_id]
        num_id = 0
        while None in box or not is_valid(sudoku, box_id, num_id) :
            if box[num_id] == None :
                box[num_id] = 1
            
            if is_valid(sudoku, box_id, num_id) :
                num_id += 1
                continue

            box[num_id] += 1

            if box[num_id] > len(box) :
                new_box = reset(box_id)
                #print(box, box[num_id])
                while new_box[num_id] != None or box[num_id] > 5 :
                    box[num_id] = new_box[num_id]
                    num_id -= 1
                    #print('num',box[num_id], num_id)
                    #print('orig',new_box[num_id], num_id)
                    print(box, new_box, '\n')
                #print('final',box[num_id])
                #t.sleep(1)
                box[num_id] += 1
        box_id += 1
        print(box, '\n')
    print(sudoku)
            

def is_valid (puzzle, box_id, num_id) :
    num = puzzle[box_id][num_id]
    box = [puzzle[box_id][id] for id in range(6) if id != num_id]
    col = find_column(puzzle,box_id,num_id)
    row = find_row(puzzle, box_id, num_id)
    print(num)
    if (num in box) or (num in col) or (num in row) :
        print('Box:',num in box, puzzle[box_id])
        print('Col:',num in col, col)
        print('Row:',num in row, row, '\n')
        t.sleep(3)
        return False
    print()
    return True
    
def find_column (puzzle, box_id, num_id) :
    alt_id = (num_id + 3) % 6
    column = []
    for id in range(0,6,2) :
        if id == box_id : 
            continue
        column.extend([puzzle[id][num_id], puzzle[id][alt_id]])
    return column

def find_row (puzzle, box_id, num_id) :
    if box_id % 2 == 0 :
        next_box = box_id + 1
    else :
        next_box = box_id - 1
    if num_id < 3 :
        alt_id = 0
    else :
        alt_id = 3
    return [puzzle[next_box][alt_id + next] for next in range(3)]

def reset (id) :
    #start = [[None,None,4,None,None,None],[None,None,None,2,3,None],[3,None,None,None,6,None],[None,6,None,None,None,2],[None,2,1,None,None,None],[None,None,None,5,None,None]]
    start = [[2,3,4,1,5,6],[None,None,None,2,3,None],[3,None,None,None,6,None],[None,6,None,None,None,2],[None,2,1,None,None,None],[None,None,None,5,None,None]]

    if id == 'all' :
        return start

    return start[id]