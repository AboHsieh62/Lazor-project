def get_colors():
    '''
    Colors map that the lazor grip will use:
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
        'C': (232, 244, 248),
    }