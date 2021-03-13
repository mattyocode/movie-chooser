from django.shortcuts import redirect, render
from django.http import HttpResponse

from moviechooser.lists.models import Item

# Create your views here.

def my_list(request):
    if request.method == 'POST':
        Item.objects.create(imdbid=request.POST['imdbid'])
        return HttpResponse('<script>history.back();</script>')
    else:
        movie_items = Item.objects.all()
        if len(movie_items) > 0:
            context = {
                'movie_items': movie_items
            }
        else:
            context = {
                'movie_items': 'No movies added to list'
            }

    return render(request, 'my_list.html', context)