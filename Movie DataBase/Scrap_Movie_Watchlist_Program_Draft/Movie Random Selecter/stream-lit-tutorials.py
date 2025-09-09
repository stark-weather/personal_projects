import streamlit as st
import pandas as pd
# Initialize Variables 
list_of_movies = []
new_movie_dict = {}

# Text input
movie_input = st.text_input("Enter a movie: ")
genre_input = st.selectbox(
    "Select a genre:",
    ("Action", "Horror", "Thriller", "Romance", "Comedy")
)

new_movie_dict['Title'] = movie_input
new_movie_dict['Genre'] = genre_input
list_of_movies.append(new_movie_dict)
print(list_of_movies)

