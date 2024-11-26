from bs4 import BeautifulSoup

class Parser:
    def searchParser(self, html, limit: int = 5) -> dict:
        soup = BeautifulSoup(html.html, 'html.parser')
        
        results: dict = {}
        
        try:
            tableResult = soup.find("table", 
                                    attrs={
                                        "class": "table-list table table-responsive table-striped"}
                                    ).findChild("tbody")
        except AttributeError:
            return {"error": "Return None"}
        
        for i, result in enumerate(tableResult.findAll("tr", limit=limit)):
            infos = result.findAll("td")

            results[i] = {
                "name": infos[0].text,
                "link": infos[0].findAll("a")[1].get("href"),
                "seeds": infos[1].text,
                "date": infos[3].text,
                "size": infos[4].contents[0].text,
                "from": infos[5].text 
            }
            
        return results
    
    
    def _findInfosTable(self, html) -> tuple:
        soup = BeautifulSoup(html.html, 'html.parser')
        
        try:
            name = soup.find("div", attrs={"class": "box-info-heading clearfix"}).find("h1").text
            
            # Since class for infos is dynamic created go to a fix class and search by childrens
            tableInfos = soup.find("div",
                                    attrs={
                                        "class": "box-info torrent-detail-page"
                                    }).findChildren("div")[1].findChild("div")
                        
            infosResult = tableInfos.find_all("ul")
            
            links = infosResult[0]
            mainInfos = infosResult[2:]
            
        except AttributeError:
            return {"error": "Return None"}
        
        return links, mainInfos, name
    
    
    def infosParser(self, html) -> dict:        
        allInfos = self._findInfosTable(html=html)
        
        links = allInfos[0]
        mainInfos = allInfos[1]
        name = allInfos[2]
        
        results: dict = {}
        magnetLink: str = links.find("li").find("a").get("href")
        
        results["magnetLink"] = magnetLink
        results["name"] = name

        for info in mainInfos:
            keys = info.findAll("strong")
            values = info.findAll("span")
            
            for i in range(len(keys)):
                results[keys[i].text] = values[i].text
    
        return results
        