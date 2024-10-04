class product:
    def __init__(self, url, name, price, brand, source, character, included, material, reviews):
        self.url = url
        self.name = name
        self.price = price
        self.source = source
        self.brand = brand
        self.character = character
        self.included = included
        self.material = material
        self.reviews = reviews
    def getUrl(self):
        return self.url
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getBrand(self):
        return self.brand
    def getSource(self):
        return self.source
    def getCharacter(self):
        return self.character
    def getIncluded(self):
        return self.included
    def getMaterial(self):
        return self.material
    def getReviews(self):
        return self.reviews
    