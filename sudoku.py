import random
import sys

max_att = 120
difficulty_table = {
    'easy': random.randint(15,25),
    'medium': random.randint(26,36),
    'hard': random.randint(37,46),
}

def sudoku_generator(diff='easy'):
    '''Print a newly generated Sudoku Puzzle

    Args:
        diff: difficulty of puzzle: 'easy, 'medium', 'hard' (default 'easy')
    '''
    solved = solved_generator()
    remove_amount = get_difficulty(diff)
    remove_cells(solved, remove_amount)
    print solved

def solved_generator():
    '''Generate a valid and solved Sudoku Puzzle

    Returns:
        a list of nine lists that compose a completed Sudoku puzzle
    '''
    board = [['_' for row in xrange(9)] for col in xrange(9)]
    for row in xrange(9):
        for col in xrange(9):
            curr_row = board[row]
            curr_col = [board[col_value][col] for col_value in xrange(9)]
            box = generate_box_list(board, row, col)
            val = '_'
            tries = 0
            while in_peers(val, curr_row, curr_col, box):
                val = random.randint(1,9)
                tries += 1
                if tries > max_att:
                    return solved_generator()
            board[row][col] = val
    return board

def generate_box_list(board, cr, cc):
    '''Generates a list of current values in a current box

    Args:
        board: current Sudoku board
        cr: current row index
        cc: current column index
    Returns:
        a list of nine values
    '''
    b = []
    curr_box_row = int(cr/3)
    curr_box_col = int(cc/3)
    for box_row in xrange(3):
        for box_col in xrange(3):
            b.append(board[curr_box_row*3+box_row][curr_box_col*3+box_col])
    return b

def remove_cells(board, num_cells):
    '''Generates an unsolved Sudoku from a solved one

    Args:
        board: current Sudoku board
        num_cells: amount of cells to be removed from the puzzle
    Returns:
        a list of nine lists that compose an uncomplete Sudoku puzzle
    '''
    if num_cells != 0:
        rand_col = random.randint(0,8)
        rand_row = random.randint(0,8)
        if board[rand_row][rand_col] == '_':
            remove_cells(board, num_cells)
        else:
            board[rand_row][rand_col] = '_'
            remove_cells(board, num_cells-1)
    else:
        return board


def in_peers(v, cr, cc, sm):
    '''Checks if value v is in the current row, column, or appropriate box

    Args:
        v: value to be checked
        cr: current row index
        cc: current column index
        sm: current box (sub-matrix)
    '''
    return (v in cr or v in cc or v in sm)

def get_difficulty(d):
    '''Returns a difficulty value 

    Args:
        d: difficulty keyword to be looked up
    '''
    return difficulty_table[d] if difficulty_table.has_key(d) else 20

if __name__ == '__main__':
    if len(sys.argv) < 2:
        diff = 'easy'
    else:
        diff = sys.argv[1] 
    sudoku_generator(diff)
