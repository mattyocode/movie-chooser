from random import randint

from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.core.paginator import Paginator

from moviechooser.library.models import Movie, Genre
# from .forms import MovieChoiceForm

def homepage(request):
    genres = Genre.objects.all()
    sorted_runtimes = [movie.runtime for movie in Movie.objects.order_by('runtime')]
    decades = sorted(set([movie.get_decade() for movie in Movie.objects.all()]), reverse=True)

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
    decade_selection = request.GET.getlist('decade_choice')

    if genre_selection != []:
        movies = Movie.objects.filter(genre__name__in=genre_selection)
    else:
        movies = Movie.objects.all()

    movies = movies.filter(
                # Q(genre__name__in=genre_selection),
                Q(runtime__lte=runtime),
                Q(*[('released__startswith', decade[:3]) for decade in decade_selection],
                _connector=Q.OR)
            )

    movies = movies.distinct().order_by('-avg_rating')

    paginator = Paginator(movies, 22)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj': page_obj,
    }

    return render(request, 'results.html', context)