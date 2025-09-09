import json
import pandas as pd
import random as r
import streamlit as st

#INFO: Initializing global variables 
# Reading JSON file
with open('Logic_Movie_List.json', 'r') as reading_logic_file:
    read_logic = json.load(reading_logic_file)
with open('movie_list.json', 'r') as read_data_file:
    read_data = json.load(read_data_file)
    copy_of_movie_list = read_logic
    copy_of_data_movie_list = read_data
    keys_of_copy_of_movie_list = list(copy_of_movie_list.keys())
    # Write to JSON file
    with open('movie_list.json', 'w') as json_file:
        # INFO: Update the first dictionary after updating the second dictionary 
        # Use to break out of the loop
        stopper = False 
        while not stopper:    
            # Getting user input and adding to current dictionary 
            data_to_collect = ['Title', 'Genre']
            # Initialize variables
            # NOTE: Creates a new temporary dictionary to add to the current list of dictionaries of movies 
            new_movie_dict = {}
            # NOTE: Empty list to store movie title and genre tittle
            movie_genre_list = []
            # Get key, value information on movies and genre for list of movies
            print('Please enter the correct information')
            for key in data_to_collect:
                dict_value = input(f"Enter {key} of your movie: ")
                # Capitalize user entries 
                values = dict_value.title()
                # Update the dictionary in memory 
                new_movie_dict[key] = values
                # Adding movie title and genre title to an empty list
                movie_genre_list.append(values)
            # Adding newly created movie and genre dictionary to current list of movies
            copy_of_data_movie_list.append(new_movie_dict)
            # Assigne user input to variables to update logic movie list
            movie_title = movie_genre_list[0]
            genre_title = movie_genre_list[1]
            # Add movie to the correct genre 
            #TODO: Add a conditional to see if the user input of movie title and genre title is already in the movie list
            # Check if user typed 'done' to quit entering movies 
            exit_from_typing = input("Enter 'done' when you finish enter your movies: ")
            if exit_from_typing.lower() == 'done':
                stopper = True
        json.dump(read_data, json_file)
#INFO: Writing movie_list to file
# Write movie_list {'genre' : [list of movies]} to JSON file 
with open('Logic_Movie_List.json', 'w') as writing_logic_file:
    json.dump(copy_of_movie_list, writing_logic_file)

