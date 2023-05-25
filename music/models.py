from django.db import models

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

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=144)
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre)
    pub_date = models.DateField()
    description = models.CharField(max_length=500)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.artists}'
