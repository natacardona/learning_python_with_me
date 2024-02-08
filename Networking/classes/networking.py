import requests

class Networking:
    def __init__(self,url):
        self.url = url

    def get(self):
        return requests.get(self.url)
    
    def caracters(self):
        return requests.get(self.url+'character')
    
    def locations(self):
        return requests.get(self.url+'location')
    
    def episodes(self):
        return requests.get(self.url+'episode')      
        