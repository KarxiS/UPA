import json
import os

import requests
from bs4 import BeautifulSoup

class websiteBrowser:


    # poslem, tu spracujem cez BS
    def __init__(self, URL):
        self.adresy = []
        self.URL = URL

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

        response = requests.get(URL, headers=self.headers)


        if response.status_code == 200:
            self.html_content = response.text
            soup = BeautifulSoup(self.html_content, 'html.parser')

            print(self.html_content)
            print(soup.contents)
        else:
            print(f"err:{response.status_code}")
            self.html_content = ''


    def ziskajAdresyProduktov(self, html):
        URL = self.URL
        self.adresy = []
        #------------- DOLE zo stareho projektu TODO
        #
        # #self.driver.get(URL+"/plany.php?f=5&t=Z&m=2&r=1&z=MN&c=4")
        #
        # # beautifulsoup
        # soup = BeautifulSoup(html, 'html.parser')
        #
        # # hladam table element s id id-tabulka..
        # table = soup.find('table', attrs={'id': 'id-tabulka-studijnych-planov'})
        #
        # # pozeram sa po tr elementoch
        # rows = table.find_all('tr')
        # # prehladavam hlavnu stranku so stidujnimy a robim objekty , ktore sa samy spracujku
        # # Iterate over the rows
        # for row in rows:
        #     # hladam podla class
        #
        #     if (row.has_attr('class')) and ((row['class'][0] == 'odd') or (row['class'][0] == 'evn')):
        #         cells = row.find_all('td')
        #
        #         # zoberiem link, ktory je v href tagu
        #         course = cells[0].text
        #         link = cells[0].find('a')['href']
        #         self.adresy.append(URL + "/" + link)
        #
        #

        return self.adresy

    def nacitajObsahAdresies(self):

        localObsahAdries = []
        #for adresa in self.adresy:
            #self.driver.get(adresa)
            #localObsahAdries.append(self.driver.page_source)


        return localObsahAdries
