from random import randint

from django.shortcuts import get_object_or_404, render

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by("-released")
    return render(request, 'library.html', {'movies': movies})

def surprise(request):
    movies = Movie.objects.all()
    rand_index = randint(0, len(movies) - 1)
    random_movie = movies[rand_index]
    context = {
        'movie': random_movie,
        'actors': random_movie.get_actors(),
        'director': random_movie.get_director(),
        'year': random_movie.get_year(),
        'genre': random_movie.get_genre(),
    }
    # year = random_movie.get_year()
    # genre = random_movie.get_genre()

    return render(request, 'surprise.html', context=context)