# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:21:14 2023

@author: jackm
"""

#from directions- Read this English dictionary into a Python dictionary
def english_dictionary(file_name):
    
    english_dict = dict()
    with open(file_name, 'r') as file:
        for line in file:
            #go through each line and split it by commas because in the file its seperated by commas
            word, freq = line.strip().split(",")
            #make the dictionary with the key = word and float freq
            english_dict[word] = float(freq)
            
    #return the dictionary    
      
    return english_dict

#gets the keyboard input and returns it as a dictionary called keyboard_dict
def keyboard(file_name):
    keyboard_dict = dict()
    with open(file_name, 'r') as file:
        for line in file:
            split_lines = line.strip().split(" ")
            #letter is the first index
            first_letter = split_lines[0]
            #as in the file the replacements are the first letter after the first letter 
            possible_replacements = split_lines[1:]
            # print(possible_replacements)
            
            #the first letter is the key and the remaining letters are the value in a list
            keyboard_dict[first_letter] = possible_replacements
    
    #return the dictionary
    
    return keyboard_dict
   


#for all these functions we need to store the value in a set/list/or dictionary im gonna do a list easiest         
def drop(word, english_dict):
    #create list
    drop_list = []
    #goes thru the length of the word
    for i in range(len(word)):
        words = word[:i] + word[i + 1:]
        #list is appended by the word[i] which gets the prefix of the word and then word[i + 1:] gives the letters after the :i
        
        #check if words in dictionary
        if words in english_dict:
            drop_list.append((english_dict[words], words))
    return drop_list

def insert(word, english_dict):
    #create list
    insert_list = []
    
    for i in range(len(word) + 1):
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            words = word[:i] + letter + word[i:]
            #same process as drop but youre just inserting the letter in the middle instead of taking a letter out
            #check if words in dictionary
            if words in english_dict:
                insert_list.append((english_dict[words], words))
    # print(insert_list)        
    return insert_list

def swap(word, english_dict):
    #create list
    swap_list = []
    
    #has to len(word) - 1 because we have to include adjacent characters
    for i in range(len(word) - 1):
        words = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        #append the list and same process as others but you need a i + 1 to go to the next letter then i + 2 to go over two
        #check if words in dictionary
        if words in english_dict:
            swap_list.append((english_dict[words], words))
        
    return swap_list

def replace(word, substitute_keyboard_word, english_dict):
    #create list
    replace_list = []
    
    # print(substitute_keyboard_word)
    #same process as others but add the substitute word
    for i in range(len(word)):
        #for each letter in the sub keyboard input append the list
        for sub_letter in substitute_keyboard_word[word[i]]:
            words = word[:i] + sub_letter + word[i + 1:]
            #check if words in dictionary
            if words in english_dict:
                replace_list.append((english_dict[words], words))
            
    return replace_list

#the drop, insert, swap, and replace functions will go in here as they are candidate corrections. make for loops for each
def candidate_corrections(word, english_dict, keyboard_call):
    #i tried a list first but list include duplicates and i had a problem with relocating
    #candidates make a set for it  
    candidates = set()
    
    #append the candidates list if the drop word is able to be added same process for each function call
    drop_word = drop(word, english_dict)
    for dropping in drop_word:
        candidates.add(dropping)
            
    #call the insert word function and use a for loop to iterate through each letter in insert word and add to the set
    insert_word = insert(word, english_dict)
    for inserting in insert_word:
        candidates.add(inserting)
            
    #call the swap word function and use a for loop to iterate through each letter in swap word and add to the set   
    swap_word = swap(word, english_dict)
    for swapping in swap_word:
        candidates.add(swapping)
            
    #call the replace word function and use a for loop to iterate through each letter in replace word and add to the set
    replace_word = replace(word, keyboard_call, english_dict)
    for replacing in replace_word:
        candidates.add(replacing)
            
    
    #return the updated list, candidates will return the word and if the letter can be dropped, inserted, swapped, or replaced

    return list(candidates)

    


if __name__ == "__main__":
    
    #user input for dictionary file
    dictionary_file = input("Dictionary file => ").strip()
    # dictionary_file = "words_10percent.txt"
    print(dictionary_file)
    
    #user input for input file
    input_file = input("Input file => ").strip()
    # input_file = "input_words.txt"
    print(input_file)
    
    #user input for keyboard file
    keyboard_file = input("Keyboard file => ").strip()
    # keyboard_file = "keyboard.txt"
    print(keyboard_file)
    
    #call the dictionary functiont to see if the word is in the dictionary
    english_dict = english_dictionary(dictionary_file)
    #call the keyboard function to get the dictionary
    keyboard_call = keyboard(keyboard_file)
    
    #open the input file and read it and strip it 
    with open(input_file, "r") as file:
        for line in file:
            #split it into lines
            word = line.strip()
            #if word is in the dictionary file
            if word in english_dict:
                #print the word and found
                print("{:>15} -> FOUND".format(word))
            
            else:
                #call the candidate function and see if the word is found or not with the corrections
                candidate_call = candidate_corrections(word, english_dict, keyboard_call)
                if candidate_call:
                    # if len(candidate_call) <= 3:
                    #sort the candidates if its more than one. lexigraphsical order 
                    candidate_call.sort(reverse = True)
                    #get the first three if its more than one
                    top_choice = []
                    for choice in candidate_call:
                        top_choice.append(choice[1])
                    if len(candidate_call) >= 10:
                        print("{:>15} -> FOUND {}:  {}".format(word, len(candidate_call), ' '.join(top_choice[:3])))
                    else:
                        print("{:>15} -> FOUND  {}:  {}".format(word, len(candidate_call), ' '.join(top_choice[:3])))
                else:
                    #else return not found for the word not found
                    print("{:>15} -> NOT FOUND".format(word))
                    
                    
            