from requests_html import HTMLSession
from cli.commands import commands

BASE_URL = "https://1337x.to"

class Scraper: 
    def _makeUrl(self) -> str:
        query, category, sort_by = commands().name, commands().category, commands().sort_by
                
        if category and sort_by:
            return f"{BASE_URL}/sort-category-search/{query}/{category}/{sort_by}/desc/1/"
            
        if category:        
            return f"{BASE_URL}/category-search/{query}/{category}/1/"
        
        if sort_by:
            return f"{BASE_URL}/sort-search/{query}/{sort_by}/desc/1/"
            
        return f"{BASE_URL}/search/{query}/1/"

    
    def getHtml(self):
        session = HTMLSession()

        response = session.get(url=self._makeUrl())
        response.html.render()
        
        return response.html
