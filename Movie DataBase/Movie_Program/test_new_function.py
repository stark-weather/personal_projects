import pymysql
from movie_functions import *
import pandas as pd
""" 
# INFO: Creates a new function to allow user to view watchlis 
# NOTE: Watchlist => DataFrame
def view_watchlist():
    data = read_json_file()
    watchlist_table = pd.DataFrame(data)

    return watchlist_table

print(view_watchlist()) """

def connect_to_database():
    data = read_json_file()
    # Connect to database 
    db_connection = pymysql.connect(host="localhost",
                                   port=3306,
                                   user="root",
                                   password="k#x#TuB#gF7j%K",
                                   database="movie_watchlist")
    cursor = db_connection.cursor()
    print("Database Connected")
    
    cursor.execute("SELECT * FROM watchlist;")
    results = cursor.fetchall()

    for movie in data:
        sql = "INSERT INTO watchlist (Original_Title, Movie_ID, Release_Date, Original_Language) VALUES (%s, %s, %s, %s)"
        values = (
            movie["original_title"],
            movie["id"],
            movie["release_date"].split("T")[0],
            movie["original_language"]
        )
        cursor.execute(sql, values)  

    db_connection.commit()

    # Write code so that it doesn't add the same movies twice into the table in the database