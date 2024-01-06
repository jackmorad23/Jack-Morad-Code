# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:16:11 2023

@author: jackm
"""

def get_words(description):
    # Replace punctuation symbols with spaces
    for char in description:
        description = description.replace("|", ' ').replace(",", ' ').replace(".", ' ').replace("(", ' ').replace(")", ' ')

    # Convert to lowercase and split the description into words
    words = description.lower().split()

    # Initialize an empty set for filtered words
    new = set()

    # Filter words to keep only those with 4 or more characters that contain only letters
    for word in words:
        if word.isalpha() and len(word) >= 4:
            new.add(word)  # Add the word to the 'new' set

    return new

# Example usage:
file_name = input("Enter a file: ")
with open(file_name, "r") as file:
    club_info = file.readline()
    name, description = club_info.strip().split("|", 1)

word_set = get_words(description)
print("Words in the description for {}:".format(name))
print(word_set)



