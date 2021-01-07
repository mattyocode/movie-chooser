from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('surprise/', views.surprise, name='surprise'),
]