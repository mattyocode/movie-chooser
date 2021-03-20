from django.urls import path
from . import views

app_name = 'lists'
urlpatterns = [
    path('', views.my_list, name='my_list'),
    path('remove/<int:pk>/', views.remove_item, name='remove'),
    path('update/<int:pk>/', views.update_item, name='update'),
]