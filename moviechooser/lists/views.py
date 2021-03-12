from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_list(request):
    return HttpResponse('Movie list')