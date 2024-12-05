import libtorrent as lt
import time

class Donwload:
    def __init__(self):
        self.session = lt.session()
        self.session.listen_on(9990, 9999)
        self.params = {
            'save_path': './MyDownloads',
            'storage_mode': lt.storage_mode_t.storage_mode_sparse
        }
        
    def download(self, link):
        handler = lt.add_magnet_uri(self.session, link, self.params)
        
        while not handler.is_seed():
            s = handler.status()
            print(f'Download rate: {s.download_rate / 1000:.2f} kB/s, '
                f'Upload rate: {s.upload_rate / 1000:.2f} kB/s, '
                f'Progress: {s.progress * 100:.2f}%')
            time.sleep(1)

        print("Download complete!")