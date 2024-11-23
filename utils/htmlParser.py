from bs4 import BeautifulSoup

class Parser:
    def parser(self, html, limit: int = 5) -> dict:
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