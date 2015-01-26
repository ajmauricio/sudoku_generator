from nose.tools import *
from sudoku import *

solved_sudoku = solved_generator()
valid = [1,2,3,4,5,6,7,8,9]
empty = [1,2,3,4,5,6,7,8,'_']

def test_amount_cells():
    assert_equal(81, sum([len(r) for r in solved_sudoku]))

def test_amount_rows():
    assert_equal(9,len(solved_sudoku))

def test_valid_columns():
    for row in xrange(9):
        for col in xrange(9):
            column = []
            for col_value in xrange(9):
                column.append(solved_sudoku[col_value][col])
            assert_equal(valid, sorted(column))

def test_valid_rows():
    for row in solved_sudoku:
        assert_equal(valid, sorted(row))

def test_valid_submatrices():
    for row in xrange(9):
        for col in xrange(9):
            curr_box_row = int(row/3)
            curr_box_col = int(col/3)
            box = []
            for box_row in xrange(3):
                for box_col in xrange(3):
                    box.append(solved_sudoku[curr_box_row*3+box_row][curr_box_col*3+box_col])
            assert_equal(valid, sorted(box))

def test_generate_box_list():
    for row in xrange(9):
        for col in xrange(9):
            b = generate_box_list(solved_sudoku, row, col)
            assert_equal(valid, sorted(b))

def test_in_peers():
    assert_equal(True, in_peers('_', empty, empty, empty))
    assert_equal(True, in_peers('_', empty, valid, empty))
    assert_equal(True, in_peers('_', empty, valid, valid))
    assert_equal(False, in_peers('_', valid, valid, valid))

def test_get_difficulty():
    assert get_difficulty('randomstring') == 20
    assert get_difficulty('easy') < 26 
    assert get_difficulty('easy') > 14
    assert get_difficulty('medium') < 37
    assert get_difficulty('medium') > 25
    assert get_difficulty('hard') < 47
    assert get_difficulty('hard') > 36

def test_remove_cells():
    assert_not_equal(solved_sudoku, remove_cells(solved_sudoku,20))