class ElectriCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterSize = batterySize

    def setBatterSize(self, batterySize):
        self.batterSize = batterySize

    def getBatterSize(self):
        return self.batterSize


myCar = ElectriCar("Hyundai", "Model H", "White", "5000", 0)
myCar.setBatterSize(240)
print(myCar)
print(myCar.getBatterSize())
