from webscraping.productObj import product
from bs4 import BeautifulSoup

class parser:
    # open the url file when instantiating parser
    def __init__(self):
        self.productList = []

    # break the html document into product objects
    def parse(self, htmlContent):

        soup = BeautifulSoup(htmlContent, 'html.parser')

        productInfo = soup.find_all(class_='product-info-main')

        
        # get product name
        productName = soup.find('h1', class_='product-name').text
        print(productName)

        productAttributes = soup.find_all(class_='product attibute description')
        #print(productInfo)

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