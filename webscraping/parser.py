from webscraping.productObj import product
from bs4 import BeautifulSoup
import re

class parser:
    # open the url file when instantiating parser
    def __init__(self):
        self.productList = []

    # break the html document into product objects
    def parse(self, url, htmlContent):

        soup = BeautifulSoup(htmlContent, 'html.parser')
        
        # find data
        productInfo = soup.find_all(class_='product-info-main')
        
        # product URL 1/8
        # url ...

        # get product name 2/8
        productName = soup.find('h1', class_='product-name').text
        print(productName)

        # current price 3/8
        price = soup.find(class_='price').text
        print(price)
        
        # find data
        productAttributes = soup.find(class_='product attibute description')

        # extra attributes 8/8
        targetAttributes = ['Brand', 'Anime', 'Source', 'Character', 'Included Items', 'Material']
        # alignment is really messy here in the description we will need to extract attributes in an obscure way
        rawText = productAttributes.getText(separator=' ', strip=True)

        # find colon
        colonIndex = rawText.find(":")
        specialColonIndex = rawText.find("：")
        if colonIndex != -1:
            validIndex = colonIndex
        if specialColonIndex != -1:
            validIndex = specialColonIndex
        if specialColonIndex != -1 and colonIndex  != -1:
            validIndex = min(colonIndex, specialColonIndex)

        # parse attribute name
        leftStr = rawText[:validIndex].strip()
        print(f"string '{leftStr}'")
        
        # parse attribute value

        # reviews


        # fill product with parsed values
        #product()

        # add product object to the list 
        #self.productList.append()

        pass # regular expressions

    # save the created objects
    def save(self):
        #logika aktualizovania cien, brand, mena atd... to ze tu musi byt co som cital na dc
        pass

    def getProducts(self):
        return self.productList