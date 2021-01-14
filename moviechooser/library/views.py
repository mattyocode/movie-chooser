from random import randint

from django.shortcuts import get_object_or_404, render

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by("-released")
    return render(request, 'library.html', {'movies': movies})

def surprise(request):
    movies = Movie.objects.all()
    if len(movies) > 1:
        rand_index = randint(0, len(movies) - 1)
    else: 
        rand_index = 0
    random_movie = movies[rand_index]
    context = {
        'movie': random_movie,
        'actors': random_movie.get_actors(),
        'director': random_movie.get_director(),
        'year': random_movie.get_year(),
        'genre': random_movie.get_genre(),
    }

    return render(request, 'surprise.html', context=context)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, imdbid=pk)
    context = {
        'movie': movie,
        'actors': movie.get_actors(),
        'director': movie.get_director(),
        'year': movie.get_year(),
        'genre': movie.get_genre(),
    }
    return render(request, 'detail_page.html', context=context)


