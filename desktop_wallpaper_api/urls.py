from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('api/wallpapers/<str:name>/', get_wallpaper, name='get_wallpaper'),
]

