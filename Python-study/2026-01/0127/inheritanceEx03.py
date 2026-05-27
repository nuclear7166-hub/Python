class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def displayCarInfo(self):
        return f"차량 = {self.make}, {self.model}, {self.color}, {self.price}"


class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterySize = batterySize

    def setBatterySize(self, batterySize):
        self.batterySize = batterySize

    def getBatterySize(self):
        return self.batterySize

    def displayElectricCarInfo(self):
        info = super().displayCarInfo()
        info += f", 배터리 = {self.batterySize}"
        return info


car1 = Car("Hyundai", "Model H", "White", "5000")
eCar1 = ElectricCar("Tesla", "Model X", "White", "10000", 240)

print(car1.displayCarInfo())
print(eCar1.displayElectricCarInfo())
