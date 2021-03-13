from django.shortcuts import redirect, render
from django.http import HttpResponse

from moviechooser.library.models import Movie
from moviechooser.lists.models import Item


# Create your views here.

def my_list(request):
    if request.method == 'POST':
        item = Item.objects.create(imdbid=request.POST['imdbid'])
        print(item)
        item.movie = Movie.objects.get(imdbid=item)
        
        return HttpResponse('<script>history.back();</script>')
    else:
        movie_items = Item.objects.all()
        context = {
            'movie_items': movie_items
        }

    return render(request, 'my_list.html', context)