# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:16:11 2023

@author: jackm
"""

def get_words(description):
    #replace punctuation symbols with spaces
    for char in description:
        description = description.replace("|", ' ').replace(",", ' ').replace(".", ' ').replace("(", ' ').replace(")", ' ')

    #Convert to lowercase and split the description into words
    words = description.lower().split()

    # Initialize an empty set for filtered words
    new = set()

    # Filter words to keep only those with 4 or more characters that contain only letters
    for word in words:
        if word.isalpha() and len(word) >= 4:
            new.add(word)  # Add the word to the 'new' set

    return new


def compare_clubs(club1_file, club2_file):
    with open(club1_file, "r") as file1:
        club1_info = file1.readline()
        name1, description1 = club1_info.strip().split("|", 1)
        
    with open(club2_file, "r") as file2:
        club2_info = file2.readline()
        name2, description2 = club2_info.strip().split("|", 1)
    
    words1 = get_words(description1)
    words2 = get_words(description2)
    
    same = words1.intersection(words2)
    unique_club1 = words1.difference(words2)
    unique_club2 = words2.difference(words1)

    
    new_file3 = club1_file.replace('.txt', '')
    new_file4 = club2_file.replace('.txt', '')
    print("Same words:", same)
    print()
    print("Unique to {}: {}".format(new_file3, unique_club1))
    print()
    print("Unique to {}: {}".format(new_file4, unique_club2))






file_name1 = input("Enter a file: ")
file_name2 = input("Enter a second file: ")

new_file1 = file_name1.replace('.txt', '')
new_file2 = file_name2.replace('.txt', '')

print("Comparing clubs {} and {}:".format(new_file1, new_file2))
print()
compare = compare_clubs(file_name1, file_name2)
print(compare)




