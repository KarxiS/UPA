# Name          : get.py
# Project       : UPA 1. část: extrakce dat z webu
# Description   : Script to get urls of different products from the target website
# Authors       : xbilko03, xpauli08, xsugark00
from bs4 import BeautifulSoup
from webscraping.websiteBrowser import websiteBrowser

class urlObtainer:
    def __init__(self, url):
        self.browser = websiteBrowser(url)
        self.urls = []
        self.baseUrl = url

    # load a link in specific html_content (from a specific website)
    def getProductAdresses(self, htmlContent):
        odkazy = []

        soup = BeautifulSoup(htmlContent, 'html.parser')

        # find all links to products
        link_classes = soup.find_all('a', class_='product-item-link')

        # load href
        for link in link_classes:
            href = link.get('href')
            if href:
                odkazy.append(href)

        return odkazy

    # prints the first urlCount adresses to stdout    
    def getUrls(self, urlCount=0):
        currentSiteIndex = 1

        while len(self.urls) < urlCount:
            self.browser.updateUrl(f'{self.baseUrl}?p={currentSiteIndex}')
            htmlContent = self.browser.getHtmlContent()
            newUrls = self.getProductAdresses(htmlContent)

            for newUrl in newUrls:
                self.urls.append(newUrl)
                if len(self.urls) >= urlCount:
                    break
            currentSiteIndex += 1
        self.output()
    

    # print the created urls
    def output(self):
        for url in self.urls:
            print(url)
    