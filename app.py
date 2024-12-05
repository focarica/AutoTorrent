from utils.htmlScraper import Scraper
from utils.htmlParser import Parser
from cli.ui import Interface

class App:
    def __init__(self):
        self._parser = Parser()
        self._interface = Interface()
        self._scraper = Scraper()
        
        self._mainHtml = self._scraper.getHtml()

    def core(self):
        self._interface.mainFlow(pageParsed=self._mainHtml)