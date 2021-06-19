from random import randint, shuffle

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from moviechooser.lists.models import Item
from moviechooser.library.models import Movie


def index(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    
    movies = cache.get('movie_selection')
    if not movies:
        movies = Movie.objects.order_by('?')
        cache.set('movie_selection', movies)

    try:
        items = Item.objects.filter(user=request.user)
        item_imdbid = set()
        for item in items:
            item_imdbid.add(item.imdbid)

        for movie in movies:
            if movie.imdbid in item_imdbid:
                item = Item.objects.filter(user=request.user, imdbid=movie.imdbid)
                movie.item_id = str(item[0].id)
                movie.added = True
            else:
                movie.added = False
    except:
        pass

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

    try:
        item = Item.objects.filter(user=request.user, imdbid=random_movie.imdbid)
        random_movie.item_id = str(item[0].id)
        random_movie.added = True
    except:
        random_movie.added = False

    context = {
        'movie': random_movie,
        'actors': random_movie.get_actors(),
        'director': random_movie.get_director(),
        'year': random_movie.get_year(),
        'genre': random_movie.get_genre(),
        'try_again': True,
    }

    return render(request, 'surprise.html', context=context)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, imdbid=pk)

    try:
        item = Item.objects.filter(user=request.user, imdbid=movie.imdbid)
        movie.item_id = str(item[0].id)
        movie.added = True
    except:
        movie.added = False

    context = {
        'movie': movie,
        'actors': movie.get_actors(),
        'director': movie.get_director(),
        'year': movie.get_year(),
        'genre': movie.get_genre(),
    }
    return render(request, 'detail_page.html', context=context)

def search_results(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    query = request.GET.get('q')
    movies = Movie.objects.filter(
        Q(title__icontains=query)
        ).order_by('-avg_rating')

    try:
        items = Item.objects.filter(user=request.user)
        item_imdbid = set()
        for item in items:
            item_imdbid.add(item.imdbid)

        for movie in movies:
            if movie.imdbid in item_imdbid:
                movie.added = True
                item = Item.objects.filter(user=request.user, imdbid=movie.imdbid)
                movie.item_id = str(item[0].id)
            else:
                movie.added = False
    except:
        pass

    paginator = Paginator(movies, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'parameters': parameters,
        'page_obj': page_obj,
    }

    return render(request, 'search_results.html', context=context)
        

