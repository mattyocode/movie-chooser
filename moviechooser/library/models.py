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
    runtime = models.IntegerField(null=True)
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

    def get_genre(self):
        genre_str = ', '.join([genre.name for genre in self.genre.all()])
        return genre_str

    def get_actors(self):
        actors_str = ', '.join([actors.name for actors in self.actors.all()])
        return actors_str

    def get_director(self):
        director_str = ', '.join([director.name for director in self.director.all()])
        return director_str

    def get_decade(self):
        decade = self.get_year()
        decade = decade[:3] + '0s'
        return decade

    def get_year(self):
        year = self.released.strftime("%Y")
        return year
        

class OnDemand(models.Model):
    imdbid = models.ForeignKey(
        Movie, on_delete=models.CASCADE
    )
    service = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    added = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.imdbid + "--" + self.service