from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='music'),
    path('all_data', views.all_data, name='all_data'),
    path('artists/', views.artist_list, name="artists_list"),
    path('artists/<str:artist_name>/', views.artist, name='artist_profile'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/<str:album_title>/', views.album, name='album'),
    path('genres/', views.genre_list, name='genre_list'),
    path('favorites/', views.favorites, name='favorites'),
    path('test', views.test, name='test'),
]

