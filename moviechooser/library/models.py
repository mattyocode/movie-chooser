# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    imdbid = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=200)
    rated = models.CharField(max_length=20, blank=True, null=True)
    released = models.DateField()
    runtime = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    director = models.ManyToManyField(Director)
    writer = models.CharField(max_length=500)
    actors = models.ManyToManyField(Actor)
    plot = models.CharField(max_length=500, null=True)
    language = models.CharField(max_length=40, null=True)
    country = models.CharField(max_length=40, null=True)
    poster_url = models.CharField(max_length=200)
    imdb_rating = models.IntegerField(null=True)
    metacritic = models.IntegerField(null=True)
    rotten_tomatoes = models.IntegerField(null=True)
    avg_rating = models.IntegerField(null=True)
    type_field = models.CharField(db_column='type_', max_length=12, null=True)

    def __str__(self):
        return self.title
