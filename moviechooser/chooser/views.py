from random import randint

from django.shortcuts import get_object_or_404, render
from django.db.models import Max, Min, Q
from django.core.paginator import Paginator

from moviechooser.library.models import Movie, Genre
from moviechooser.lists.models import Item


def homepage(request):
    genres = Genre.objects.all()
    max_runtime = list(Movie.objects.aggregate(Max('runtime')).values())[0]
    min_runtime = list(Movie.objects.aggregate(Min('runtime')).values())[0]
    decades = sorted(set([movie.get_decade() for movie in Movie.objects.all()]), reverse=True)

    context = {
        'genres': genres,
        'min_runtime': min_runtime,
        'max_runtime': max_runtime,
        'decades': decades,
    }
    return render(request, 'homepage.html', context)


def results(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    genre_selection = request.GET.getlist('genre_choice')
    runtime = request.GET.getlist('runtime')[0]
    decade_selection = request.GET.getlist('decade_choice')

    if genre_selection != []:
        movies = Movie.objects.filter(genre__name__in=genre_selection)
    else:
        movies = Movie.objects.all()

    movies = (movies
                .filter(
                    Q(runtime__lte=runtime),
                    Q(*[('released__startswith', decade[:3]) for decade in decade_selection],
                    _connector=Q.OR)
                )
                .distinct()
                .order_by('-avg_rating')
            )

    try:
        items = Item.objects.filter(user=request.user)
        item_imdbid = set()
        for item in items:
            item_imdbid.add(item.imdbid)

        for movie in movies:
            if movie.imdbid in item_imdbid:
                movie.added = True
                movie.item = Item.objects.get(imdbid=movie.imdbid)
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

    return render(request, 'results.html', context=context)