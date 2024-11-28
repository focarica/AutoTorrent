from requests_html import HTMLSession
from utils.htmlParser import Parser
from utils.cacheManager import Cache
from cli.commands import commands

class Scraper: 
    def __init__(self):
        self._parser = Parser()
        self._cache = Cache()
        self.BASE_URL = "https://1337x.to"
    
    def _makeSearchUrl(self) -> str:
        query, category, sort_by = commands().name, commands().category, commands().sort_by
                
        if category and sort_by:
            return f"{self.BASE_URL}/sort-category-search/{query}/{category}/{sort_by}/desc/1/"
            
        if category:        
            return f"{self.BASE_URL}/category-search/{query}/{category}/1/"
        
        if sort_by:
            return f"{self.BASE_URL}/sort-search/{query}/{sort_by}/desc/1/"
            
        return f"{self.BASE_URL}/search/{query}/1/"

    
    def getHtml(self):
        session = HTMLSession()

        response = session.get(url=self._makeSearchUrl())
        response.html.render()
        
        mainResponseParsed = self._parser.searchParser(
                                                    html=response.html, 
                                                    limit=commands().limit
                                                    )
        
        return mainResponseParsed

    def getSpecificTorrentPage(self, link: str):              
        cachedData = self._cache.get(link)
        
        if cachedData:
            return cachedData
        
        session = HTMLSession()
        url = f"{self.BASE_URL}{link}"
        
        response = session.get(url=url)
        response.html.render()
        
        specificPageParsed = self._parser.infosParser(html=response.html)        
        self._cache.add(link, specificPageParsed)
        
        return specificPageParsed