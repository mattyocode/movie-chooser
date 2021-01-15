# from django.db import models

# from moviechooser.library.models import Genre, Movie

# class MovieChoice(models.Model):
#     GENRE_SELECT = [(genre.id, genre.name) for genre in Genre.objects.all()]

#     genre = models.CharField(max_length=20, choices=GENRE_SELECT)
#     sorted_runtimes = [movie.runtime for movie in Movie.objects.order_by('runtime')]
#     min_runtime = sorted_runtimes[0]
#     max_runtime = sorted_runtimes[-1]