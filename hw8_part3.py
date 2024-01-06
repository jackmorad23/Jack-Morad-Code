# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:34:33 2023
@author: jackm
"""

import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist

#read the input file
json_file_name = input("Enter the json file name for the simulation => ").strip()
print(json_file_name)

f = open(json_file_name)
data = json.loads(f.read())

#initialize lists for bears and tourists
queue_bears = []  # Reserved bears
bears = []        # Active bears

#create Bear objects for active and reserved bears
for bear in data["active_bears"]:
    bears.append(Bear(bear[0], bear[1], bear[2]))
for bear in data["reserve_bears"]:
    queue_bears.append(Bear(bear[0], bear[1], bear[2]))
    
# print(data["active_bears"], data["reserve_bears"])

#initialize lists for tourists and reserved tourists
tourists = []            # Active tourists
reserve_tourists = []    # Reserved tourists

#create Tourist objects for active and reserved tourists
for tourist in data["active_tourists"]:
    tourists.append(Tourist(tourist[0], tourist[1]))
for tourist in data["reserve_tourists"]:
    reserve_tourists.append(Tourist(tourist[0], tourist[1]))

#create a BerryField object
grid = BerryField(data["berry_field"])
print()
print("Starting Configuration")

#display initial berry field configuration
print("Field has {} berries.".format(grid.total_berries()))
grid.letter(bears, tourists)
print(grid)

#display information about active bears and tourists
print("Active Bears:")
for bear in bears:
    print(bear)
print()
print("Active Tourists:")
for tourist in tourists:
    print(tourist)

#grid loop for 5 turns
left_field_list = []
enter_field_list = []
next_bears = []
next_tourists = []
flagging = False
turns = 1
while True:
    next_bears = []
    next_tourists = []
    
    grid.grow_berry_field()
    
    #update bear positions and interactions with tourists
    for bear in bears:
        
        
            
        if bear.asleep_turns > 0:
            bear.asleep_turns -= 1
            continue
            
        while bear.row >= 0 and bear.row < len(grid.grid) and bear.column >= 0 and bear.column < len(grid.grid[0]) and bear.berries_eaten < 30:
            
            # print(bear.row, bear.column)
            # Check for obstacles and tourists in the bear's path
            if grid.put_letter[bear.row][bear.column] == "X" or grid.put_letter[bear.row][bear.column] == "T":
                grid.put_letter[bear.row][bear.column] = "B"
                
            need_to_break = False    
            #check for tourists at the bear's location
            for i in range(len(tourists)):
                if tourists[i].row == bear.row and tourists[i].column == bear.column:
                    tourists[i].leave_field()
                    bear.asleep = True  # Make bear fall asleep for three turns
                    bear.asleep_turns = 2
                    need_to_break = True
                    break
            if need_to_break == True:
                break
            
            grid = bear.eat(tourists, grid, left_field_list, next_bears, bear.row, bear.column)
            if grid.grid[bear.row][bear.column] == 0 and bear.berries_eaten < 30:
                bear.move()
            
            
        
    
    
    
    
    
    #reset berries eaten count for each bear
    for bear in bears:
        bear.berries_eaten = 0
        bear.enter_field = False
    for bear in bears:
        if bear.row < 0 or bear.column < 0 or bear.row >= len(grid.grid) or bear.column >= len(grid.grid[0]):
            bear.left_field = True
            left_field_list.append(bear)
        else:
            next_bears.append(bear)
    
    bears = next_bears.copy()
    
    #update tourists based on bear proximity
    for i in range(len(tourists)):
        if tourist.left_field:
            continue
        bears_close = tourists[i].sees_bears(bears)
        # if bears_close == 0:
        #     tourists[i].turns_to_bear += 1
        # else:
        #     tourists[i].turns_to_bear = 0
    #check for bears moving out of bounds
    
    
    #move tourists that left the field or reached the turns limit to the reserved list
    for tourist in tourists:
        tourist.enter_field = False
        if tourist.left_field or tourist.turns_to_bear == 3:
            tourist.left_field = True
            left_field_list.append(tourist)
        else:
            next_tourists.append(tourist)
    tourists = next_tourists.copy()
    
    
        
    #check if there are bears in the reserve queue list
    if len(queue_bears) != 0 and grid.total_berries() >= 500:
        active_bears = queue_bears.pop(0)
        active_bears.enter_field = True
        enter_field_list.append(active_bears)
        bears.append(active_bears)
        
    #check if there are reserve tourists in the field and add them to the active tourist list
    just_entered = []
    if len(reserve_tourists) != 0 and len(bears) != 0:
        active_tourist = reserve_tourists.pop(0)
        active_tourist.enter_field = True
        enter_field_list.append(active_tourist)
        tourists.append(active_tourist)
        
    for i in range(len(active_tourist)):
        bears_close = active_tourist[i].sees_bears(bears)
    #display current state of the grid
    grid.letter(bears, tourists)  
    
     #conditons for part 3  
     
     #check if Then, if there is are still tourists in the reserve queue and at least 1 active bear, add the next reserve tourist to the field.
     #bears in the reserve list; or if there are no more bears on the field and no more berries
    if (len(bears) <= 0 and len(queue_bears) <= 0) or (len(bears) <= 0 and grid.total_berries() <= 0):
        flagging = True
    if (turns % 5 == 0) or flagging == True:  
        print()
        
        
        print("Turn: {}".format(turns))
        for item in left_field_list:
            print(item)
        left_field_list = []
        for item in enter_field_list:
            print(item)
            item.enter_field = False
        enter_field_list = []
        if flagging == True:
            print()
            
        print("Field has {} berries.".format(grid.total_berries()))
        grid.letter(bears, tourists)
        print(grid)
        
        
        
        
        print("Active Bears:")
        
        for bear in bears:
            print(bear)
            
        print() 
        
        
        print("Active Tourists:")
        for tourist in tourists:
            print(tourist)
            
            
        if turns != 0 and turns % 5 != 0 and flagging == False:
            print()
        if flagging == True:
            break
        print()
    else:
        print()
        
        print("Turn: {}".format(turns))
        for item in left_field_list:
            print(item)
        for item in enter_field_list:
            print(item)
        print()
        
    # if (len(bears) <= 0 and len(queue_bears) <= 0) or (len(bears) <= 0 and grid.total_berries() <= 0):
    #     break
    
    #increase turns by 1
    turns += 1
    #empty the list
    left_field_list = []
    enter_field_list = []
