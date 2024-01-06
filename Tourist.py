# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:59:02 2023

@author: jackm
"""

class Tourist:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.left_field = False
        self.enter_field = 0
        self.turns_to_bear = 0
    
    def __str__(self):
        if self.left_field == True:
            return "Tourist at ({},{}), {} turns without seeing a bear. - Left the Field".format(str(self.row), str(self.column), str(self.turns_to_bear))
        elif self.enter_field == True:
            return "Tourist at ({},{}), {} turns without seeing a bear. - Entered the Field".format(str(self.row), str(self.column), str(self.turns_to_bear))
        else:
            return "Tourist at ({},{}), {} turns without seeing a bear.".format(str(self.row), str(self.column), str(self.turns_to_bear))

    #nearby bears and distance formula less than 4
    def sees_bears(self, bears):
        bears_sees = 0
        for bear in bears:
            if ((bear.row - self.row)**2 + (bear.column - self.column) ** 2) ** 0.5 <= 4:
                bears_sees += 1
        
        if bears_sees >= 3:
            self.left_field = True
            return bears_sees
        elif 0 < bears_sees:
            self.turns_to_bear = 0
        elif bears_sees == 0:
            self.turns_to_bear += 1
        if self.turns_to_bear > 3:
            self.left_field = True
        
        return bears_sees
    
    def location(self):
        return (self.row, self.column)
    
    def leave_field(self):
        self.left_field = True
    
    
    