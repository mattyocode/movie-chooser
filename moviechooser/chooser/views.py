from random import randint

from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from moviechooser.library.models import Movie, Genre
# from .forms import MovieChoiceForm

def homepage(request):
    genres = Genre.objects.all()
    sorted_runtimes = [movie.runtime for movie in Movie.objects.order_by('runtime')]
    decades = sorted(set([movie.get_decade() for movie in Movie.objects.all()]))

    context = {
        'genres': genres,
        'min_runtime': sorted_runtimes[0],
        'max_runtime': sorted_runtimes[-1],
        'decades': decades,
    }
    return render(request, 'homepage.html', context)

def results(request):
    print('request', request.GET)
    genre_selection = request.GET.getlist('genre_choice')
    runtime = request.GET.getlist('runtime')[0]

    if genre_selection != []:
        movies = Movie.objects.filter(genre__name__in=genre_selection).distinct().order_by('-avg_rating')
    else:
        movies = Movie.objects.all()

    movies = movies.filter(
                Q(runtime__lt=runtime)
            )

    context = {
        'movies': movies
    }
    return render(request, 'results.html', context)