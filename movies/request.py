import urllib.request,json
from .models import Movie
from googleapiclient.discovery import build
import pprint

# youtube  api key

youtube_api_key= 'AIzaSyDlz500SD9WihXvsnn2mUJu9oESpjmiubE'
youtube = build('youtube','v3', developerKey= youtube_api_key)


# movie  api key
api_key ='5aa4c08c5714786bc0d458cdbe0d525e'

# movie base url
base_url ='https://api.themoviedb.org/3/movie/trending/all/week_key=5aa4c08c5714786bc0d458cdbe0d525e'


def remove(string): 
    return string.replace(" ", "+") 

def remove2(string): 
    return string.replace(" ", "_") 

search_movies ='Batman' 
search_movie=remove2(search_movies)


#Method to get popular movies
def get_onlinemovies(trending):
    '''
    Function that gets the json responce to our url request
    '''
    with urllib.request.urlopen('https://api.themoviedb.org/3/movie/popular?api_key=5aa4c08c5714786bc0d458cdbe0d525e') as url:
        get_movies_data = url.read()
        movie_results = json.loads(get_movies_data)

    return movie_results
        

#Method to get genre of movies
def get_genre(genre):
    '''
    Function that gets the json responce to our url request
    '''

    with urllib.request.urlopen('https://api.themoviedb.org/3/genre/movie/list?api_key=5aa4c08c5714786bc0d458cdbe0d525e') as url:
        get_movies_data = url.read()
        movie_genre = json.loads(get_movies_data)

    return movie_genre


#Method to get searched  movies
def get_searched_movie(search):
    '''
    Function that gets the json responce to our url request
    '''
    with urllib.request.urlopen('https://api.themoviedb.org/3/search/movie?api_key=5aa4c08c5714786bc0d458cdbe0d525e&language=en-US&query={}'.format(search_movie)) as url:
        get_movies_data = url.read()
        movie_searched = json.loads(get_movies_data)


    return movie_searched

#Method to get youtube search

def get_youtube_search():
    searched_list = get_searched_movie('search')
    movies= searched_list['results']
    search=movies[0]['title'] 

    search_term=remove(search)
    
    request = youtube.search().list(

        part="snippet",
        q="{}".format(search_term),
        maxResults=5,
        # type="video",
        # videoType= "movie"

    )
    response = request.execute()
    
    return response
   
