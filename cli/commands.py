import argparse

def __typeForCategory(string: str) -> str:
    if string.upper() == "XXX":
        return string.upper()
    elif string.upper() == "TV":
        return string.upper()
    
    return string.capitalize()


def commands():
    parser = argparse.ArgumentParser(
        prog='AutoTorrent'
    )
    
    subparsers = parser.add_subparsers(dest='command')
    
    searchParser = subparsers.add_parser('search', help='Search for a torrent and retrieves some of them.')
    searchParser.add_argument("name", 
                              type=str, 
                              help="Name to search for.")
    
    searchParser.add_argument("--category",
                              type=__typeForCategory,
                              choices=["Movies", "TV", "Games", "Music", "Aplications", "Documentaries", "Anime", "Others", "XXX"],
                              help="Specify the category to search in.")
    
    searchParser.add_argument("--sort-by",
                              type=lambda string: string.lower(),
                              choices=["time", "size", "seeders"],
                              help="Sort results by a specific field")
    
    searchParser.add_argument("--limit",
                              type=int,
                              default=5,
                              help="Limit the number of results")
    
    return parser.parse_args()