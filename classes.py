class Block:

    def __init__(self, coordinate, block_type):
        self.coordinate = coordinate
        self.block_type = block_type
    
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
            new_dir = block.(pos, dirc)
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
    
    return new_dir
