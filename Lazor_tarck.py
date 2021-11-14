"""
Includes functions and class to define the path of
the lazer and find the solution.
@author: Po-I Hsieh, Vina Ro
"""


class Block:
    '''
    An object that defines a block in the board
    The block can be
        'x'--empty(no blocks can be put on)
        'o'--empty(positions for potential blocks)
        'A'--reflective block
        'B'--opaque block
        'C'--refractive block
    '''

    def __init__(self, coordinate, blktype):
        '''
        This function initializes the block object

        **Parameters**
            coordinate: *tuple, int*
                The (x, y) coordinates of the block

            blktype: *string*
                The type of the block
        '''
        self.coordinate = coordinate
        self.blktype = blktype

    def contact(self, contactpos, lazor_dir):
        '''
        Updates the new direction of the laser when it contact with a block

        **Parameters**
            self: *object*
                This block object instance

            contactpos: *tuple of 2 int*
                The coordinates of where laser hits a block

            lazor_dir: *tuple of 2 int*
                The direction in which the laser is currently going

        **Returns**
            new_dir: *list*
                A list of new directions
        '''
        # If x coordinate is odd, the laser will be in contact with
        # the top or bottom block, thus changing the y-direction
        if contactpos[0] % 2 == 1:
            if self.blktype == 'A':
                new_dir = [(lazor_dir[0], lazor_dir[1] * -1)]
            elif self.blktype == 'B':
                new_dir = []
            elif self.blktype == 'C':
                new_dir = [lazor_dir, (lazor_dir[0], lazor_dir[1] * -1)]

        # If x coordinate is even, the laser will be in contact with
        # the left or right block, thus changing the x-direction
        elif contactpos[0] % 2 == 0:
            if self.blktype == 'A':
                new_dir = [(lazor_dir[0] * -1, lazor_dir[1])]
            elif self.blktype == 'B':
                new_dir = []
            elif self.blktype == 'C':
                new_dir = [lazor_dir, (lazor_dir[0] * -1, lazor_dir[1])]
        return new_dir


def pos_chk(length, width, lazer_pos):
    '''
    This function checks whether a given laser position is within the board.

    **Parameters**
        length: *integer*
            length of the board

        width: *integer*
            width of the board

        lazer_pos: *tuple*
            (x, y) coordinates of the current lazer position being checked

    **Return**
        *boolean*
            True if not within board and False if out of the board
    '''
    return lazer_pos[0] >= 0 and lazer_pos[0] < length and lazer_pos[1] >= 0 and lazer_pos[1] < width


def lazor_target_track(board, lazor_source, intersects):
    '''
    Takes a board and runs lasers from given lazer positions and directions
    through the Lazor board, tracking each laser's position as it goes and
    checking if all required target positions have been intersected by a laser.

    **Parameters**
        board: *list, list, string*
            contains list of x coordinates,
            in each list is a list of y coordinates
            containing a string representing the type of block on the board

        laser_source: *list, list, tuple, int*
            A list containing 2 sets of tuples that each contain 2 integers
            The first tuple is the laser's starting (x, y) coordinates
            The second tuple is the laser's initial direction

        intersects: **list, tuple, int*
            A list of tuples which each have two integers, which are a required
            intersections (x, y) coordinates

    **Returns**
        *boolean*
            True if all interesects are included in saved laser positions
            False if not
    '''
    lazor_pos = []
    lazor_ls = []
    # Create a list to store all laser sources
    lazor_ls.extend(lazor_source)
    grid_len = len(board[0])
    grid_height = len(board)
    check = False

    for lazer in lazor_ls:
        trace = []
        lazor_pos.append(lazer[0])
        x = lazer[0][0]
        y = lazer[0][1]
        dir_x = lazer[1][0]
        dir_y = lazer[1][1]
        # If the next laser position is in the grid do the below calculation
        while pos_chk(grid_len, grid_height, (x + dir_x, y + dir_y)):
            # Check if there is any block that will interact with the laser
            # and do the corresponding direction change
            if board[y][x + dir_x] == 'A' or board[y + dir_y][x] == 'A':
                block = Block((x, y), 'A')
                new_dir = block.contact((x, y), lazer[1])
                for xy in new_dir:
                    # Check if the new laser source already exists
                    # in case an infinite loop happens
                    if [(x, y), xy] not in lazor_ls:
                        lazor_ls.append([(x, y), xy])
                break
            elif board[y][x + dir_x] == 'B' or board[y + dir_y][x] == 'B':
                block = Block((x, y), 'B')
                new_dir = block.contact((x, y), lazer[1])
                for xy in new_dir:
                    if [(x, y), xy] not in lazor_ls:
                        lazor_ls.append([(x, y), xy])
                break
            elif board[y][x + dir_x] == 'C' or board[y + dir_y][x] == 'C':
                block = Block((x, y), 'C')
                new_dir = block.contact((x, y), lazer[1])
                # If the laser interacts with block 'C' it refracts and penetrates
                # In case the new source is the same as the original one
                # add the next position and the old direction to the source list
                # without checking if it still exist
                lazor_ls.append([(x+dir_x, y+dir_y), new_dir[0]])
                if [(x, y), new_dir[1]] not in lazor_ls:
                    lazor_ls.append([(x, y), new_dir[1]])
                break
            else:
                x = x + lazer[1][0]
                y = y + lazer[1][1]
                # Record all laser traces
                trace.append((x, y))
        # Add all traces to the position list
        lazor_pos.extend(trace)
        # Check if the laser passes through all intersects
        check = all(item in lazor_pos for item in intersects)
        # If position includes all intersects(solved), return True.
        if check:
            return True
    return False


if __name__ == '__main__':
    board = [['x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'A', 'x', 'B', 'x', 'A', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'o', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'A', 'x', 'C', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x']]
    lazor_sorce = [[(4, 5), (-1, -1)]]
    target = [(1, 2), (6, 3)]
    print(lazor_target_track(board, lazor_sorce, target))
