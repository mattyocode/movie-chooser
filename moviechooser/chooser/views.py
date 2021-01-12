from random import randint

from django.shortcuts import get_object_or_404, render

from moviechooser.library.models import Movie, Genre

def homepage(request):
    context = {
        'genres': Genre.objects.all()
    }
    return render(request, 'homepage.html', context)