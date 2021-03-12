from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    watched = models.BooleanField(default=False)