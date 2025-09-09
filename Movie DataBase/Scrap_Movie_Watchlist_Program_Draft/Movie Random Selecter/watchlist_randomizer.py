"""Simple Random Movie Selection Program"""
import csv
import random as r 
import pandas as pd
import streamlit as st
from movie_list import movie_list
from movie_list import data_movie_list

#NOTE: Global variables
#INFO: Randomization logic dictionary 
lst_of_movies = movie_list
movie_genres = list(movie_list.keys())

#INFO: Display and database dictionary
data_base = data_movie_list

def randomize_movie():
    "Pick movie based on randomized genre"
    # Convert dict.keys() into a list of genre for randomization
    list_movie_genre = movie_genres
    # Randomize a movie genre 
    randomized_genre = r.choice(list_movie_genre)
    # Select movie based on randomized genre
    randomized_movie = r.choice(movie_list[randomized_genre])

    return randomized_movie

def pick_movie_genre():
    "Pick movie based on user genre entry"
    # List all the different types of genres available
    print("Genres:")
    list_of_movie_genres = movie_genres
    for genre in list_of_movie_genres:
        print(genre)
    stopper = False
    while not stopper:
        # Get user input for a genre
        user_selection = input("Select a genre (eg. Action): ").capitalize()
        # Ask user to input again if it is an invalid input
        if user_selection.isdigit():
            print("Invalid input. Please enter a genre.")
        else:
            # Check if the user entered a valid genre
            if user_selection in list_of_movie_genres:
                # Select random movie based on the user entered genre
                random_movie_selection = r.choice(movie_list[user_selection])
                stopper = True 
            else:
                print(f"{user_selection} is not in the genre list.")
    
    print()
    print("Random Movies Selected: ")
    return random_movie_selection

def add_movie():
    "Add movie to current movie list"
    stopper = False 
    while not stopper:
        # Get user to input movie and genre to add to the current movie list
        print("Type 'done' when you are done adding your movies.")
        user_movie_input = input("Enter a movie and genre (eg. movie, genre): ").lower().strip()
        # Check if user input is valid 
        if user_movie_input.isdigit():
            print("Invalid input. Please enter a genre.")
        elif user_movie_input == 'done':
            user_movie_input = input("Thank you for adding your movies!\n" \
            "Do you want to see the new movie list? (y/n): ").lower()
            if user_movie_input == 'y':
                #INFO: Additional added movies and genres are built into memory
                #TODO: Fix built in memory problem for GUI program
                view_movie_list()
            elif user_movie_input == 'n':
                print("Come Again!")
                stopper = True
            else:
                print("Invalid input. Please try again.")
        else:
            # Separate user input into a list containing movie and genre
            user_input = user_movie_input.split(',')
            movie_entry = user_input[0].title() # Capitalize the title of the movie
            genre_entry = user_input[1]
            # Check if there is a space before the genre to get rid of it
            if ' ' in genre_entry:
                genre = genre_entry.replace(' ', '').capitalize() # Capitalize the first letter of the genre to match the keys of the movie list
            # Check to match genre input with listed genre 
            if genre in movie_genres:
                lst_of_movies[genre].append(movie_entry)
            
def view_movie_list():
    "View movie list"
    #TODO: Create dataframe for user to view 
    print()
    for genre, movies in lst_of_movies.items():
        print(f"{genre} : {movies}")
    print()
    
    """# Creates dataframe/table of movies and genres
    #TODO: Make dataframe work even with different lengths of rows and columns 
    # Import from movie_list_file.csv
    df = pd.DataFrame(lst_of_movies)

    return df
    """
    return None

def run_program():
    "Main program that runs everything"
    # Title of the program
    print("-Welcome to the Movies-")
    # Stopper to exit the program
    break_point = False 
    while not break_point:
        # Main selections 
        print()
        print("1. Pick movie")
        print("2. Add movie to current movie list")
        print("3. View current movie list")
        print("4. Exit")
        print()
        # User input for a selection
        user_input = input("Select an option (1-5): ")
        try:
            # Convert user input into a integer
            option = int(user_input)
        # Prints out message if an error occurs
        except ValueError as value_error:
            print("Invalid input. Please enter a number.")
            print(f"Error: {value_error}")
        
        if option == 1:
            print("Would you like:\n" \
            "1. Randomize a movie from a randomize genre\n" \
            "2. Pick a movie from a selected genre")
            # User input for a selection
            second_user_input = input("Select an option (1-2): ")
            try:
                # Convert user input to integer
                second_option = int(second_user_input)
            # Prints out message if an error occurs
            except ValueError as value_error_two:
                print()
                print("Invalid input. Please enter a number.")
                print(f"Error: {value_error_two}")
                print()
            # Select random movie from a randomized genre
            if second_option == 1:
                print()
                print("Random Movie Selected:")
                print(randomize_movie())
                print()
                # Breaks out of the program
                break_point = True
            # Select random movie from user entered genre
            if second_option == 2:
                #pick_movie_genre() 
                print()
                print(pick_movie_genre())
                print()
                # Breaks out of the program
                break_point = True
        # Allows user to add more watch list movies to current movie list
        elif option == 2:
            add_movie()
        # Allows user to view current movie list
        elif option == 3:
            view_movie_list()
            continue
        # Exits the program
        elif option == 4:
            print()
            print("Goodbye! Have a good day!")
            print()
            break_point = True
        else:
            print("Invalid input. Please try again.")

def main():
    "Main function"
    run_program()

    ### i) Write and read file function(s) 
    ### ii) Update two dictionaries
    ###     - Save and update data to file
    ### iii) Create another dictionary (movie -> genre); easier to display (DataFrame - pandas) and save to database 
    ### iv) Create database to save new dictionary file (SQL)
    ### v) Create a user-interface with streamlit 

if __name__ == '__main__':
    main()