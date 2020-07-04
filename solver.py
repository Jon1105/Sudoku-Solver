import numpy as np
import getBoard
board = [[2, 0, 5, 0, 0, 9, 0, 0, 4],
         [0, 0, 0, 0, 0, 0, 3, 0, 7],
         [7, 0, 0, 8, 5, 6, 0, 1, 0],
         [4, 5, 0, 7, 0, 0, 0, 0, 0],
         [0, 0, 9, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 5],
         [0, 2, 0, 4, 1, 8, 0, 0, 6],
         [6, 0, 8, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 2, 0, 0, 7, 0, 8]]


def possible(x, y, n, grid):
    "Can number satisfy sudoku conditions in position?"
    for i in range(9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False
    # returns 0, 3, 6
    x0 = (x//3)*3
    y0 = (y//3)*3
    for yn in range(3):
        for xn in range(3):
            if grid[y0+yn][x0+xn] == n:
                return False
    return True


def rSolve(grid, arr):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for i in range(1, 10):
                    if possible(x, y, i, grid):
                        grid[y][x] = i
                        rSolve(grid, arr)
                        grid[y][x] = 0
                return
    arr.append(grid)


def solve(grid):
    l = []
    rSolve(grid, l)
    return l
