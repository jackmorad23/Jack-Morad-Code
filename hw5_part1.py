# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:30:49 2023

@author: jackm
"""

import hw5_util

# the neighbor locations are (r-1, c), (r, c-1), (r, c+1), and (r+1, c)


def get_nbrs(row, column, num_rows, num_columns):
    neighbors = []
    if row - 1 >= 0:
        #(r-1, c),
        neighbors.append((row - 1, column))
        
    if row + 1 < num_rows:
        #(r+1, c)
        neighbors.append((row + 1, column))
        
    if column - 1 >= 0:
        #(r, c-1),
        neighbors.append((row, column - 1))
        
    if column + 1 < num_columns:
        #(r, c+1)
        neighbors.append((row, column + 1))
        
    return neighbors

#hw5_util.num_grids() returns the number of different grids in the data
num_grid = hw5_util.num_grids()

#gets grid index
n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
print(n)
n = int(n)

#checks if n is between 1 and 3
if n < 1 or n > 3:
    print('invalid input.')
#or else it does the yes or no then gives me the grid number then the number that correspond
else:
    print_g = input("Should the grid be printed (Y or N): ").strip()
    print(print_g)
    print_g = str(print_g).lower()
    
    get_grid = hw5_util.get_grid(n)
    
    num_rows = len(get_grid)
    num_columns = len(get_grid[0])
    
    
    if print_g == 'y':
        print("Grid {}".format(n))
        for row in get_grid:
            for i in row:
                print("  {:2d}".format(i), end='')
            print()
    print("Grid has {} rows and {} columns".format(num_rows, num_columns))
    
    start = hw5_util.get_start_locations(n)
    for position in start:
        neighbors = get_nbrs(position[0], position[1], num_rows, num_columns)
        ne_list = []
        for neighbor in neighbors:
            ne_list.append(neighbor)
        ne_list = sorted(ne_list)
        print("Neighbors of {}: {}".format(position, ne_list).replace('[', '').replace(']', '').replace('), ', ') '))
    
    
    valid = True
    get_path = hw5_util.get_path(n)
    downward = 0
    upward = 0
    
    for i in range(len(get_path) - 1):
        pos_cur = get_path[i]
        move_next = get_path[i + 1]
        get = get_nbrs(pos_cur[0], pos_cur[1], num_rows, num_columns)
        if move_next not in get:
            valid = False
            print("Path: invalid step from {} to {}".format(pos_cur, move_next))
        change = get_grid[pos_cur[0]][pos_cur[1]] - get_grid[move_next[0]][move_next[1]]
        
        if change > 0:
            upward += change
        
        else:
            change = abs(change)
            downward += change  
    
    if valid:
        print("Valid path")
        print("Downward", upward)
        print("Upward", downward)

        



