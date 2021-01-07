from random import randint

from django.shortcuts import render

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by("-released")
    return render(request, 'index.html', {'movies': movies})

def surprise(request):
    movies = Movie.objects.all()
    rand_index = randint(0, len(movies) - 1)
    random_movie = movies[rand_index]
    return render(request, 'surprise.html', {'movie': random_movie})