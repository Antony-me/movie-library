from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Movie
from .request import get_onlinemovies, get_genre, get_searched_movie, get_youtube_search



#view function for desplaying treading/popular movies
def movies(request):
    '''
    View root page function that returns the index page and its data
    '''

    # Getting trendy movie
    movie_list = get_onlinemovies('trending')
    movies= movie_list['results']

    title = 'Home - Welcome'

    return render(request, 'All_movies/movies.html', {'movies':movies, 'title' : title })


#view function for desplaying genre-list movies
def genre(request):

    '''
    View root page function that returns the index page and its data
    '''
    genre_list = get_genre('Action')
    movies= genre_list['genres']
 
    title = 'categories'

    return render(request, 'All_movies/genre.html', {'movies':movies, 'title' : title })


#view function for desplaying searched movies
def searched_movie(request):

    '''
    View root page function that returns the index page and its data
    '''
    # Getting searched movie
    searched_result = get_searched_movie('movie')
    movies= searched_result['results']
    title = 'searched movies'
        
    return render(request, 'All_movies/search.html', {'movies':movies, 'title' : title })


#view function for desplaying youtube trailers
def youtube_search(request):

    '''
    View root page function that returns the index page and its data
    '''
    youtube_search = get_youtube_search()
    youtube_searched_movie= youtube_search['items']

    title = 'trailers'
        
    return render(request, 'All_movies/trailers.html', {'movies':youtube_searched_movie, 'title' : title })

#view function for desplaying  movies detailes
def description(request):

    # Getting  movie details
    genre_list = get_genre('Action')
    movies= genre_list['genres']
 
    return render(request, 'All_movies/description.html', {'movies': movies})
