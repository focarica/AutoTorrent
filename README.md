# AutoTorrent

An intermediary between you and the top torrent aggregators. Easily search for and download any torrent directly from the command line.

## Installing

Clone the repository:

```bash
git clone https://github.com/focarica/AutoTorrent.git
cd AutoTorrent
```

If you are using a:

**Linux System**

```bash
# Installing lib to donwload torrents.

sudo apt-get install python3-libtorrent
``` 
    
```bash
# Creating and activating a venv for this project.

python3 -m venv venv --system-site-packages
source venv/bin/activate
```

**Or a Windows System**

```bash
# Creating and activating a venv for this project.

python -m venv venv
venv\Scripts\activate
```

And last, for both:

```bash
# Installing requirements

pip install -r requirements.txt
```

## How To use

Run `main.py` file passing args for search. Type `main.py search -h` to see all possible options

### Example

If you wanna make a normal search for avengers torrents, 

On linux Systems:

```bash
python3 main.py search avengers
```

On Windows:

```bash
python main.py search avengers
```

And will return top 5 torrents, to modify the quantity add `--limit {value}` when running.

An robust search using all filters would be like,

```bash
main.py search avengers --category games --sort-by time --limit 6
```

## Future Enhancements

- Extend scraping capabilities for additional torrent websites.
- Integrate FastAPI for API-based torrent search and download management.
- Add advanced filtering and sorting options.
