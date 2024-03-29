from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from moviechooser.library.models import Movie
from moviechooser.lists.models import Item

@login_required(login_url='accounts:login')
def my_list(request):
    if request.method == 'POST':
        item_imdbid = request.POST['imdbid']
        # Check user's saved items
        if not Item.objects.filter(user=request.user, imdbid=item_imdbid).exists():
            movie = Movie.objects.get(imdbid=item_imdbid)
            item = Item.objects.create(user=request.user, imdbid=item_imdbid, movie=movie)
            if 'surprise' and '?' in request.META.get('HTTP_REFERER'):
                return redirect(request.META.get('HTTP_REFERER'))
            # if 'surprise' and not '?' in request.META.get('HTTP_REFERER'):
            #     return redirect(request.META.get('HTTP_REFERER') + f"?movie={item_imdbid}")
        return redirect(request.META.get('HTTP_REFERER') + f"#{item_imdbid}")
    else:
        list_items = Item.objects.filter(user=request.user)
        for item in list_items:
            movie = Movie.objects.get(imdbid=item.movie.imdbid)
        context = {
            'list_items': list_items
        }
    return render(request, 'my_list.html', context)

@login_required(login_url='accounts:login')
def remove_item(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    if request.META.get('HTTP_REFERER') == reverse('lists:my_list'):
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        if 'surprise' and '?' in request.META.get('HTTP_REFERER'):
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER') + f"#{item.imdbid}")

@login_required(login_url='accounts:login')
def update_item(request, pk):
    item = Item.objects.get(id=pk)
    if item.watched:
        item.watched = False
    else:
        item.watched = True
    item.save()

    return redirect(reverse('lists:my_list'))