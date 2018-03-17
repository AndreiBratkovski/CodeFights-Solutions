"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;
"""
def sudoku2(grid):
    #
    # columns
    #
    for i in range(0, 9):
        lst = []
        for j in range(0,9):
            if grid[j][i] == '.':
                continue
            elif grid[j][i] not in lst:
                lst.append(grid[j][i])
            else:
                return False
    #
    # rows
    #
    for row in grid:
        lst = []
        for index in range(0, 9):
            if row[index] == ".":
                continue
            if row[index] in lst:
                return False
            else:
                lst.append(row[index])
                
    #
    # subdivisions
    #
    lst = []
    for x in range(0, 3):
        for y in range(0, 3):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
                
    lst = []
    for x in range(0, 3):
        for y in range(3, 6):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
        
    lst = []
    for x in range(0, 3):
        for y in range(6, 9):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
                
    lst = []
    for x in range(3, 6):
        lst = []
        for y in range(0, 3):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
                
    lst = []
    for x in range(3, 6):             
        for y in range(3, 6):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
                
    lst = []
    for x in range(3, 6):
        for y in range(6, 9):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
                
    lst = []
    for x in range(6, 9):     
        for y in range(0, 3):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
                
    lst = []
    for x in range(6, 9):
        for y in range(3, 6):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
        
    lst = []
    for x in range(6, 9):
        for y in range(6, 9):
            if grid[x][y] == ".":
                continue
            if grid[x][y] in lst:
                return False
            else:
                lst.append(grid[x][y])
                
    return True
            