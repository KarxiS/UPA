from webscraping.productObj import product
from bs4 import BeautifulSoup

class parser:
    # open the url file when instantiating parser
    def __init__(self):
        self.productList = []

    # break the html document into product objects
    def parse(self, url, htmlContent):
        # product URL 1/8 from input argument

        # get input document
        soup = BeautifulSoup(htmlContent, 'html.parser')
        
        # find data
        productInfo = soup.find_all(class_='product-info-main')
        
        # product name 2/8
        productName = soup.find('h1', class_='product-name').text

        # current price 3/8
        price = soup.find(class_='price').text

        # brand 4/8 - categorical
        brand = '-'
        # source/anime 5/8 - categorical
        source = '-'
        # character 6/8 - categorical
        character = '-'
        # Included Items/Includes/Package 7/8
        included = '-'
        # material 8/8 - categorical
        material = '-'
        
        # find data
        attributes = soup.find(class_='product attibute description')
        # due to inconsistent formatting replace 'br' elements
        for element in attributes.find_all("br"):
            element.replace_with(" ||| ")
        attributesRaw = attributes.find_all('p')

        # replace each element in html with spaces for more consistent parsing

        # array of separated attributes (text only)
        attributesText = [element.get_text(separator=" ", strip=True) for element in attributesRaw]
        
        attributesFiltered = []
        for attribute in attributesText:
            forcedSeparatorIndex = attribute.find("|||")
            if forcedSeparatorIndex == -1:
                attributesFiltered.append(attribute)
            else:
                # if there is the forced separator, split the string
                splitAttributes = attribute.split('|||')
                for element in splitAttributes:
                    attributesFiltered.append(element)            
            
        # for each attribute, split it by colon and construct a pair 'name : value'
        for attribute in attributesFiltered:

            colonPresent = attribute.find(":")
            scolonPresent = attribute.find("：")

            separatorIndex = 0
            if scolonPresent != -1:
                separatorIndex = scolonPresent
            elif colonPresent != -1:
                separatorIndex = colonPresent
            
            if separatorIndex != 0:
                name = attribute[:separatorIndex].strip()
                value = attribute[separatorIndex + 1:].strip()
                # brand 4/8 - categorical
                if name == 'Brand':
                    brand = value
                # source/anime 5/8 - categorical
                elif name == 'Anime' or name == 'Source':
                    source = value
                # character 6/8 - categorical
                elif name == 'Character':
                    character = value
                # included Items/includes/package 7/8
                elif name == 'Included Items' or name == 'Includes' or name == 'Package':
                    included = value
                # material 8/8 - categorical
                elif name == 'Material':
                    material = value

        # reviews 9/8 - numeric
        reviews = soup.find(itemprop='reviewCount')
        if reviews:
            reviewCount = reviews.get_text(strip=True)
        else:
            reviewCount = '0'

        # fill product with parsed values
        newProduct = product(url, productName, price, brand, source, character, included, material, reviewCount)

        # add product object to the list 
        self.productList.append(newProduct)

    # save the created objects
    def save(self):
        outputFile = "data.tsv"
        with open(outputFile, 'w', encoding='utf-8') as file:
            for product in self.productList:
                file.write(product.getUrl())
                file.write('\t')
                file.write(product.getName())
                file.write('\t')
                file.write(product.getPrice())
                file.write('\t')
                file.write(product.getBrand())
                file.write('\t')
                file.write(product.getSource())
                file.write('\t')
                file.write(product.getCharacter())
                file.write('\t')
                file.write(product.getIncluded())
                file.write('\t')
                file.write(product.getMaterial())
                file.write('\t')
                file.write(product.getReviews())
                file.write('\n')
        

    def getProducts(self):
        return self.productList