# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:10:53 2023

@author: jackm
"""



def parse_stop_words():
    # Read stop words from stop.txt and return them as a set
    stop_words = set()
    with open("stop.txt", "r") as stop_file:
        #r will be var for reading file
        for line in stop_file:
            # Parse and add stop words to the set
            stop_words.add(line.strip().lower())
    return stop_words


#this function will read the document and remove all the stop words and use the function above to access those stop words
# def parse_docs(file, stop_words):
#     words = []
#     with open(file, "r") as doc:
#         #reads doc
#         for line in doc:
#             #for each line in the doc split the line into words
#             split_words = line.split()
#             #create a new list for the new words without the stop words
#             new_list = []
            
#             #uses isalpha to see if it is a letter and puts it in lower case
#             for word in split_words:
#                 #creates an empty string then goes through each
#                 string1 = ''
#                 for char in word:
#                     if char.isalpha() or char == "'": 
#                         string1 += char
#                 if string1.lower() not in stop_words:
#                     new_list.append(string1.lower())
#             words.append(new_list)
#     for each_list in words:
#         for word in each_list:
            
#             if "'" in word and word.replace("'","") in stop_words: #if the word is a stop word
#                 each_list.remove(word)
                
#             elif "'" in word:
#                 word = word.replace("'", "")
#             elif word in stop_words:
#                 each_list.remove(word)
                
            
#     return words

def parse_docs1(file):
    doc = open(file)
    words = doc.read()
    word_list = words.strip().split()
    i = 0
    while i < len(word_list):
        char = []
        for x in word_list[i]:
            if x.isalpha():
                x = x.lower()
                char.append(x)
        result = ''.join(char)
        if result:
            word_list[i] = result
        else:
            word_list.pop(i)
            i -= 1
        i += 1
    doc.close()
    return word_list
        
                
     
#calculates avg word length     
def avg_word_length(word_list):
    #for each word in the words list calculated above in parse_docs get the total length of words 
    list1 = []
    #goes through each word in words
    for word in word_list:
        list1.append(len(word))
        
    
    #gets the average
    avg = sum(list1) / len(word_list)
    
    return avg      


#gets the ratio between the number of distinct words and the total number of words.
def word_ratio(word_list):
    #make a set for distinct words
    distinct_words = set(word_list)
    
    ratio = len(distinct_words) / len(word_list)
    return ratio

def flatten_extend(matrix):
     flat_list = []
     for row in matrix:
         for word in row:
             if word != '':
                 flat_list.append(word)
     return flat_list
 
    
#grouping words by length
def word_pairs_and_ratio(word_list, max_sep):
    word_length = []
    for i in range(len(word_list)):
        if i + max_sep > len(word_list) - 1:
            for y in range(i + 1, len(word_list)):  
                word_length.append(tuple(sorted([word_list[i], word_list[y]])))
        else:
            for x in range(i + 1, i + max_sep + 1):
                word_length.append(tuple(sorted([word_list[i], word_list[x]])))
    #get the ratio of distinct word pairs to total word pairs
    
    dist_ratio = len(set(word_length)) / len(word_length)
    return word_length, dist_ratio


# def word_pairs(words, max_sep):
#     #make the pairs a list
#     pairs = []
    
#     flat1 = flatten_extend(words)
#     #range(len(words)) because you need to go over the whole words list
#     for i in range(len(flat1)):
#         #i + 1 bc i need to index of the next word after the first word in the list
#         #you would do the min because you dont want it go out of the boundary
#         for x in range(i + 1, min(i + 1 + max_sep, len(flat1))):
#             #have to create a two assignment for the word pairs
#             word_pair1, word_pair2 = flat1[i], flat1[x]
#             if "'" in word_pair1:
#                 word_pair1 = word_pair1.replace("'", "")
#             if "'" in word_pair2:
#                 word_pair2 = word_pair2.replace("'", "")
#             #now have to put them alphabetical
#             if word_pair1 < word_pair2:
#                 pairs.append((word_pair1, word_pair2))
#             else:
#                 pairs.append((word_pair2, word_pair1))
            
#     sort = sorted(pairs)
#     #remove ' from each word, maybe remove stop words ****************************************

#     return sort
            
            
# #get word pair ratio and round it to 3 decimal places
# def word_pair_ratio(pairs_call, total):
#     #gave me a division  by zero error
#     if total == 0:
#         return 0.000
    
#     ratio_eq = len(pairs_call) / total
    
#     return ratio_eq         

#In plain English it is the size of the intersection between two sets divided by the size of their union
def jaccard_similarity(file_set1, file_set2):
    #s1.intersection() — create a new set that contains only the values that are in both sets. Operator syntax:
    file_set1 = set(file_set1)
    file_set2 = set(file_set2)
    intersect = len(list(file_set1.intersection(file_set2)))
    #union() — create a new set that contains values that are in either set.
    union = len(list(file_set1.union(file_set2)))

    if union == 0:
        return 0.000
    #print(intersect)
    #print(union)
    similiar = intersect / union
    
    return similiar
               
    
    



if __name__ == "__main__":
    #ask for input files and the max seperation between words in a pair
    first_file = input("Enter the first file to analyze and compare ==> ").strip()
    # first_file = "cat_in_the_hat.txt"
    print(first_file)
    
    second_file = input("Enter the second file to analyze and compare ==> ").strip()
    # second_file = "pulse_morning.txt"
    print(second_file)
    
    max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
    print(max_sep)
    max_sep = int(max_sep)
    
    #gets the stop words in a list
    stop_words = parse_docs1("stop.txt")
    #gets the words that has no other characters etc
    words_first_file = parse_docs1(first_file)
    
    word_list1 = words_first_file.copy()
    for word in words_first_file:
        if word in stop_words:
            word_list1.remove(word)
            
    words_first_file = word_list1
    
    
    print()
    #evaluating first file
    print("Evaluating document {}".format(first_file))
    
    
    #avg word length
    avg_word_length1 = avg_word_length(words_first_file)
    print("1. Average word length: {:.2f}".format(avg_word_length1))
    
    #ratio for the distinct words to total words
    ratio_word1 = word_ratio(words_first_file)
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio_word1))

    #word sets
    print("3. Word sets for document {}:".format(first_file))
    words_pairs, ratio = word_pairs_and_ratio(words_first_file, max_sep)
    #make a for loop to get the length of the words, how many words have that length, and the first 6 words. 
    
    max_length = 0
    for word in words_first_file:
        if len(word) > max_length:
            max_length = len(word)
    word_lists1 = []
    for x in range(max_length):
        word_lists1.append([])
    
    for word in words_first_file:
        word_lists1[len(word) - 1].append(word)
        
    for i in range(len(word_lists1)):
        word_lists1[i] = sorted(list(set(word_lists1[i])))
        
    for i in range(len(word_lists1)):
        temp = []
        flag = False
        if len(word_lists1[i]) > 6:
            flag = True
            for j in range(len(word_lists1[i])):
                if j < 3:
                    temp.append(word_lists1[i][j])
            temp.append('...')
            temp += word_lists1[i][-3:]
        if len(word_lists1[i]) == 0:
            print("{:>4}:   {}:".format(i + 1, len(word_lists1[i])))
        elif len(word_lists1[i]) >= 10:
            if flag == False:
                print("{:>4}:  {}: {}".format(i + 1, len(word_lists1[i]), ' '.join(word_lists1[i])))
            else:
                print("{:>4}:  {}: {}".format(i + 1, len(word_lists1[i]), ' '.join(temp)))
        else:
            if flag == False:
                print("{:>4}:   {}: {}".format(i + 1, len(word_lists1[i]), ' '.join(word_lists1[i])))
            else:
                print("{:>4}:   {}: {}".format(i + 1, len(word_lists1[i]), ' '.join(temp)))
        #print(words)
        
    
    
    #word pairs
    print("4. Word pairs for document {}".format(first_file))
    
    
    #call the word pairs function
    word_pairs1, dist_ratio1 = word_pairs_and_ratio(words_first_file, max_sep)
    
    word_pairs1 = list(set(word_pairs1))
    #list(no_duplicates1)
    #len of pairs to get the number of pairs but only want to print the first 10
    if len(word_pairs1) >= 10:
        print("  {:>2} distinct pairs".format(len(word_pairs1)))
    else:
        print(" {:>2} distinct pairs".format(len(word_pairs1)))
    
    #It should also output the first 5 word pairs in alphabetical order
    word_pairs1 = sorted(word_pairs1)
    if len(word_pairs1) <= 5:
        for pair in word_pairs1:
            print("  {} {}".format(pair[0], pair[1]))
    else:
        count = 0
        for pair in word_pairs1:
            if count < 5:
                print("  {} {}".format(pair[0], pair[1]))
                count += 1
        print("  ...")
    #It should also output the last 5 word pairs in alphabetical order
        count = 0
        position = 0
        for pair in word_pairs1:
            position += 1
            if count < 5 and position + 5 >= len(word_pairs1) + 1:
                print("  {} {}".format(pair[0], pair[1]))
        
        
        
    #ratio of word pairs 
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(dist_ratio1))

    print()
    
    
    
    
    
    #document 2
   #gets the words that has no other characters etc
    words_second_file = parse_docs1(second_file)
    
    word_list2 = words_second_file.copy()
    for word in words_second_file:
        if word in stop_words:
            word_list2.remove(word)
            
    words_second_file = word_list2
    
    #evaluating first file
    print("Evaluating document {}".format(second_file))
    
    
    #avg word length
    avg_word_length2 = avg_word_length(words_second_file)
    print("1. Average word length: {:.2f}".format(avg_word_length2))
    
    #ratio for the distinct words to total words
    ratio_word2 = word_ratio(words_second_file)
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio_word2))

    #word sets
    print("3. Word sets for document {}:".format(second_file))
    words_pairs2, ratio2 = word_pairs_and_ratio(words_second_file, max_sep)
    #make a for loop to get the length of the words, how many words have that length, and the first 6 words. 
    
    max_length2 = 0
    for word in words_second_file:
        if len(word) > max_length2:
            max_length2 = len(word)
    word_lists2 = []
    for x in range(max_length2):
        word_lists2.append([])
    
    for word in words_second_file:
        word_lists2[len(word) - 1].append(word)
        
    for i in range(len(word_lists2)):
        word_lists2[i] = sorted(list(set(word_lists2[i])))
        
    for i in range(len(word_lists2)):
        temp = []
        flag = False
        if len(word_lists2[i]) > 6:
            flag = True
            for j in range(len(word_lists2[i])):
                if j < 3:
                    temp.append(word_lists2[i][j])
            temp.append('...')
            temp += word_lists2[i][-3:]
        if len(word_lists2[i]) == 0:
            print("{:>4}:   {}:".format(i + 1, len(word_lists2[i])))
        elif len(word_lists2[i]) >= 10:
            if flag == False:
                print("{:>4}:  {}: {}".format(i + 1, len(word_lists2[i]), ' '.join(word_lists2[i])))
            else:
                print("{:>4}:  {}: {}".format(i + 1, len(word_lists2[i]), ' '.join(temp)))
        else:
            if flag == False:
                print("{:>4}:   {}: {}".format(i + 1, len(word_lists2[i]), ' '.join(word_lists2[i])))
            else:
                print("{:>4}:   {}: {}".format(i + 1, len(word_lists2[i]), ' '.join(temp)))
        #print(words)
        
    
    
    #word pairs
    print("4. Word pairs for document {}".format(second_file))
    
    
    #call the word pairs function
    word_pairs2, dist_ratio2 = word_pairs_and_ratio(words_second_file, max_sep)

    #list(no_duplicates1)
    #len of pairs to get the number of pairs but only want to print the first 10
    word_pairs2 = list(set(word_pairs2))
    if len(word_pairs2) >= 10:
        print("  {:>2} distinct pairs".format(len(word_pairs2)))
    else:
        print(" {:>2} distinct pairs".format(len(word_pairs2)))
    
    #It should also output the first 5 word pairs in alphabetical order
    word_pairs2 = sorted(word_pairs2)
    if len(word_pairs2) <= 5:
        for pair in word_pairs2:
            print("  {} {}".format(pair[0], pair[1]))
    else:
        count = 0
        for pair in word_pairs2:
            if count < 5:
                print("  {} {}".format(pair[0], pair[1]))
                count += 1
        print("  ...")
    #It should also output the last 5 word pairs in alphabetical order
        count = 0
        position = 0
        for pair in word_pairs2:
            position += 1
            if count < 5 and position + 5 >= len(word_pairs2) + 1:
                print("  {} {}".format(pair[0], pair[1]))
        
        
        
    #ratio of word pairs 
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(dist_ratio2))

    print()
    
    #Jaccard Similairity
    print("Summary comparison")
    #checks to see if the word length for file 2 is longer or shorter than file 1
    if avg_word_length2 > avg_word_length1:
        long_short = "longer"
        print("1. {} on average uses {} words than {}".format(second_file, long_short, first_file))
    else:
        long_short = "longer"
        print("1. {} on average uses {} words than {}".format(first_file, long_short, second_file))
    
    
    
    #need to get overall word use similairty. need to make set1 and set2 for the function to work. goes through each words in the first and second files and makes a set for each
    
    #call jaccard
    jaccard = jaccard_similarity(words_first_file, words_second_file)
    print("2. Overall word use similarity: {:.3f}".format(jaccard))
    
    print("3. Word use similarity by length:")
    #make a for loop for each word sets then make a set for each words1 and words2 then call the jaccard function
    biggest_word_length = max([max_length, max_length2])
    smallest_word_length = min([max_length, max_length2])
    for i in range(biggest_word_length):
        if i <= smallest_word_length - 1 and i != biggest_word_length - 1:   
            word_use_jaccard = jaccard_similarity(word_lists1[i], word_lists2[i])
            print("{:>4}: {:.4f}".format(i + 1, word_use_jaccard))
        else:
            print("{:>4}: {:.4f}".format(i + 1, 0))
    
    
    #word pair similarity. make the pair calls sets then call the jaccard function
    word_pair_similarity = jaccard_similarity(word_pairs1, word_pairs2)
    print("4. Word pair similarity: {:.4f}".format(word_pair_similarity))
    
    
    


