from utils.htmlScraper import Scraper
from utils.htmlParser import Parser
from cli.ui import commands
from cli.ui import Interface

class App:
    def __init__(self):
        self._parser = Parser()
        self._interface = Interface()
        self._scraper = Scraper()
        
        mainHtml = self._scraper.getHtml()
        self._htmlParsed = self._parser.searchParser(html=mainHtml, limit=commands().limit)

        
    def core(self):
        self._interface.mainFlow(pageParsed=self._htmlParsed)