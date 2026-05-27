class Car:
    def __init__(self, make, moedl, color, price):
        self.make = make
        self.model = moedl
        self.color = color
        self.price = price

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def __str__(self):
        return f"차량 = {self.make}, {self.model}, {self.color}, {self.price}"
