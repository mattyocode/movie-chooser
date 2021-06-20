from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('movie/<str:pk>/', views.movie_detail, name='detail'),
    path('surprise/', views.surprise, name='surprise'),
    path('search/', views.search_results, name='search_results')
]