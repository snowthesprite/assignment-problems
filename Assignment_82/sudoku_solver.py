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
                num_id = (num_id + 1) % 6
                continue

            box[num_id] += 1

            if box[num_id] > len(box) :
                new_box = reset(box_id)
                while new_box[num_id] != None or box[num_id] > 5 :
                    box[num_id] = new_box[num_id]
                    num_id -= 1
                box[num_id] += 1
        box_id += 1
    return sudoku
            
def is_valid (puzzle, box_id, num_id) :
    num = puzzle[box_id][num_id]
    box = [puzzle[box_id][id] for id in range(6) if id != num_id]
    col = find_column(puzzle,box_id,num_id)
    row = find_row(puzzle, box_id, num_id)
    if (num in box) or (num in col) or (num in row) :
        return False
    return True
    
def find_column (puzzle, box_id, num_id) :
    start= box_id % 2
    alt_id = (num_id + 3) % 6
    column = []
    for id in range(start,6,2) :
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
    start = [[None,None,4,None,None,None],[None,None,None,2,3,None],[3,None,None,None,6,None],[None,6,None,None,None,2],[None,2,1,None,None,None],[None,None,None,5,None,None]]

    if id == 'all' :
        return start

    return start[id]