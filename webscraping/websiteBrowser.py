import requests

class websiteBrowser:

    # poslem, tu spracujem cez BS
    def __init__(self, URL):
        self.URL = URL
        self.html_content = ''

        #headre, lebo 403 forbidden
        self.headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/58.0.3029.110 Safari/537.3'
            ),
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': (
                'text/html,application/xhtml+xml,application/xml;'
                'q=0.9,image/webp,image/apng,*/*;q=0.8'
            ),
            'Connection': 'keep-alive',
        }

    def updateUrl(self, newUrl):
        self.URL = newUrl

    def getHtmlContent(self):
        url = f'{self.URL}'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            self.html_content = response.text
        else:
            self.html_content = ''

        return self.html_content
        
