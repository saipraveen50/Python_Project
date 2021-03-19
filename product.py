class Product:

    def __init__(self):
        self.name = 'Iphone'
        self.description = 'best'
        self.price = 100000

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)


p1 = Product()
p1.display()
