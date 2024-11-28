import tempfile
import json

class Cache:
    def __init__(self):
        self.tempFile = tempfile.NamedTemporaryFile(mode="w+", delete=True)
        self.cache = {}
        self._loadCache()
        
    def _loadCache(self):
        try:
            self.tempFile.seek(0)
            data = self.tempFile.read()
            
            if data:
                self.cache = json.loads(data)
        except json.JSONDecodeError:
            self.cache = {}
    
    def _saveToCache(self):
        self.tempFile.seek(0)
        self.tempFile.truncate(0)
        json.dump(self.cache, self.tempFile)
        self.tempFile.flush()
        
    def get(self, key):
        torrentPage = self.cache.get(key)
        
        return torrentPage if torrentPage is not None else []
    
    def add(self, key, value):
        self.cache[key] = value
        self._saveToCache()