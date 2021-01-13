from django.db import models

from moviechooser.library.models import Genre

class MovieChoice(models.Model):
    GENRE_SELECT = [(genre.id, genre.name) for genre in Genre.objects.all()]
    genre = models.CharField(max_length=20, choices=GENRE_SELECT)