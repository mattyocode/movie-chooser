from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_list(request):
    return render(request, 'my_list.html', {
        'new_movie_item': request.POST.get('title', ''),
    })