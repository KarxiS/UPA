import json
import os

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class websiteBrowser:


    # poslem, tu spracujem cez BS
    def __init__(self, URL):
        self.adresy = []
        self.URL = URL
        s = Service(ChromeDriverManager().install())
        options = Options()
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.get(URL)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        print(self.driver.page_source)
        print(soup.contents)


    def ziskajAdresyPredmetov(self,html):
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
        for adresa in self.adresy:
            self.driver.get(adresa)
            localObsahAdries.append(self.driver.page_source)


        return localObsahAdries
