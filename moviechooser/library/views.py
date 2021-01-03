from django.shortcuts import render

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by("-released")
    return render(request, 'index.html', {'movies': movies})