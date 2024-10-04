# script to get urls of different products from the target website
from bs4 import BeautifulSoup
from webscraping.websiteBrowser import websiteBrowser

class urlObtainer:
    def __init__(self, URL):
        self.browser = websiteBrowser(URL)
        self.urls = []
        self.baseUrl = URL

    # nacteni linku v konkretnim html_content (na konkretni strance)
    def ziskajAdresyProduktov(self, htmlContent):
        odkazy = []

        soup = BeautifulSoup(htmlContent, 'html.parser')

        # najiti vsech odkazu
        link_classes = soup.find_all('a', class_='product-item-link')

        # nacteni hrefu
        for link in link_classes:
            href = link.get('href')
            if href:
                odkazy.append(href)

        return odkazy

    # ulozi prvnich urlCount adres do souboru urls.txt    
    def getUrls(self, urlCount):
        stranka = 1 # cislo aktualni stranky

        while len(self.urls) < urlCount:
            self.browser.updateUrl(f'{self.baseUrl}?p={stranka}')
            htmlContent = self.browser.getHtmlContent()
            newUrls = self.ziskajAdresyProduktov(htmlContent)

            for newUrl in newUrls:
                self.urls.append(newUrl)
                if len(self.urls) >= urlCount:
                    break
            stranka += 1
        self.output()
    

    # print the created urls
    def output(self):
        for url in self.urls:
            print(url)
    