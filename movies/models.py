from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_movie_title = models.CharField(max_length=70)
    movie_poster_url = models.CharField( max_length= 200)
    movie_overview = models.CharField( max_length= 200)
  
    @classmethod
    def get_movies(cls):
        all_movies = Movie.objects.all()
        return all_movies

    def __str__(self):
        return self.movie_title

    def save_movie(self):
        self.save()

    def delete_movie(self):
        self.delete()



class Movies:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,id,movie_title,movie_overview,movie_poster):
        self.id =id
        self.movie_title = movie_title
        self.movie_overview = movie_overview
        self.movie_poster_url = "https://image.tmdb.org/t/p/w500/" + poster


        def save_movie(self):
            self.save()
       

