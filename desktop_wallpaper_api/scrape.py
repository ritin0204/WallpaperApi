from bs4 import BeautifulSoup
import requests


class ScrapeWallpaper:
    def __init__(self, keyword, url=None) -> None:
        self.keyword = keyword
        self.url = url
    
    
    def get_wallpapers(self, limit):
        html_page = requests.get(self.url)
        soup = BeautifulSoup(html_page.text, 'html.parser')
        a_tags =  soup.find_all('a', class_='preview')
        links = [] 
        count = 0
        for i in a_tags:
            if i.get('href').startswith('https://wallhaven.cc/w/'):
                links.append(self.get_wallpaper_by_link(i.get('href')))
                count += 1
            if len(links) == limit or count == 10:
                return links
        return links
    
    
    def get_wallpaper_by_link(self, link):
        html_page = requests.get(link)
        soup = BeautifulSoup(html_page.text, 'html.parser')
        image = soup.find('img', id='wallpaper')
        return {"name": self.keyword ,"url": image.get('src')} if image else None
        
        
        