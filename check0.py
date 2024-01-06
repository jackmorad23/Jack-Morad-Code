# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:43:58 2023

@author: jackm
"""

#part 1
line = ""
for num in range(9):
    line += str(num) + " "
print(line)

print()
#part 2
for row in range(9):
    for col in range(9):
        if col == 8:
            print("{},{}".format(row, col))
        else:
            print("{},{}".format(row, col), end=" ")
    if row % 3 == 2:
        print()
        
        
row = 2
for col in range(9):
    print("{},{}".format(row, col), end=" ")
    
    
print()
print()
col = 5
for row in range(9):
    print("{},{}".format(row, col), end=" ")
    
    
print()
print()

for row in range(3):
    for col in range(3):
        print("{},{}".format(row, col), end=" ")
    print()  # Move to the next line for the next row