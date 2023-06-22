from django.urls import path, include
from .views import *


urlpatterns = [
    # Define All Endpoints of the API
    ## GET /<int:pk> - Get a Wallpaper by ID
    ## Search by Name
    ## GET /?name=<str:name> - Get a Wallpaper by Name
    ## POST / - Create a Wallpaper
    
    path('', index, name='index'),
    path('api/wallpapers/<str:name>', get_wallpaper, name='get_wallpaper'),
]

