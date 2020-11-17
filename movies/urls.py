from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#..............

urlpatterns=[

    url('^$',views.movies,name='movies'),
    # url(r'^search/', views.search_results, name='search_results'),
    url(r'^genre/', views.genre, name='genre'),
    url(r'^searched_movie/', views.searched_movie, name='searched_movie'),

    
  

]