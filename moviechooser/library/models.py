# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movie(models.Model):
    """Model representing a movie - selected fields from OMDB."""
    imdb_id = models.CharField(primary_key=True, max_length=12)
    title = models.CharField(max_length=200)
    rated = models.CharField(max_length=10, blank=True, null=True)
    released = models.DateField()
    runtime = models.IntegerField()
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=45)
    writer = models.CharField(max_length=75)
    actors = models.CharField(max_length=100)
    plot = models.CharField(max_length=500)
    language = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    poster_url = models.CharField(max_length=200)
    imdb_rating = models.IntegerField()
    metacritic = models.IntegerField()
    rotten_tomatoes = models.IntegerField()
    type_field = models.CharField(db_column='type_', max_length=12)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'movies'

    def __str__(self):
        """String to represent Movie model object."""
        return self.title
