def bff_reader(file):
    bff_file = open(file,'r').read()
    lines = bff_file.strip().split('\n')
    lines_no_comment = []
    lazer_grid = []
    blocks = [0,0,0]
    laser = []
    intersect = []
    for line in lines:
        if not "#" in line and line:
            lines_no_comment.append(line)
    for i in range(0,len(lines_no_comment)):
        if lines_no_comment[i] == 'GRID START':
            for j in range(i+1, len(lines_no_comment)):
                lazer_grid.append(lines_no_comment[j])
                if lines_no_comment[j] == 'GRID STOP':
                    lazer_grid.remove(lines_no_comment[j])
                    break

    for i in range(0,len(lines_no_comment)):
        if lines_no_comment[i][0] == 'A':
            blocks[0] = int(lines_no_comment[i][2])
        if lines_no_comment[i][0] == 'B':
            blocks[1] = int(lines_no_comment[i][2])
        if lines_no_comment[i][0] == 'C':
            blocks[2] = int(lines_no_comment[i][2])
    
    for i in range(0,len(lines_no_comment)):
        if lines_no_comment[i][0] == 'L':
            laser.append(lines_no_comment[i].strip('L '))
    
    for i in range(0,len(lines_no_comment)):
        if lines_no_comment[i][0] == 'P':
            intersect.append(lines_no_comment[i].strip('P '))
                          
    return lazer_grid, blocks, laser, intersect

if __name__ == '__main__':
    print(bff_reader('mad_1.bff'))
