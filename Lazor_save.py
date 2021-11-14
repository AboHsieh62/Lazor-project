"""
This file saves the solution to a .png file
@author: Po-I Hsieh, Vina Ro
"""

from PIL import Image


def get_colors():
    '''
    Colors map that the png file will use:
        x - gray = no block allowed
        o - sliver = blocks allowed
        A - white = fixed reflect block
        B - black = fixed opaque block
        C - light blue = fixed refract block

    **Returns**
        color_map: *dict, int, tuple*
            A dictionary that will correlate the integer key to
            a color.
    '''
    return {
        'x': (128, 128, 128),
        'A': (255, 255, 255),
        'o': (192, 192, 192),
        'B': (0, 0, 0),
        'C': (173, 216, 230),
    }


def save_grid(grid, name):
    '''
    This will save a grid object to a png file to show the
    solution of where the blocks should be placed on the board.

    **Parameters**
        grid: *list, list, str*
            A list of lists, holding strings specifying the different aspects
            of the grid
                'o' - An open space
                'x' - A space that blocks can't be (includes boundaries)
                'A' - A reflective block
                'B' - An opaque block
                'C' - A refractive block

        name: *str, optional*
            The name of the saved png filename.

    **Returns**
        Saves a png file
    '''

    # Define the grid image, blockSize1 is the border areas, and blockSize2
    # is the size of the various blocks.
    blockSize1 = 10
    blockSize2 = 60
    nBlocksx = len(grid[0])
    nBlocksy = len(grid)

    # Set png size
    dimx = ((nBlocksx - 1) // 2 * (blockSize1 + blockSize2)) + blockSize1
    dimy = ((nBlocksy - 1) // 2 * (blockSize1 + blockSize2)) + blockSize1
    colors = get_colors()

    # save a new png
    img = Image.new("RGB", (dimx, dimy), color=0)

    # Parse "grid" into pixels, making the border areas thinner than the main
    # block areas. Then assigning the appropriate colors to those areas.
    for jy in range(nBlocksy):
        for jx in range(nBlocksx):

            if jy % 2 == 0:
                y = (jy // 2) * (blockSize2 + blockSize1)
                yran = blockSize1

                if jx % 2 == 0:
                    x = (jx // 2) * (blockSize2 + blockSize1)
                    xran = blockSize1
                else:
                    x = ((jx + 1) // 2) * \
                        (blockSize2 + blockSize1) - blockSize2
                    xran = blockSize2

            else:
                y = ((jy + 1) // 2) * (blockSize2 + blockSize1) - blockSize2
                yran = blockSize2

                if jx % 2 == 0:
                    x = (jx // 2) * (blockSize2 + blockSize1)
                    xran = blockSize1
                else:
                    x = ((jx + 1) // 2) * \
                        (blockSize2 + blockSize1) - blockSize2
                    xran = blockSize2

            for i in range(xran):
                for j in range(yran):
                    img.putpixel((x + i, y + j), colors[grid[jy][jx]])

    # delete the .bff of the filename, save as grid_solution.png
    if ".bff" in name:
        name = name.split(".bff")[0]
    if not name.endswith(".png"):
        name += "_solution.png"
    img.save("%s" % name)
    print("Solution saved as %s" % name)


if __name__ == '__main__':
    grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'A', 'x', 'o', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'A', 'x', 'o', 'x', 'o', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'A', 'x', 'o', 'x', 'A', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'o', 'x', 'A', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    name = 'gridsolaaa'
    save_grid(grid, name)
