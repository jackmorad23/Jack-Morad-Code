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
        neighbors.append((row - 1, column))
        
    if row + 1 < num_rows:
        neighbors.append((row + 1, column))
        
    if column - 1 >= 0:
        neighbors.append((row, column - 1))
        
    if column + 1 < num_columns:
        neighbors.append((row, column + 1))
        
    return neighbors

def check_path(starting_pos, history, max_height):
    # check global max
    if get_grid[starting_pos[0]][starting_pos[1]] == global_var[2]:
        return 0
    
    #check local max
    cur_position = starting_pos
    neighbors = get_nbrs(cur_position[0], cur_position[1], num_rows, num_columns)
    flag1 = 0
    for neighbor in neighbors:
        if get_grid[neighbor[0]][neighbor[1]] > get_grid[cur_position[0]][cur_position[1]]:
            flag1 = 1
            break
    if flag1 == 0:
        return 1
            
    
    #check no max
    flag2 = 0
    
    for n in neighbors:
        elevation_var = get_grid[n[0]][n[1]] - get_grid[cur_position[0]][cur_position[1]]
        if elevation_var > 0 and elevation_var <= max_height:
            flag2 = 1
            break  
    if flag2 == 0:
        return 2
    
    # another move is possible 
    return -1
    


#function to find steepest path from start point
def steep_path(starting_pos, max_height):
    num_rows = len(get_grid)
    num_columns = len(get_grid[0])
    cur_position = starting_pos
    next_pos = None
    
        # Get neighbors for the current position
    neighbors = get_nbrs(cur_position[0], cur_position[1], num_rows, num_columns)
    remaining = -1
        
    
    for neighbor in neighbors:
            
        elevation_var = -get_grid[cur_position[0]][cur_position[1]] + get_grid[neighbor[0]][neighbor[1]]
        
        if elevation_var > 0 and elevation_var <= max_height:
            if elevation_var > remaining:
                remaining = elevation_var
                
                next_pos = neighbor
            
        
    return next_pos


    
    
    
    
#function to get the gradual path
def gradual_path(starting_pos, max_height):
    cur_position = starting_pos
    num_rows = len(get_grid)
    num_columns = len(get_grid[0])


    neighbors = get_nbrs(cur_position[0], cur_position[1], num_rows, num_columns)       
    
    next_pos = None
    change_min_elevation = float('inf')

    for neighbor in neighbors:
        
        difference = get_grid[neighbor[0]][neighbor[1]] - get_grid[cur_position[0]][cur_position[1]]
        
        if difference > 0 and difference <= max_height:
            if difference < change_min_elevation:
                change_min_elevation = difference
                next_pos = neighbor

    return next_pos



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
    max_height = input("Enter the maximum step height: ").strip()
    print(max_height)
    max_height = int(max_height)
    
    get_grid = hw5_util.get_grid(n)
    tmp = [0] * len(get_grid[0])
    path_count = []
    for i in range(len(get_grid)):
        path_count.append(tmp.copy())
    
    
    num_rows = len(get_grid)
    num_columns = len(get_grid[0])
    
    start = hw5_util.get_start_locations(n)
    

    #to get global max
    global_var = (0, 0, get_grid[0][0])
    for row1 in range(num_rows):
        for column1 in range(num_columns):
            if get_grid[row1][column1] > global_var[2]:
                global_var = (row1, column1, get_grid[row1][column1])
                
    print_g = input("Should the path grid be printed (Y or N): ").strip()
    print(print_g)
    print_g = str(print_g).lower()
    
    print("Grid has {} rows and {} columns".format(num_rows, num_columns))
    print("global max: ({}, {}) {}".format(global_var[0], global_var[1], global_var[2]))
    print('===')
    
    
    #function to check the path
    
        
    
    for position in start:
        #steep path
        print("steepest path")
        history = [position]
        print("({}, {})".format(position[0], position[1]), end = ' ')
        path_count[position[0]][position[1]] += 1
        
        # has to be 5 because only 5 points allowed in the output
        steep1 = steep_path(position, max_height)
        history.append(steep1)
        path_count[steep1[0]][steep1[1]] += 1
        while True:
            if (len(history) - 1) % 5 == 0:
                print()
            print("({}, {})".format(steep1[0], steep1[1]), end = ' ')
            # elevation_var = -get_grid[cur_position[0]][cur_position[1]] + get_grid[neighbor[0]][neighbor[1]]    
            
            what_to_do = check_path(steep1, history, max_height)
            
            if what_to_do == 0:
                print("\nglobal maximum")
                break
            elif what_to_do == 1:
                print("\nlocal maximum")
                break
            elif what_to_do == 2:
                print("\nno maximum")
                break

            steep1 = steep_path(steep1, max_height) 
            history.append(steep1)
            path_count[steep1[0]][steep1[1]] += 1
            
        print("...")
            
        #gradual path
        print("most gradual path")
        print("({}, {})".format(position[0], position[1]), end = ' ')
        path_count[position[0]][position[1]] += 1
        history.clear()
        history = [position]
        grad_path = gradual_path(position, max_height)
        history.append(grad_path)
        path_count[grad_path[0]][grad_path[1]] += 1
        while True:
            if (len(history) - 1) % 5 == 0:
                print()
            print("({}, {})".format(grad_path[0], grad_path[1]), end = ' ')
            
            what_to_do = check_path(grad_path, history, max_height)
            
            if what_to_do == 0:
                print("\nglobal maximum")
                break
            elif what_to_do == 1:
                print("\nlocal maximum")
                break
            elif what_to_do == 2:
                print("\nno maximum")
                break

            grad_path = gradual_path(grad_path, max_height) 
            history.append(grad_path)
            path_count[grad_path[0]][grad_path[1]] += 1
                
            
            
        print("===")
       
        
    #path grid
    if print_g == 'y':
        print("Path grid")
        for row in path_count:
            for i in row:
                if i == 0:
                    print('  .', end = '')
                else:
                    print("  " + str(i), end = '')
            print()
    else:
        print('')

    
        
    
    
    
    
    

        



