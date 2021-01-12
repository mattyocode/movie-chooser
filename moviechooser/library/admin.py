from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, Actor, Director

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)