from django.shortcuts import render
from django.http import JsonResponse
from .scrape import ScrapeWallpaper
from .models import Wallpaper
from random import randint

# Create your views here.
def index(request):
    api_urls = [
        {
            "name": "Search by Name",
            "description": "GET /Name",
            "link": "/api/wallpapers/<name>"
        },
        {
            "name": "get a random wallpaper",
            "description": "GET /random",
            "link": "/api/wallpapers/random"
        }
    ]
    return render(request, 'desktop_wallpaper_api/index.html', {
        "apis": api_urls,
    })


def get_wallpaper(request, name):
    name = name.lower()
    
    # Get the limit, width and height from the request
    # If not provided, default values are used
    name = name.replace("-", "+")
    limit = int(request.GET.get('limit', '1/')[0])
    resolution_width = request.GET.get('width', 1920)
    resolution_height = request.GET.get('height', 1080)
    
    if not name:
        return JsonResponse({"error": "Invalid Name"}, safe=False)
    
    
    if name == "random":
        scrape = ScrapeWallpaper("random", url="https://wallhaven.cc/random")
        wallpapers = scrape.get_wallpapers(limit=limit)
        return JsonResponse(wallpapers, safe=False)
    
    scrape = ScrapeWallpaper(keyword=name, url=f"https://wallhaven.cc/search?q={name}&categories=111&purity=100&resolutions={resolution_width}x{resolution_height}&sorting=relevance&order=desc&ai_art_filter=0")
    
    # Get Wallpapers from the ScrapeWallpaper Class
    # Returns a list of dictionaries Limit = 1 by default
    wallpapers = scrape.get_wallpapers(limit=limit)
    
    if not wallpapers:
        return JsonResponse({"error": "No Wallpaper Found"}, safe=False)
    
    # Create Wallpaper Objects from the list of dictionaries
    response_data = []
    for wallpaper in wallpapers:
        if wallpaper:
            response_data.append(wallpaper)
            
    return JsonResponse(response_data, safe=False)
