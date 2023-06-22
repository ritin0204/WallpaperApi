from bs4 import BeautifulSoup
import requests


class ScrapeWallpaper:
    def __init__(self, keyword, url=None) -> None:
        self.keyword = keyword
        if url:
            self.url = url
        else:
            self.url = f'https://wallhaven.cc/search?q={self.keyword}&categories=111&purity=100&resolutions=1920x1080&sorting=relevance&order=desc'
    
    
    def get_wallpapers(self, limit=1):
        html_page = requests.get(self.url)
        soup = BeautifulSoup(html_page.text, 'html.parser')
        a_tags =  soup.find_all('a', class_='preview')
        links = [] 
        count = 0
        for i in a_tags:
            if i.get('href').startswith('https://wallhaven.cc/w/'):
                links.append(self.get_wallpaper_by_link(i.get('href')))
                count += 1
                if count == limit and limit < 5:
                    break
        return links
    
    
    def get_wallpaper_by_link(self, link):
        html_page = requests.get(link)
        soup = BeautifulSoup(html_page.text, 'html.parser')
        image = soup.find('img', id='wallpaper')
        return {"name": self.keyword ,"url": image.get('src')} if image else None
        
        
        