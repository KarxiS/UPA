# IMPORTY
import requests
from webscraping.websiteBrowser import websiteBrowser
from webscraping.parser import parser

# DEFINICIE
URL = "https://www.rolecosplay.com/anime-costume.html"

# MAIN

analyzator = websiteBrowser(URL)
# analyzator.prvnich150Adres()

extractor = parser()
# for each url in urls.txt extract the data into product objects
urlFile = open('urls.txt', 'r')
x = 0
for line in urlFile:
    x += 1
    analyzator.updateUrl(line.strip())
    extractor.parse(line.strip(), analyzator.getHtmlContent())
    print('object ' + str(x) + ' / 150')
    if x > 2:
        break
urlFile.close()

extractor.save()