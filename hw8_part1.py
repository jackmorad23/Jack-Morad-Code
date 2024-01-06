# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:33:50 2023

@author: jackm
"""
import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist

# f = open("bears_and_berries_1.json")
# data = json.loads(f.read())
# print(data["berry_field"])
# print(data["active_bears"])
# print(data["reserve_bears"])
# print(data["active_tourists"])
# print(data["reserve_tourists"])

# Read the input file
json_file_name = input("Enter the json file name for the simulation => ").strip()
print(json_file_name)

f = open(json_file_name)
data = json.loads(f.read())

queue_bears= []
bears = []
for bear in data["active_bears"]:
    bears.append(Bear(bear[0], bear[1], bear[2]))
for bear in data["reserve_bears"]:
    queue_bears.append((Bear(bear[0], bear[1], bear[2])))

tourists = []
reserve_tourists = []
for tourist in data["active_tourists"]:
    tourists.append(Tourist(tourist[0], tourist[1]))
for tourist in data["reserve_tourists"]:
    reserve_tourists.append(Tourist(tourist[0], tourist[1]))
    
grid = BerryField(data["berry_field"])
print()
print("Field has {} berries.".format(grid.total_berries()))
grid.letter(bears, tourists)
print(grid)

print("Active Bears:")
for bear in bears:
    print("Bear at ({},{}) moving {}".format(bear.row, bear.column, bear.direction))
print()  
print("Active Tourists:")
for tourist in tourists:
    print(tourist)
    


    


        
        
            
    
        
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            