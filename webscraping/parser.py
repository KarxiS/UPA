class parser:
    def __init__(self, htmlContents):
        self.contents =  htmlContents
        self.products =[]
    def parse(self):
        #logika parsovania html kodu, vytvarania objektov, pridavania do arrayu self.objects
        #tu sa bude posielat viacero stranok, cize zachovanie si stavu
        pass

    def updater(self):
        #logika aktualizovania cien, brand, mena atd... to ze tu musi byt co som cital na dc
        pass

    def getProducts(self):
        return self.products