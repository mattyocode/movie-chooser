from django.urls import path
from . import views

app_name = 'lists'
urlpatterns = [
    path('', views.my_list, name='my_list'),
    # path('results/', views.results, name='results'),
]