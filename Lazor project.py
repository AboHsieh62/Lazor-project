'''
This is the main function of the lazor project.
@author: Po-I Hsieh, Vina Ro

Calls all necessary codes for solving the Lazor puzzle.

**Called functions**
    bff_reader
        reads .bff file
    Lazor_tarck
        check if lazer intersects with all target positions
    Lazor_save
        saves a .png of the solution if a solution is found

**Classes**
    Block
'''
import bff_reader
import Lazor_tarck
import Lazor_save
import copy
import time
from sympy.utilities.iterables import multiset_permutations
from PIL import Image


def game_solver(filename):
    '''
    Takes a .bff file for a Lazor puzzle and solves it.
    Then creates a .png solution that shows where to put each block

    **Parameters**
        filename: *string*
            The .bff file that contains all the information.

    **Returns**
        None

    '''
    # Read all the needed data from the .bff file
    data = bff_reader.bff_reader(filename)
    board = data[0]
    [A, B, C] = data[1]
    laser_origin = data[2]
    targetPos = data[3]

    # Generates a list that puts all blocktypes on the grid
    block_loc = []
    for lines in board:
        for elements in lines:
            if elements == 'o':
                block_loc.append(elements)
    for i in range(A):
        block_loc[i] = 'A'
    for i in range(A, (A+B)):
        block_loc[i] = 'B'
    for i in range((A+B), (A+B+C)):
        block_loc[i] = 'C'

    # Generates all the possibilites of the board on board1
    combs = list(multiset_permutations(block_loc))
    length = len(board[0])
    width = len(board)

    SOLUTION_FOUND = False
    for possibility in combs:
        board1 = copy.deepcopy(board)
        for ll in range(length):
            for ww in range(width):
                if board1[ww][ll] == 'o':
                    board1[ww][ll] = possibility.pop(0)

        # Call function to check all possibilities of board1 and find solution
        if Lazor_tarck.lazor_target_track(board1, laser_origin, targetPos):
            print("Solution found.")
            # If the solution is found, save as a .png file
            Lazor_save.save_grid(board1, name="%s_solution.png" % filename)
            SOLUTION_FOUND = True
            break

    if not SOLUTION_FOUND:
        print("Solution not found.")


def unit_tests():
    '''
        This function serves as unit tests to test whether each function and
        class object in this script is running as expected.
        Error messages will be shown if any function returns incorrect results
    '''
    # Test 'bff_reader' function
    mad_1_test = bff_reader.bff_reader('mad_1.bff')
    assert (len(mad_1_test[0]) == 9), 'Error in reading grid'
    assert (mad_1_test[1] == [2, 0, 1]), 'Error in reading blockS'
    assert (mad_1_test[2][0][1] == (1, -1)), 'Error in reading laser'
    assert (mad_1_test[3][1] == (4, 3)), 'Error in reading intersect'

    # Test 'get_colors' function in Lazor_save.py
    color_test = Lazor_save.get_colors()
    assert (color_test['B'] == (0, 0, 0)), 'Error in get_colors()'

    # Test 'save_grid' function in Lazor_save.py
    Lazor_save.save_grid(mad_1_test[0], 'test')
    img_test = Image.open('test_solution.png')
    assert(img_test.getpixel((15, 15)) == (192, 192, 192)
           ), 'Error: save_grid does not save correct image'

    # Test 'Block' class by testing whether refractive block reflects laser
    block_test = Lazor_tarck.Block((1, 1), 'C')
    direction_test = block_test.contact((0, 1), (1, 1))
    assert(direction_test[1] == (-1, 1)
           ), 'Error: Block object does not return correct laser direction'

    # Test 'lazor_target_track' function in Lazor_tarck.py
    mad_1_test[0][5][1], mad_1_test[0][1][5], mad_1_test[0][3][7] = 'A', 'C', 'A'
    assert (Lazor_tarck.lazor_target_track(mad_1_test[0], mad_1_test[2], mad_1_test[3])), \
        'Error: board is not being correctly solved in lazor_target_track()'


if __name__ == "__main__":
    time_start = time.time()
    # unit_tests()

    lazor_file = 'mad_4.bff'
    # lazor_file = 'yarn_5.bff'
    # lazor_file = 'dark_1.bff'
    # lazor_file = 'mad_1.bff'
    # lazor_file = 'mad_7.bff'
    # lazor_file = 'numbered_6.bff'
    # lazor_file = 'tiny_5.bff'
    # lazor_file = 'showstopper_4.bff'

    game_solver(lazor_file)

    time_end = time.time()
    print('Total runtime(sec):', time_end-time_start)
