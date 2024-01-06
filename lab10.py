# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:03:25 2023

@author: jackm
"""
import random
import time

def closest1(list1):
    """
    >>> closest1([])
    (None, None)
    
    >>> closest1([3.5, 1.2, 7.8, 2.1, 5.4])
    (1.2, 2.1)
    
    >> closest([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    """
    #if len is < 2 then make a none tuple
    if len(list1) < 2:
        return (None, None)
    
    #make a pair of list[0], and list[1]
    closest_pair = (list1[0], list1[1])
    
    smallest_difference = abs(list1[0] - list1[1])
    
    #need two for loops
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            
            current_difference = abs(list1[i] - list1[j])
            
            #check if the current difference is less than the smallest diff then make that the current
            if current_difference < smallest_difference:
                smallest_difference = current_difference
                
                #make a tuple of the closest pair 
                closest_pair = (list1[i], list1[j])
    
    
    return closest_pair

def closest2(list1):
    """
    >>> closest2([])
    (None, None)
    
    >>> closest2([3.5, 1.2, 7.8, 2.1, 5.4])
    (1.2, 2.1)
    
    >>> closest2([4.6, 1.2, 8.8, 3.1, 6.4])
    (3.1, 4.6)
    """
    #if len is < 2 then make a none tuple
    if len(list1) < 2:
        return (None, None)
    
    
    sorted_list1 = sorted(list1)
    #make a pair of list[0], and list[1]
    closest_pair = (sorted_list1[0], sorted_list1[1])
    
    smallest_difference = abs(sorted_list1[0] - sorted_list1[1])
    
    
    
    #need two for loops
    for i in range(len(sorted_list1)):
        for j in range(i + 1, len(sorted_list1)):
            
            current_difference = abs(sorted_list1[i] - sorted_list1[j])
            
            #check if the current difference is less than the smallest diff then make that the current
            if current_difference < smallest_difference:
                smallest_difference = current_difference
                
                #make a tuple of the closest pair 
                closest_pair = (sorted_list1[i], sorted_list1[j])
    
    
    return closest_pair

if __name__ == "__main__":
    print("Closest 1:")
    L1 = [3.5, 1.2, 7.8, 2.1, 5.4]
    L2 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    result = closest1(L1)
    print(result)
    result2 = closest1(L2)
    print(result2)
    
    print("Closest 2:")
    L3 = [3.5, 1.2, 7.8, 2.1, 5.4]
    result3 = closest2(L3)
    print(result3)
    L4 = [4.6, 1.2, 8.8, 3.1, 6.4]
    result4 = closest2(L4)
    print(result4)
    
    print()
    print("Timimg:")
    
    lengths = [100, 1000, 10000]
    for length in lengths:
        
        random_list = [random.uniform(0.0, length) for i in range(length)]
        print(len(random_list))
        
        #time for closest1 
        start_time1 = time.time()
        result1 = closest1(random_list)
        end_time1 = time.time() - start_time1
        
        # print(end_time1)
        print("Closest1 - List length {}: Time: {:.6f} seconds".format(length, end_time1))

        # Timing for closest2
        start_time2 = time.time()
        
        result2 = closest2(random_list)
        end_time2 = time.time() - start_time2
        # print(end_time2)
        print("Closest2 - List length {}: Time: {:.6f} seconds".format(length, end_time2))
        
        print()
        
    
    
    
