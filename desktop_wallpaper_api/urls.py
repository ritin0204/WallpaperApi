from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('api/wallpapers/random/', get_wallpaper, name='get_random_wallpaper'),
    path('api/wallpapers/<str:name>/', get_wallpaper, name='get_wallpaper'),
]

