# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:37:12 2023

@author: jackm
"""

import json

#only need to work in the main
if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    #input for min  year
    min_year = input("Min year => ").strip()
    min_year = int(min_year)
    print(min_year)
    #input for max year
    max_year = input("Max year => ").strip()
    max_year = int(max_year)
    print(max_year)
    #input for weight imdb
    w1 = input("Weight for IMDB => ").strip()
    
    print(w1)
    w1 = float(w1)
    #input for weight twitter
    w2 = input("Weight for Twitter => ").strip()
    
    print(w2)
    w2 = float(w2)
    print()
    
    #have a while loop after the inputs
    while True:
        #genre input. have to make it lower then title it to fit the output
        input_genre = input("What genre do you want to see? ").strip()
        
        print(input_genre)
        input_genre = input_genre.lower()
          
        #check to see if genre == 'stop' and break the program
        if input_genre == "stop" or input_genre == "Stop":
            break
        
        print()
        #make a list for the best and worst movies
        best = []
        worst = []
        #get the movie number associated and the info attached. The first dictionary has movie ids as keys
        for movie_number, info in movies.items():
            year = info["movie_year"]
            
            #now after getting the movie year i have to check if its in between the min and max years
            if min_year <= year <= max_year:
                imdb_rating = info["rating"]
                
                #check if the movie number is in the ratings or not because i got an error one of them was not so i need to make a condition
                if movie_number not in ratings:
                    continue
                twitter = ratings[movie_number]
            
                #If a movie is not rated in Twitter, or if the Twitter rating has fewer than 3 entries, skip the movie
                if (len(twitter) < 3):
                    continue
                
                
                #calculations
                average_twitter_rating = sum(twitter) / len(twitter)
                #For each movie, compute the combined rating for the movie as follows: (w1 * imdb_rating + w2 * average_twitter_rating) / (w1 + w2)
                combined_rating = (w1 * imdb_rating + w2 * average_twitter_rating) / (w1 + w2)
                
                #get_genre takes the info of the movies.json and get the genre after "genre"
                get_genre = info["genre"]
                #print(get_genre)
                
                if input_genre.title() in get_genre:
                    best.append((combined_rating, [info["movie_year"], info["name"]]))
                    #worst.append((combined_rating, [info["movie_year"], info["name"]]))
        #print(best)           
        if len(best) != 0:
            #sorting it with reverse is the best movie, regular sorting is the worst
            #The TA who i met with told me to use lambda function to fix my issue where the rating was the same and needed to get the second name
            sorted_best = sorted(best, reverse = True, key = lambda x:(x[0], x[1][1]))
            # print(best)
            best = sorted_best[0]
            worst = sorted_best[-1]
            # print(sorted_best)
            
            print("Best:")
            #print(best[0])
            print("        Released in {}, {} has a rating of {:.2f}".format(best[1][0], best[1][1], best[0]))
            print()
            print("Worst:")
            print("        Released in {}, {} has a rating of {:.2f}".format(worst[1][0], worst[1][1], worst[0]))
            print()
        else:
            print("No {} movie found in {} through {}".format(input_genre.title(), min_year, max_year))
            print()
        
        
        
    
        