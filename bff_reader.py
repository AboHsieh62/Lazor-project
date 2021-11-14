"""
This .py file reads the board requirements (.bff files)
@author: Po-I Hsieh, Vina Ro
"""


def bff_reader(file):
    '''
    Reads in a file and that contains:
        - comments starting with #
        - information on blocks in the format of: type|number (ex. A 2)
        - information on lasers in the format of:
            starting point|direction(ex. L 2 7 1 -1)
        - laser intersection points (ex. P 3 0)
        - Block grid (in the below style)

            GRID START
             grid data
            GRID STOP

            Where symbols are:
                x = no block allowed
                o = blocks allowed
                A = fixed reflect block
                B = fixed opaque block
                C = fixed refract block

    **Parameters**

        filename: *str*
            The .bff file that contains all the data mentioned above

    **Returns**

        grid: *list, list, str*
            A list X of lists Y containing strings. The lists Y contain values
            for the rows in the array and the list X contains each column.

        blocks: *list*
            A list of the number of each type of block in the order A, B, and C

        lasers: *list, list, tuple, int*
            A list containing lists of 2 sets of tuples each contain 2 integers
            The first tuple is the laser's starting (x, y) coordinates
            The second tuple is the laser's initial direction

        intersects: *list, tuple, int*
            A list of tuples which each have two integers, which are a required
            intersections (x, y) coordinates
    '''

    bff_file = open(file, 'r').read()
    lines = bff_file.strip().split('\n')
    lines_no_comment = []
    lazer_grid = []
    grid = []
    blocks = [0, 0, 0]
    laser = []
    intersect = []

    # Reorganize the file. Remove all comments and space sentences.
    for line in lines:
        if "#" not in line and line:
            lines_no_comment.append(line)

    # Recognize the lazer grid
    for i in range(0, len(lines_no_comment)):
        if lines_no_comment[i] == 'GRID START':
            for j in range(i+1, len(lines_no_comment)):
                lazer_grid.append(lines_no_comment[j].replace(' ', ''))
                if lines_no_comment[j] == 'GRID STOP':
                    lazer_grid.remove(lines_no_comment[j].replace(' ', ''))
                    break

    del lines_no_comment[0:j+1]

    # Recognize the blocks and seperate them into 'A', 'B', 'C'
    for i in range(0, len(lines_no_comment)):
        if lines_no_comment[i][0] == 'A':
            blocks[0] = int(lines_no_comment[i][2])
        elif lines_no_comment[i][0] == 'B':
            blocks[1] = int(lines_no_comment[i][2])
        elif lines_no_comment[i][0] == 'C':
            blocks[2] = int(lines_no_comment[i][2])

    # Recognizes the laser and stores it into two seperate tuples:
    # coordinate and direction
    for i in range(0, len(lines_no_comment)):
        if lines_no_comment[i][0] == 'L':
            ll = lines_no_comment[i].strip('L ').split(' ')
            laser.append([(int(ll[0]), int(ll[1])), (int(ll[2]), int(ll[3]))])

    # Recognize all the intersects
    for i in range(0, len(lines_no_comment)):
        if lines_no_comment[i][0] == 'P':
            ll = lines_no_comment[i].strip('P ').split(' ')
            intersect.append((int(ll[0]), int(ll[1])))

    # Saves grid as a calculatable form
    grid_len = 2*len(lazer_grid[0])+1
    grid.append(['x']*grid_len)
    for i in range(0, len(lazer_grid)):
        ll = list(lazer_grid[i])
        j = 0
        while j < grid_len:
            ll.insert(j, 'x')
            j = j+2
        grid.append(ll)
        grid.append(['x']*grid_len)

    return grid, blocks, laser, intersect


if __name__ == '__main__':
    print(bff_reader('yarn_5.bff')[0])
    print(bff_reader('yarn_5.bff')[1])
    print(bff_reader('yarn_5.bff')[2])
    print(bff_reader('yarn_5.bff')[3])
    print(bff_reader('yarn_5.bff'))
    # print(bff_reader('dark_1.bff'))
    # print(bff_reader('mad_1.bff')[2])
    # print(bff_reader('mad_4.bff'))
    # print(bff_reader('mad_7.bff'))
    # print(bff_reader('numbered_6.bff'))
    # print(bff_reader('showstopper_4.bff'))
    # print(bff_reader('tiny_5.bff'))
