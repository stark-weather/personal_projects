"""API File"""
import requests

def call_to_api(search_movie):
    API_KEY = 'f3f1214088405be2b2f3dc84ab3513df'
    # Contruct Request 
    URL = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={search_movie}'
    params = {
        'api-key' : API_KEY
    }
    # Make call to API 
    get_request = requests.get(URL, params=params)
    json_file = get_request.json()
    movie_results = json_file['results']
    status_code = get_request.status_code
    try:
        if status_code == 200:
            print(f"Status Code: {status_code}")
    except Exception as e:
        print(f"Status Code Error: {status_code}")
        print(f"Error: {e}")
    
    return movie_results