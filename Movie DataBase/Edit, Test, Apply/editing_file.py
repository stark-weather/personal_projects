"""Editing File"""
import requests
import json
import string
from randomize_movie_copy import randomize_movie
from api_fetch_copy import call_to_api

# NOTE: TODOs for program
# TODO: 1) Create database and add saved movies 
# TODO: 2) Add -> seen_or_not_seen, my_ratings to database table 
# TODO: 3) Edit table of movies in database to allow user to rate movies and see if the user has seen the movie or not
# TODO: 4) Display dataframe of current watchlist (?)

def find_movie(search_movie):
    """
    Function finds all movies similar or exactly to user search

    Parameter:
        search_movie (str) : user input of the movie there are searching for 

    Return: 
        list_of_movies_searched ([dict]) : list of dictionaries containing data of the searched movies
    """
    # INFO: Remove all punctuations
    deletion = str.maketrans("", "", string.punctuation) # NOTE: string.punctuation = '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
    user_movie_title = search_movie.lower().translate(deletion)

    # NOTE: Initialize all variables needed
    # Adds all movies similar to movie title search to empty list
    list_of_movies_searched = []
    list_of_movie_titles = []
    # List of dictionaries that hold the data that is needed 
    # INFO: results is a list of dictionaries
    results = call_to_api(search_movie)
    # Data needed to be acquired from the API 
    database_keys = ['original_title', 'id', 'release_date', 'original_language']
    # Search movie titles for matched words
    words_found = True

    # NOTE: Create a list of movies that are similar or match the key words the user searched for
    # Loop through each movie in the results list
    for data_dict in results:
        # INFO: Initialize variables
        dictionaries_of_movies = data_dict
        # Remove all punctuations from and make movie title lowercase
        movie_titles = data_dict[database_keys[0]].lower()
        searched_movie_titles = movie_titles.translate(deletion)
        # Find matching words to check if movie exists
        for key_word in user_movie_title:
            if key_word not in searched_movie_titles:
                words_found = False
                break
        # Find if the search movie title is in the list of movie titles
        if words_found:
            # INFO: Initialize variables 
            add_movie_to_dictionary = {}
            try:
                for db_keys in database_keys:
                    # Creating a new dictionary for every movie 
                    add_movie_to_dictionary[db_keys] = dictionaries_of_movies[db_keys]
            except:
                add_movie_to_dictionary[db_keys] = ""
            # Add the movie titles to a list to ask for user input
            list_of_movie_titles.append(dictionaries_of_movies[database_keys[0]])
            # Add dictionaries of movies searched to a list 
            list_of_movies_searched.append(add_movie_to_dictionary)

    return list_of_movies_searched

def display_list_of_searched_movies(user_movie_title, movies_searched):
    """
    Function displays all the movie titles that are contained from the find_movie() function

    Parameter:
        user_movie_title (str) : the movie title that the user searched
        movies_searched (dict) : dictionary containing the information of the movies searched

    Return:
        movies (list) : list of movie titles only
    """
    # NOTE: Displaying the movies in the key words and let the user add the movies to the file
    movies = []
    print(f"Listed movies of: '{user_movie_title}'")
    # Ask user to pick movie from a list of movies 
    for index in enumerate(movies_searched): # INFO: return tuple(int, dict[str: Any])
        numbers = index[0]
        # Dictionaries containing info of movies
        listed_movies = index[1]
        # Get original title to display
        titles_of_movies = listed_movies['original_title']
        try:
            # Get year from release date to display 
            release_year = listed_movies['release_date'][0:4]
        except (IndexError, KeyError) as multiple_errors:
            release_year = ""
        print(f"{numbers}. {titles_of_movies} ({release_year})")
        movies.append(titles_of_movies)

    return movies

def user_selection(search_movie):
    """
    Function ask user to pick movie(s) from a displayed list of movie titles collected from the user search

    Parameter:
        search_movie (str) : user input of the movie there are searching for 

    Return:
        database_watchlist (list) : list of user selected movies 
    """
    # NOTE: User adds selection(s) of movies to a list to save to a file
    list_of_movies_searched = find_movie(search_movie)
    movies = display_list_of_searched_movies(search_movie, list_of_movies_searched)
    stopper = False
    # INFO: Initialize variable
    database_watchlist = []
    while not stopper:
        # Ask user to select a movie
        select_a_movie = input(f"Select a movie (e.g. 1): ")
        if select_a_movie.lower() == 'done':
            stopper = True
        else:
            try:
                # Try to convert user input into int
                selected_movie = int(select_a_movie)
                # Select movie based on user input 
                for movie_index in range(len(movies)):
                    if selected_movie == movie_index:
                        final_selected_movie = list_of_movies_searched[movie_index]
                        database_watchlist.append(final_selected_movie)
            except ValueError as value_error:
                print("Invalid input. Enter a number to select a movie")
                print(f"{value_error} has occurred.")
    
    return database_watchlist

def read_json_file():
    """
    Function reads a JSON file containing a list of dictionaries of movie information

    Return
        read_data (list) : list of dictionaries of movie information
    """
    # NOTE: Reading a JSON file to store and use movie list 
    # Read JSON file
    with open("test_movie_list.json", 'r') as read_json:
        read_data = json.load(read_json)

    return read_data

def write_to_json_file(search_movie):
    """
    Function writes to a JSON file to save a list of user selected movies 

    Parameter:
        search_movie (str) : user input of the movie there are searching for 
    """
    database_watchlist = user_selection(search_movie)
    read_data = read_json_file()
    # Append dictionary to data
    read_data.extend(database_watchlist)
    # Write to a JSON file 
    with open("test_movie_list.json", 'w') as write_to_json:
        json.dump(read_data, write_to_json, indent=4)

def main():
    """ Main Function """
    # Display options for user selections
    print("Opening Watchlist...")
    print("1. Search and Save Movie\n" \
    "2. Randomize Movie from Watchlist\n" \
    "3. View Watchlist (Coming Soon...)\n" \
    "4. Exit")
    stopper = False
    while not stopper:
        try:
            # User input of a selection
            user = int(input(f"Select an option (e.g. 1):  "))
            # Allows user to search, find, and save a movie to a JSON file
            if user == 1:
                search_movie = input("Enter a movie: ")
                write_to_json_file(search_movie)
                print("Movie has been added to the watchlist.")
            # Allows user to randomize movie
            elif user == 2:
                randomize_movie()
            # Allows user to view the current movie watchlist
            elif user == 3:
                print("Coming Soon...")
            # Exits the program
            elif user == 4:
                print("Come Again!")
                stopper = True
            else:
                print(f"Option {user} does not exist.")            
        except TypeError as type_error:
            print("Invalid input. Enter a number.")

if __name__ == '__main__':
    main()