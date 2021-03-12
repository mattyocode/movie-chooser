from django.db import models

# Create your models here.
class Item(models.Model):

    # user = 
    title = models.CharField(max_length=200)
    # date_added =
    # watched = 