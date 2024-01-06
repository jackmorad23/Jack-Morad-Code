# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:59:02 2023
@author: jackm
"""

# Bear class definition
class Bear:
    # Constructor method to initialize a Bear object with its initial position and direction
    def __init__(self, row, column, direction, berries_eaten=0):
        self.row = row
        self.column = column
        self.direction = direction
        self.asleep = False
        self.asleep_turns = 0
        self.berries_eaten = 0
        self.left_field = False
        self.enter_field = False

    # String representation of a Bear object, used for printing
    def __str__(self):
        if self.asleep_turns > 0:
            return "Bear at ({},{}) moving {} - Asleep for {} more turns".format(self.row, self.column, self.direction, self.asleep_turns)
        elif self.left_field == True:
            return "Bear at ({},{}) moving {} - Left the Field".format(self.row, self.column, self.direction)
        elif self.enter_field == True:
            return "Bear at ({},{}) moving {} - Entered the Field".format(self.row, self.column, self.direction)
        else:
            return "Bear at ({},{}) moving {}".format(self.row, self.column, self.direction)

    # Helper method for moving the bear in the specified direction
    def move(self):
        if self.direction == 'N':
            self.row -= 1
        elif self.direction == 'E':
            self.column += 1
        elif self.direction == 'S':
            self.row += 1
        elif self.direction == 'W':
            self.column -= 1
        elif self.direction == 'SE':
            self.row += 1
            self.column += 1
        elif self.direction == 'NW':
            self.row -= 1
            self.column -= 1
        elif self.direction == 'NE':
            self.row -= 1
            self.column += 1
        elif self.direction == 'SW':
            self.row += 1
            self.column -= 1
        

    # Method for simulating the bear eating berries and moving
    def eat(self, tourists, grid, left_field_list, next_bears, row, column):

        # Calculating berries eaten at the current location
        berries_current_location = grid.grid[row][column]

        while self.berries_eaten < 30 and berries_current_location > 0:
            grid.grid[row][column] -= 1
            berries_current_location = grid.grid[row][column]
            
            self.berries_eaten += 1
            
                    
                      
        return grid
