from django.shortcuts import redirect, render
from django.http import HttpResponse

from moviechooser.library.models import Movie
from moviechooser.lists.models import Item


# Create your views here.

def my_list(request):
    if request.method == 'POST':
        item_id = request.POST['imdbid']
        item = Item.objects.create(imdbid=item_id)
        item.movie = Movie.objects.get(imdbid=item_id)
        return HttpResponse('<script>history.back();</script>')
    else:
        list_items = Item.objects.all()
        
        context = {
            'list_items': list_items
        }

    return render(request, 'my_list.html', context)