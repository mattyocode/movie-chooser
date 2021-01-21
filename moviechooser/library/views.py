from random import randint, shuffle

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('?')

    paginator = Paginator(movies, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'library.html', context=context)

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
    print(movie.imdb_rating)
    context = {
        'movie': movie,
        'actors': movie.get_actors(),
        'director': movie.get_director(),
        'year': movie.get_year(),
        'genre': movie.get_genre(),
    }
    return render(request, 'detail_page.html', context=context)

def search_results(request):
    query = request.GET.get('q')
    object_list = Movie.objects.filter(
        Q(title__icontains=query)
        )
    return render(request, 'search_results.html', {'movies': object_list})
        

