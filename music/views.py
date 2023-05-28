from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Genre
# Create your views here.

def homepage(request):
    latest_albums = Album.objects.order_by('-review_date')[:6]
    
    return render(request, 'music/homepage.html', { 'latest_albums': latest_albums})


def all_data(request):
    colors = ["red", "crimson", "firebrick", "tomato", "coral", "salmon", "indianred", "orange", "orangered", "darkorange", "chocolate", "sandybrown", "yellow", "gold", "goldenrod", "khaki", "palegoldenrod", "green", "lime", "limegreen",
                  "forestgreen", "seagreen", "olive", "olivedrab", "blue", "dodgerblue", "royalblue", "steelblue", "skyblue", "lightblue", "indigo", "darkslateblue", "slateblue", "mediumslateblue", "violet", "purple", "magenta", "fuchsia", "darkviolet", "darkorchid"]

    albums = Album.objects.all()
    artists = Artist.objects.all()
    genres = Genre.objects.all()
    return render(request, 'music/all_data.html', {'albums': albums, 'artists': artists, 'genres': genres, 'colors': colors})

def artist(request, artist_name):
    artist =  get_object_or_404(Artist, name=artist_name)
    return render(request, 'music/artist.html', {'artist': artist})

def album(request, album_title):
    album =  get_object_or_404(Album, title=album_title)
    return render(request, 'music/album.html', {'album': album})


def test(request):
    color_list = ["red", "crimson", "firebrick", "tomato", "coral", "salmon", "indianred", "orange", "orangered", "darkorange", "chocolate", "sandybrown", "yellow", "gold", "goldenrod", "khaki", "palegoldenrod", "green", "lime", "limegreen", "forestgreen", "seagreen", "olive", "olivedrab", "blue", "dodgerblue", "royalblue", "steelblue", "skyblue", "lightblue", "indigo", "darkslateblue", "slateblue", "mediumslateblue", "violet", "purple", "magenta", "fuchsia", "darkviolet", "darkorchid"]
    return render(request, 'music/test.html', {'colors': color_list})
