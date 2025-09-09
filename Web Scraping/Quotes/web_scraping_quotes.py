"""Simple Quote Web Parsing Project"""
# NOTE: Parses through a website to collect 10 inspirations quotes and the author that said the quote

import requests
import pandas as pd
import random as r
from bs4 import BeautifulSoup

def get_quotes_n_authors():
    """
    Function parses a quote website of inspirational quotes to gather all 10 quotes and the authors that said the quotes

    Return:
        container, inspirational_quotes (tuple) : a tuple holding a list of dictionaries, container, of authors with their quotes and a dictionary[str: []], inspirational_quotes, of authors and quotes
    """
    # URL to the quote website for inspirational quotes
    URL = 'https://quotes.toscrape.com/tag/inspirational'

    # INFO: Initialize variables
    # List of quotes
    lst_of_quotes = []
    # List of authors
    lst_of_author = []
    # List of dictionaries storing each author and quote
    container = []

    # Get page content and convert it to text
    quote_content = requests.get(URL)
    # Get html formate of webpage 
    quote_text = quote_content.text
    # Get page status 
    status_code = quote_content.status_code
    # Parse to readable code
    soup = BeautifulSoup(quote_text, 'html.parser')
    # Find all quotes in div
    quotes = soup.find_all("div", class_='quote')
    # Loops through the div class that contains all the quotes to parse
    for many_quotes in quotes: 
        # INFO: Initialize variables
        author_n_quotes = {}
        # Get all quotes
        quote = many_quotes.find('span', class_='text').text
        # Get all author associated to the quotes
        author = many_quotes.find('small', class_='author').text
        # Add the authors and quotes to the correct list
        lst_of_quotes.append(quote)
        lst_of_author.append(author)
        # Create a dictionary for each author of the quotes
        author_n_quotes[author] = quote
        # Add the dictionary to an empty list
        container.append(author_n_quotes)

    # Dictionary to store the author and the quotes they said
    inspirational_quotes = {
        'Author': lst_of_author,
        'Quotes': lst_of_quotes
    }   
    return container, inspirational_quotes

def create_dataframe():
    """
    Function creates a dataframe of the authors and quotes said

    Return
        dataframe (panda.DataFrame) : a dataframe consisting of authors and their quotes
    """
    tup_of_data = get_quotes_n_authors()
    inspirational_quotes = tup_of_data[1]
    # Creates a dataframe of the authors who said each quotes
    dataframe = pd.DataFrame(inspirational_quotes)
    
    print(dataframe)

def randomize_quote():
    """
    Function randomizes an inspirational quote
    """
    tup_of_data = get_quotes_n_authors()
    container = tup_of_data[0]
    # Randomize quote
    rand_quote = r.choice(container)
    for auth, value in rand_quote.items():
        print(f"{auth} said, {value}")

    return None

def main():
    "Main Function"

    print("Welcome to the Quote Table")
    print("1. View Table \n" \
    "2. Randomize Quote")
    user = input("Select an option: ")
    try:
        option = int(user)
        if option == 1:
            create_dataframe()
        elif option == 2:
            randomize_quote()
    except Exception as e:
        print("Invalid Input. Try Again.")

if __name__ == "__main__":
    main()