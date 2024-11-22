from requests_html import HTMLSession

BASE_URL = "https://1337x.to"

class Scraper: 
    def getHtml(self, url: str):
        session = HTMLSession()
        
        response = session.get(url=url)
        response.html.render()
        
        return response.html
