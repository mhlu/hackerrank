#!/bin/python3
# find cells with larger number than it's four adjacent cells
import sys

n = int(input().strip())
grid = []
grid_i = 0

moves = [(-1,0), (1,0), (0,-1), (0,1)]
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)
    
new_grid = []
for i in range(n):
    new_grid.append(list(grid[i]))
    
for i in range(1, n-1):
    for j in range(1, n-1):
        for (mi, mj) in moves:
            if int(new_grid[i][j]) <= int(grid[i+mi][j+mj]):

                break
        else:
            new_grid[i][j] = 'X'

for row in new_grid:
    for cell in row:
        print(cell, end='')
    print()

