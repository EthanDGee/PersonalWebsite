from django.contrib import admin
from .models import Album, Genre, Artist

models = [Album, Genre, Artist] 
# Register your models here.
admin.site.register(models)