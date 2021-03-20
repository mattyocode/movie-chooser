from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from moviechooser.library.models import Movie
from moviechooser.lists.models import Item


def my_list(request):
    if request.method == 'POST':
        item_imdbid = request.POST['imdbid']
        movie = Movie.objects.get(imdbid=item_imdbid)
        item = Item.objects.create(imdbid=item_imdbid, movie=movie)
        request.session['from_list'] = True
        return redirect(request.META.get('HTTP_REFERER') + f"#{item_imdbid}")
    else:
        list_items = Item.objects.all()
        context = {
            'list_items': list_items
        }

    return render(request, 'my_list.html', context)

def remove_item(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))
    
def update_item(request, pk):
    item = Item.objects.get(id=pk)
    if item.watched:
        item.watched = False
    else:
        item.watched = True
    item.save()

    return redirect(reverse('lists:my_list'))