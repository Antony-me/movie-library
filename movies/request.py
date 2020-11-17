import urllib.request,json
from .models import Movie



# Getting api key
api_key ='5aa4c08c5714786bc0d458cdbe0d525e'

# Getting the movie base url
base_url ='https://api.themoviedb.org/3/movie/trending/movie/week_key=5aa4c08c5714786bc0d458cdbe0d525e'


def get_onlinemovies(trending):
    '''
    Function that gets the json responce to our url request
    '''
    with urllib.request.urlopen('https://api.themoviedb.org/3/movie/popular?api_key=5aa4c08c5714786bc0d458cdbe0d525e') as url:
        get_movies_data = url.read()
        movie_results = json.loads(get_movies_data)

    return movie_results
        

def get_genre(genre):
    '''
    Function that gets the json responce to our url request
    '''

    with urllib.request.urlopen('https://api.themoviedb.org/3/genre/movie/list?api_key=5aa4c08c5714786bc0d458cdbe0d525e') as url:
        get_movies_data = url.read()
        movie_genre = json.loads(get_movies_data)

    return movie_genre



def get_searched_movie(search):
    '''
    Function that gets the json responce to our url request
    '''

    with urllib.request.urlopen('https://api.themoviedb.org/3/search/movie?api_key=5aa4c08c5714786bc0d458cdbe0d525e&language=en-US&query=endgame') as url:
        get_movies_data = url.read()
        movie_searched = json.loads(get_movies_data)

    return movie_searched
