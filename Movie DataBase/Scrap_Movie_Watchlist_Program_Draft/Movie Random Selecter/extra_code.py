import json
import pandas as pd
from movie_list import data_movie_list
from movie_list import movie_list

#TODO: Implement new code into the block of code above
#TODO: write movie_list to a file to save updates for future randomization

# Update the first dictionary after updating the second dictionary 
# Initialize variables 
copy_of_data_movie_list = data_movie_list #INFO: List of dictionaries
copy_of_movie_list = movie_list #INFO: Dictionary of genre : [list of movies]

print(copy_of_movie_list)
print(copy_of_data_movie_list)

stopper = False 
while not stopper:    
    # Getting user input and adding to current dictionary 
    data_to_collect = ['Title', 'Genre']
    # Initialize variables
    # NOTE: Creates a new temporary dictionary to add to the current list of dictionaries of movies 
    new_movie_dict = {}
    # NOTE: Empty list to store movie title and genre tittle
    movie_genre_list = []
    # NOTE: Flag if movie is already in the list
    data_movie_found = False
    # NOTE: Flag if movie is already in the list
    logic_movie_found = False
    # Get key, value information on movies and genre for list of movies
    print('Please enter the correct information')
    for key in data_to_collect:
        dict_value = input(f"Enter {key} of your movie: ").title()
        

print(copy_of_movie_list)
print(copy_of_data_movie_list)