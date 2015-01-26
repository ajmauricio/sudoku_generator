Installation
============

To perform the accompanying UnitTests requires `nose`, as seen in [LearnPythonTheHardway](http://learnpythonthehardway.org/book/).

You may install `nose` using `easy_install nose` or `pip install nose`.

No other dependencies are required.

Running the Program
===================

To generate a new Sudoku, cd into the appropriate directory and run `sudoku.py` by typing `python sudoku.py difficulty`. `difficulty` may be replaced with either `easy`, `medium`, or `hard`. If no argument for difficulty is provided, the program defaults to `easy`.

Tests
=====

UnitTests can be run by cd'ing into the appropriate
directory and running `nosetests`.

Known Issues
============

None at this time


Areas for Improvement
=====================

The algorithm generates new, solved Sudokus very quickly. This was my primary goal in this project. Once I attained a solved Sudoku, it would be very easy to generate an unsolved one by removing different amounts of cells. I believed that this would be faster than generating a random Sudoku and attempting to solve it.

The algorithm to generate new Sudokus could definitely be improved upon, given more time. Specifically, the `solved_generator()` function could be implemented more efficiently by keeping track of which numbers are already in use in each column, row, and box. At the moment, the algorithm randomly chooses an integer between 1 and 9, disregarding already placed numbers.

The algorithm also does not ensure a unique solution. This is the first area I would like to enhance to ensure that each sudoku puzzle only has one unique solution. At the moment, this is not implemented.