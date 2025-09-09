import random as r 
"""Basic Random Movie Selecter"""
# 1) Select a genre randomly 
# 2) Once the genre is selected, it is going to randomize from the genre category

# List of movies and movie genres
### Save dictionary either as dataframe or some sort of file
movie_list = {
    'Action' : ['Ne Zha 2', 'John Wick 4'],
    'Comedy' : ['Cruella', 'Rush Hour 2'],
    'Romance' : ['My Oxford Year', 'Paper Town'],
    'Horror' : ['The Shinning', 'Lolita']
}
movie_genres = list(movie_list.keys())

### Option 1 - Randomize Genre and Movie
# Randomize movie genres 
genre_selection = r.choice(movie_genres)
# Select movie based on randomized genre
movie_selection = r.choice(movie_list[genre_selection])

### Option 2 - User Pick Genre
# Continuous loop if user enters wrong input
stop = True
while not stop:
    print("Genres: Action, Comedy, Romance, Horror")
    user_input = input("Select a genre: ")
    # Capitalize input to match dictionary key 
    user_select_genre = user_input.capitalize()
    if user_select_genre in movie_genres:
        movie_selected = r.choice(movie_list[user_select_genre])
        #print(movie_selected)
        stop = True
    else:
        print(f"{user_select_genre} is not a genre. Please try again.")

### Add Movies to List 
user_input = input("Enter a movie and genre (movie, genre): ")
input_list = user_input.split(',') # Split input into a list 
# Separate input into movie and genre 
movie_entry = input_list[0].title() # Capitalize the first word of each word of the movie title 
genre_entry = input_list[1]
# Check if there is a space before the genre word 
if ' ' in genre_entry:
    genre = genre_entry.replace(' ', '').capitalize()
# Check to match genre input with listed genre
if genre in movie_genres:
    movie_list[genre].append(movie_entry)
print(movie_list)

    
### Print station
#print(genre_selection)
#print(movie_selection)
