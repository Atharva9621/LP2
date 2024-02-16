import sys
from typing import List
n = len(sys.argv)
if n==1:
    MODE = "DEFAULT"
elif sys.argv[1]=='display':
    MODE = "DISPLAY"
else:
    MODE = "DEFAULT"

if n==3:
    N_QUEENS = int(sys.argv[2])
else:
    N_QUEENS = 5

if MODE=="DISPLAY":
    from chessboard.chessboard import Chessboard

def is_danger(grid: List[List[bool]], row: int, col: int) -> bool:
    n = len(grid)
    for i in range(row+1):
        if grid[i][col]:
            return True
    for i in range(min(row, col)):
        if grid[row-i-1][col-i-1]:
            return True
    for i in range(min(row, n-1-col)):
        if grid[row-i-1][col+1+i]:
            return True
    return False

def place_queen(grid: List[List[bool]], row:int, verbosity:bool =False)->bool:
    n = len(grid)
    for col in range(n):
        if not is_danger(grid, row, col):
            if verbosity:
                print(f"Placing a Queen at ({row}, {col}) ")
            grid[row][col] = 1
            if place_queen(grid, row+1, verbosity ) or row==n-1:
                return True
            else:
                grid[row][col] = 0
    return False

def solveNQueen(n: int, verbosity: bool=False)->List[List[bool],]:
    grid = [[0 for i in range(n)] for i in range(n)]
    res = True
    try:
        res = place_queen(grid, 0, verbosity)
        return grid
    except Exception as e:
        print(e)
        if not res:
            print('Unable to find optimal solution')

if __name__ == "__main__":
    grid = solveNQueen(N_QUEENS)
    if MODE=="DEFAULT":
        for row in grid:
            print(row)
    elif MODE=="DISPLAY":
        chessboard = Chessboard(grid, None)
        chessboard.run()