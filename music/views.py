from django.shortcuts import render
from .models import Album, Artist, Genre

# Create your views here.


def homepage(request):
    return render(request, 'music/homepage.html')


def all_data(request):
    colors = ["red", "crimson", "firebrick", "tomato", "coral", "salmon", "indianred", "orange", "orangered", "darkorange", "chocolate", "sandybrown", "yellow", "gold", "goldenrod", "khaki", "palegoldenrod", "green", "lime", "limegreen",
                  "forestgreen", "seagreen", "olive", "olivedrab", "blue", "dodgerblue", "royalblue", "steelblue", "skyblue", "lightblue", "indigo", "darkslateblue", "slateblue", "mediumslateblue", "violet", "purple", "magenta", "fuchsia", "darkviolet", "darkorchid"]
 
    albums = Album.objects.all()
    artists = Artist.objects.all()
    genres = Genre.objects.all()
    return render(request, 'music/all_data.html', {'albums': albums, 'artists': artists, 'genres': genres, 'colors': colors})
