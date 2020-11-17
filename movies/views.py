from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Movie
from .request import get_onlinemovies, get_genre, get_searched_movie



# Create your views here
def movies(request):

    '''
    View root page function that returns the index page and its data
    '''

    # Getting trendy movie
    movie_list = get_onlinemovies()

    movies= movie_list['results']
 

    title = 'Home - Welcome'

    # search_movie = request.args.get('movie_query')

  
        
    return render(request, 'All_movies/movies.html', {'movies':movies, 'title' : title })


# Create your views here
def genre(request):

    '''
    View root page function that returns the index page and its data
    '''

    # Getting trendy movie
    genre_list = get_genre('Action')

    movies= genre_list['genres']
 

    title = 'categories'

    # search_movie = request.args.get('movie_query')

  
        
    return render(request, 'All_movies/genre.html', {'movies':movies, 'title' : title })


def searched_movie(request):

    '''
    View root page function that returns the index page and its data
    '''

    # Getting trendy movie
    searched_list = get_searched_movie('search')

    movies= searched_list['results']
 

    title = 'searched movies'

    # search_movie = request.args.get('movie_query')

  
        
    return render(request, 'All_movies/search.html', {'movies':movies, 'title' : title })





def movie_description(request):
    
    return render(request, 'all_movies/description.html', {'images': images})

