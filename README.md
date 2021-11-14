# Lazor-project
This is a Python solver for the game Lazors.

## How To Use
1. Uncomment the .bff file you want to run in the file named Lazor project.py, then run file.
2. Results will be stored into a png file(shown below), showing where the blocks should be placed to solve.

![tiny_5_solution](https://user-images.githubusercontent.com/43463024/141701993-b96f2278-e4b2-45eb-a30b-c3786c84da52.png)

Fig 1. Solution for tiny_5. Retractive blocks are in white, opaque blocks are in black, and reflective blocks are in blue.

## Code Descriptions 
1. bff_reader.py: Reads the .bff files into data structures we need to manipulate later in the solver.
2. Lazor_tarck.py: The main algorithm for determining the laser pathways and finding a solution.
3. Lazor_save.py: Saves the final solution into a .png file.
4. Lazor project.py: The main(and only) file needed to run in order to solve the board.

## Contributors
Po-I Hsieh
Vina Ro
