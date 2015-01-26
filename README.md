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

The algorithm to generate new Sudokus could be improved upon, given more time. Specifically, the `solved_generator()` function could be implemented more efficiently by keeping track of which numbers it has already tried.