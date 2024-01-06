# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:59:02 2023

@author: jackm
"""

# The berry field must maintain and manage the location of berries as a square Row X Column grid
# with (0,0) being the upper left corner and (N-1, N-1) being the lower right corner. Each space
# holds 0-10 berry units.
class BerryField:
    def __init__(self, grid):
        self.grid = grid
        self.put_letter = list()
        
    # The string function must, minimally, be able to generate a string of the current state of the berry patch.
    def __str__(self):
        #go through a for loop to go through each value in the self.grid
        result = ""
        for row in range(0, len(self.put_letter)):
            item = ""
            for column in range(0, len(self.put_letter[0])):
                item = item + "{:>4}".format(self.put_letter[row][column])
            result = result + item + '\n'
        return result
    
    
    #inserting the b, t, and x in the grid
    def letter(self, bears, tourists):
        new_list1 = []
    
        # Copy the grid to avoid modifying the original grid
        for row in self.grid:
            new_list2 = []
            for value in row:
                new_list2.append(value)
            new_list1.append(new_list2)
    
        # Insert bears into the grid
        for bear in bears:
            # Check if the bear's coordinates are within the grid
            if 0 <= bear.row < len(new_list1) and 0 <= bear.column < len(new_list1[0]):
                new_list1[bear.row][bear.column] = "B"
    
        # Insert tourists into the grid
        for tourist in tourists:
            # Check if the tourist's coordinates are within the grid
            if 0 <= tourist.row < len(new_list1) and 0 <= tourist.column < len(new_list1[0]):
                if new_list1[tourist.row][tourist.column] == "B":
                    new_list1[tourist.row][tourist.column] = "X"
                else:
                    new_list1[tourist.row][tourist.column] = "T"
    
        self.put_letter = new_list1

                
        
    def grow_berry_field(self):
        for i in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                #self.grid[i][x] is the speciific location of berries and if the condition is true it gains a berry
                if 1 <= self.grid[i][x] < 10:
                    self.grid[i][x] += 1
              
                    
        for i in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                #for the spread method to spread berries where berries = 0 and adjacent to a location with 10 berries
                if self.grid[i][x] == 0 and self.spread(i, x): #checks if the berries at a location is 0 and the spread method is true then it adds a berry
                    self.grid[i][x] += 1
                    
    #helper method to spread berries to neighboring locations    
    def spread(self, row, column):
        
        #create neighbors as a list and any location with no berries that is adjacent to a location with 10 berries will get 1 berry during the grow operation.
        adjacent_neighbors = [(row, column - 1), (row, column + 1), (row - 1, column), (row + 1, column), (row - 1, column - 1), (row + 1, column + 1), (row - 1, column + 1), (row + 1, column - 1)]
        
        for rows, columns in adjacent_neighbors:
            if 0 <= rows < len(self.grid) and 0 <= columns < len(self.grid[0]) and self.grid[rows][columns] == 10:
                return True
        return False
    
    #get total berries
    def total_berries(self):
        count = 0
        for row in self.grid:
            count += sum(row)
        return count
        
    
    
    
    
    
    
    