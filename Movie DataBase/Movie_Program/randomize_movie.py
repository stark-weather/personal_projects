"""Main Randomize File"""
import json
import random as r

def read_json_file():
    # NOTE: Read JSON file to collect data needed 
    with open("get_movie.json", 'r') as read_json:
        read_data = json.load(read_json)

    return read_data

def randomize_movie():
    # NOTE: Initialize variable 
    read_data = read_json_file()
    reroll_count = 0
    stopper = False
    # NOTE: Allows the user to randomize 3 movies 
    while not stopper:
        # Keep count of re-rolls
        reroll_count +=1
        # INFO: Randomizing movie 
        # Create a copy of read data (dictionary)
        list_of_movies = read_data
        # Randomize movie information
        selecting_a_movie = r.choice(list_of_movies)
        list_of_movies.remove(selecting_a_movie)
        # Gets movie title
        movie_title = selecting_a_movie['original_title']
        try:
            # Check if there is a release year to display
            release_year = selecting_a_movie['release_date'][0:4]
        except Exception as e:
            release_year = 'N/A' 
        # Display randomized movie
        print('Randomized Movie:')
        print(f"{movie_title} ({release_year})")
        # Check if the re-roll count is less than 3 
        if reroll_count < 3:
            # User input for reroll
            user_input = input("Do you want to re-roll? (y/n) ")
            # Exits the loop if user types in anything besides 'y'
            if user_input.lower() != 'y':
                stopper = True 
        else:
            # Display messages after 3 re-rolls
            print("No more re-rolls.")
            stopper = True
