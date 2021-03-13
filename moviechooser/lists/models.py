from django.db import models
from django.contrib.auth.models import User

from moviechooser.library.models import Movie

# Create your models here.
class Item(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    imdbid = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    watched = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title

    class Meta:
        ordering = ['date_added']