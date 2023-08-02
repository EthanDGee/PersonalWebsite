from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Genre
# Create your views here.


def homepage(request):
    latest_albums = Album.objects.order_by('-review_date')[0:6]
    latest_favorite = Album.objects.filter(
        favorite='True').order_by('-review_date')[0]
    return render(request, 'music/homepage.html', {'favorite': latest_favorite, 'latest_albums': latest_albums})


def all_data(request):
    colors = ["red", "crimson", "firebrick", "tomato", "coral", "salmon", "indianred", "orange", "orangered", "darkorange", "chocolate", "sandybrown", "yellow", "gold", "goldenrod", "khaki", "palegoldenrod", "green", "lime", "limegreen",
              "forestgreen", "seagreen", "olive", "olivedrab", "blue", "dodgerblue", "royalblue", "steelblue", "skyblue", "lightblue", "indigo", "darkslateblue", "slateblue", "mediumslateblue", "violet", "purple", "magenta", "fuchsia", "darkviolet", "darkorchid"]

    albums = Album.objects.all()
    artists = Artist.objects.all()
    genres = Genre.objects.all()
    return render(request, 'music/all_data.html', {'albums': albums, 'artists': artists, 'genres': genres, 'colors': colors})


def artist(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)

    return render(request, 'music/artist.html', {'artist': artist})


def album(request, album_title):
    album = get_object_or_404(Album, title=album_title)
    return render(request, 'music/album.html', {'album': album})


def test(request):
    color_list = ["red", "crimson", "firebrick", "tomato", "coral", "salmon", "indianred", "orange", "orangered", "darkorange", "chocolate", "sandybrown", "yellow", "gold", "goldenrod", "khaki", "palegoldenrod", "green", "lime", "limegreen",
                  "forestgreen", "seagreen", "olive", "olivedrab", "blue", "dodgerblue", "royalblue", "steelblue", "skyblue", "lightblue", "indigo", "darkslateblue", "slateblue", "mediumslateblue", "violet", "purple", "magenta", "fuchsia", "darkviolet", "darkorchid"]
    return render(request, 'music/test.html', {'colors': color_list})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'music/genre_list.html', {'genres': genres})


def favorites(request):
    albums = Album.objects.filter(favorite='True').order_by('-review_date')
    artists = Artist.objects.filter(favorite='True').order_by('name')
    return render(request, 'music/favorites.html', {'albums': albums, 'artists': artists})
