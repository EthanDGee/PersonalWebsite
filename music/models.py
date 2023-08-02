from django.db import models
import datetime
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=144)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=144)
    description = models.CharField(max_length=500)
    favorite = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre)
    profile = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=144)
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre)
    pub_date = models.DateField()
    description = models.CharField(max_length=500)
    favorite = models.BooleanField(default=False)
    review_date = models.DateField(default=datetime.date.today)
    art = models.ImageField(upload_to='images')

    def stringArtists(self):
        # return type(self.artists)

        # artist_string = ""
        # if len(self.artists) > 1:
        #     for x in range(len(self.artists)-2):
        #         artist_string += self.artists[x]+', '
        #     artist_string += "and " + self.artists[-1]
        # else:
        #     artist_string = self.artists[0]

        # return artist_string
        return "Work in progress"

    def __str__(self):
        return f'{self.title} by {self.stringArtists()}'
