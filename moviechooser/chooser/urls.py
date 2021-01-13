from django.urls import path
from . import views

app_name = 'chooser'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('selection/', views.selection, name='selection'),
]