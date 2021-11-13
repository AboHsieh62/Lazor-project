# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:41:25 2021

@author: Vina
"""

class Block:

    def __init__(self, coordinates, blktype):
        '''
        This function initializes the block object
        
        **Parameters**

            coordinates: *tuple
                The x y coordinates of the block on the board

        '''
        self.coord = coordinates
        self.blktype = blktype


    def next_direction(self, curr_direct, position):
        #lz_direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        # Check if x coordinate is even or odd
        if position[0] % 2 == 1:
            #non_zero_ind = [i for i, element in enumerate(blocks) if element!=0]
            
            # If block is A(reflective)
            if self.blktype == 0:
                new_direct = (curr_direct[0], curr_direct[1]*-1)
            # If block is B(opaque)
            elif self.blktype == 1:
                new_direct = []
            # If block is C(refractive)
            else:
                new_direct = (curr_direct[0], curr_direct[1]*-1)
                new_direct.append(curr_direct)
        return new_direct
                
        
    def pos_chk:
        """
        This function checks if the current laser position is within the board.
    
        **Parameters**
    
            board: *list, list, string*
                contains list of x coordinates, in which list is a list of y coordinates
                containing a string representing the type of block on the board
    
            pos: *tuple*
                the current (x,y) position of the laser
    
        **Returns**
    
            *boolean*
                True if within board and False if outside board
        """
        len_x, len_y = len(board), len(board[0])
        if (pos[0] <= 0 or pos[0] >= len_x - 1 or pos[1] <= 0 or pos[1] >= len_y - 1):
            return False
        else:
            return True

        
def laser_new_pos(position, board, direction):
    '''
    If the laser is not currently at the boundary, this function will check
    whether laser interacts with a block and return the new direction of laser
    
    **Parameters**
    
        board: *list, list, string*
            A list of list holds all elements on board
    
        pos: *tuple of 2 int*
            The current position of laser
    
        dirc: *tuple of 2 int*
            The current direction laser is going
    
    **Return**
        new_dir: *list*
            a list that hold new directions laser will be going
    '''
    x = position[0]
    y = position[1]
    lsr_new_dir = []
    
    # Check laser position and if it hits a block, then change direction
    # appropriately, otherwise continue on in the same direction
    
    # Check above and below laser position if x is an odd number
    if x % 2 == 1:
        if (board[x][y + direction[1]].blktype() == 'A') or 
                (board[x][y + direction[1]].blktype() == 'B') or 
                (board[x][y + direction[1]].blktype() == 'C'):
            block = Block((x, y + direction[1]), board[x][y + direction[1]])
            lsr_new_dir = block.(pos, dirc)
        else:
            lsr_new_dir = direction
    
    
    # Check left and right of laser position if x is an even number
    else:
        if (board[x + direction[0]][y].blktype() == 'A') or
                (board[x + direction[0]][y].blktype() == 'B') or
                (board[x + direction[0]][y].blktype() == 'C'):
    
            block = Block((x + dirc[0], y), board[x + dirc[0]][y])
            lsr_new_dir = block.laser(pos, dirc)
        else:
            lsr_new_dir = direction
    
    return lsr_new_dir

def laser_runner(board, laser_origin, target_list):
    '''
    Takes a board and runs lasers from given start positions and directions through
    the Lazor board and blocks, tracking each laser's position as it goes and
    checking if all required target positions have been intersected by a laser.

    **Parameters**
        board: *list, list, string*
            contains list of x coordinates, in which list is a list of y coordinates
            containing a string representing the type of block on the board

        laser_origin: *list, list, tuple, int*
            A list containing lists of 2 sets of tuples that each contain 2 integers
            The first tuple is the laser's starting (x, y) coordinates
            The second tuple is the laser's initial direction

        targetPos: **list, tuple, int*
            A list of tuples which each have two integers, which are a required
            intersections (x, y) coordinates

    **Returns**
        *boolean*
            True if not on all positions are interesected by the laser(s)
            and False if not all target positions have been hit
    '''

    max_trials = 1000
    trials = 0

    # Initialize the list laserpos that stores all laser positions
    laserpos = []
    remn_target = target_list
    #target_remain = copy.deepcopy(targetPos)
    for pos in laser_origin:
        laserpos.append([pos])

    # Solving for the laser's pathway through a given board
    solved = False

    # Keep iterating the laser until: 
    # 1. Solved 2. All lasers are out of the boundary 3. All lasers are absorbed
    while solved != True:
        trials += 1
        for i in range(len(laserpos)):

            # Get current position of this laser if the last position in this
            # laser list is not empty. If it is empty, just continue
            if (len(laserpos[i][-1]) == 0):
                continue
            pos, dirc = laserpos[i][-1][0], laserpos[i][-1][1]

            # Check if laser is at the boundaries.
            # If so, append an empty list to this list in laserpos and skip to
            # the next laser
            if (not pos_chk(board, pos)) and (trials > 1):
                laserpos[i].append([])
                continue

            # move laser one step forward
            next_direct = laser_new_pos(board, pos, dirc)

            # If laser did not interact with a refract block
            if len(next_direct) == 1:
                dirc = next_direct[0]
                pos = tuple(map(sum, zip(pos, dirc)))
                laserpos[i].append([pos, dirc])

            # If laser interacted with a refract block and created a new laser
            elif len(next_direct) == 2:
                dir1, dir2 = next_direct[0], next_direct[1]
                pos1 = tuple(map(sum, zip(pos, dir1)))
                pos2 = tuple(map(sum, zip(pos, dir2)))

                # Append new position and direction of the first and second
                # lasers to the their respective laserpos (an old and new one)
                # first list in laserpos
                laserpos[i].append([pos1, dir1])
                laserpos.append([[pos2, dir2]])
            else:
                laserpos[i].append([])

        # Go throught the current laserpos and see whehther all target
        # points are in the laserList
        rmn_lasers = 0

        # Check whether this block assignment has failed by checking
        # whether all lasers have reached boundaries
        for lasers in laserpos:
            if not (len(lasers[-1]) == 0):
                rmn_lasers += 1

        # break the while loop if lasers cannot go anywhere else or if the
        # max iterations have been reached
        if (laser_alive == 0) or (trials == maxtrials):
            break

    for lasers in laserpos:
        for positions in lasers:

            # Remove targets being hit by lasers from the target_list list
            try:
                if (positions[0] in target_list):
                    rmn_target.remove(positions[0])
            except IndexError:
                pass

    # Check to see if all targets are intersected by the lasers
    if (len(target_list) == 0):
        return True
    else:
        return False



if __name__ == "__main__":
