class product:
    def __init__(self,name, price, originalPrice, brand,
                 reviews, processTime, sku, material, character):
        self.name = name
        self.price = price
        self.originalPrice = originalPrice
        self.brand = brand
        self.reviews = reviews
        self.processTime = processTime
        self.sku = sku
        self.material = material
        self.character = character
        # self.noItems = "" ---implementacia sa uvidi
    def getDiscount(self):
        discount = (100-(100*self.price/self.originalPrice))
        return discount if discount >0 else 0