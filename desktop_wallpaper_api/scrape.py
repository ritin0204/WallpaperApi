from bs4 import BeautifulSoup
import requests
import imghdr
from urllib.parse import urlparse


class ScrapeWallpaper:
    def __init__(self, keyword, url=None) -> None:
        self.keyword = keyword
        self.url = url
    
    
    def get_wallpapers(self, limit):
        html_page = requests.get(self.url)
        soup = BeautifulSoup(html_page.text, 'html.parser')
        img_tags =  soup.find_all('figure', class_='thumb', limit=limit)
        links = [] 
        for img in img_tags:
            img_id = img['data-wallpaper-id']
            link = f"https://w.wallhaven.cc/full/{img_id[:2]}/wallhaven-{img_id}"
            link = link + self.get_image_type(link)
            links.append(link)
        return {"name": self.keyword, "imageURL": links}
    
    
    def get_image_type(self, image_url):
        image_type = ['.jpg', '.png','.jpeg']
        for img_type in image_type:
            if requests.get(image_url + img_type).status_code == 200:
                return img_type