from django.shortcuts import redirect, render
from django.http import HttpResponse

from moviechooser.lists.models import Item

# Create your views here.

def my_list(request):
    if request.method == 'POST':
        item_imdbid = request.POST['imdbid']
        Item.objects.create(imdbid=item_imdbid)
        return HttpResponse('<script>history.back();</script>')

    return render(request, 'my_list.html')