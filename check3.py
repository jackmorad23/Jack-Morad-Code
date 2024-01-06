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

def similiar_clubs(club1_file):
    with open(club1_file, "r") as file1:
        club1_info = file1.readline()
        name1, description1 = club1_info.strip().split("|", 1)
        club1_words = get_words(description1)

    # Initialize a list to store similarities
    similarities = []

    # Read descriptions of all clubs from allclubs.txt
    with open("allclubs.txt", "r") as allclubs_file:
        for line in allclubs_file:
            #splits this into name then all the words after the |
            club2_info = line.strip().split("|", 1)
            name2, description2 = club2_info
            club2_words = get_words(description2)

            # Ensure that club2 is different from club1
            if name1 != name2:
                # Calculate the similarity as the number of common words
                similarity = len(club1_words.intersection(club2_words))
                similarities.append((similarity, name2))
            else:
                print("Same club.")

    # Sort the list by similarity in reverse order to get the most similar clubs first
    similarities.sort(reverse=True)

    # Print the top 5 most similar clubs
    print("Top 5 most similar clubs to '{}':".format(name1))
    for i, (similarity, name2) in enumerate(similarities[:5], start=1):
        print("{}. Club: {} Similarity: {} common words".format(i, name2, similarity))


def compare_clubs(club1_file, club2_file):
    with open(club1_file, "r") as file1:
        club1_info = file1.readline()
        #splits this into name then all the words after the |
        name1, description1 = club1_info.strip().split("|", 1)
        
    with open(club2_file, "r") as file2:
        club2_info = file2.readline()
        #splits this into name then all the words after the |
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




sim = similiar_clubs(file_name1)
print(sim)




