from random import randint

from django.shortcuts import get_object_or_404, render

from moviechooser.library.models import Movie, Genre
from .forms import MovieChoiceForm

def homepage(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, 'homepage.html', context)

def selection(request):
    return render(request, 'detail_page.html')


    