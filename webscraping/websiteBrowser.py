import json
import os

import requests
from bs4 import BeautifulSoup

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

    # nacteni linku v konkretnim html_content (na konkretni strance)
    def ziskajAdresyProduktov(self):
        odkazy = []

        soup = BeautifulSoup(self.html_content, 'html.parser')

        # najiti vsech odkazu
        link_classes = soup.find_all('a', class_='product-item-link')

        # nacteni hrefu
        for link in link_classes:
            href = link.get('href')
            if href:
                print(href)
                odkazy.append(href)

        return odkazy

        # ulozi prvnich 150 adres do souboru urls.txt
    def prvnich150Adres(self):
        odkazy = []
        stranka = 1 # cislo aktualni stranky

        while len(odkazy) < 150:
            url = f'{self.URL}?p={stranka}'
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:

                # ziskani odkazu z konkretni stranky
                self.html_content = response.text
                nove_odkazy = self.ziskajAdresyProduktov()
                odkazy.extend(nove_odkazy)

                # toto je optional, jen orizne pocet odkazu presne na 150
                if len(odkazy) >= 150:
                    odkazy = odkazy[:150]
                    break

                stranka += 1

            else:
                print(f"err:{response.status_code}")
                break

        # zapis do souboru
        with open('urls.txt', 'w') as f:
            for odkaz in odkazy:
                f.write(odkaz + '\n')

    def nacitajObsahAdresies(self):

        localObsahAdries = []
        #for adresa in self.adresy:
            #self.driver.get(adresa)
            #localObsahAdries.append(self.driver.page_source)


        return localObsahAdries
