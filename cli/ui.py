import sys
from os import system
from cli.commands import commands


class Interface:
    def __init__(self) -> None:
        self.query = commands().name
        self.category = commands().category
        self.sort_by = commands().sort_by
        
        
    def _typeSearch(self) -> str:
        baseString = f"Searching for '{self.query}'"
        finalString = "Type 'q' to exit application."
        
        if self.category and self.sort_by:
            return f"{baseString} in {self.category} category ordered by {self.sort_by}. {finalString}"
        
        if self.category:
            return f"{baseString} in {self.category} category. {finalString}"
        
        if self.sort_by:
            return f"{baseString} ordered by {self.sort_by}. {finalString}"
        
        return baseString + {finalString}
    
    
    def _printLongNames(self, name: str) -> str:
        if len(name) > 64:
            return f"{name[:64]}..."
        return name
    
    
    def mainMenu(self, response: dict) -> int:
        system("clear")
            
        print(self._typeSearch() + "\n")
            
        for i, result in response.items():
            name = result["name"]
            size = result["size"]
            seeders = result["seeds"]
            uploader = result["from"]
            date = result["date"]
            
            print(f"[{i}] {self._printLongNames(name)} - {size} - {seeders} online - upload by {uploader} in {date}\n")

        print("Select the specific torrent to view details.\n")
        
        while True:
            choice = input("> ")
            
            if choice.lower() == 'q':
                sys.exit()
            
            try:   
                choice = int(choice)
                
                if not (0 <= choice < len(response)):
                    first_key = list(response.keys())[0]
                    last_key = list(response.keys())[-1]
                    print(f"Please put a valid value between {first_key} and {last_key}.") 
                else:
                    return response[choice]['link']
            except ValueError:
                print("Enter a valid number or type 'q' to quit.")