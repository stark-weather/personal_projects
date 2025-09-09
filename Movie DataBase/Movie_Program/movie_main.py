"""Editing File"""
from randomize_movie import randomize_movie
from movie_functions import write_to_json_file

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