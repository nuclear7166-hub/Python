class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.base


rect1 = Rectangle(30, 30)
rect1.base = 10
rect1, setBase(10)
print(rect1.base)
print(rect1.getBase())
rect2 = Rectangle(50, 30)


class Student:
    def __init__(self, name, addr, phone, age):
        self.name = name
        self.addr = addr
        self.phone = phone
        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


st1 = Student("홍길동", "우산국", "010-1212-2121", 500)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius**2

    def getPrimeter(self):
        return 2 * 3.14 * self.radius


c1 = Circle(6)
print(
    f"반지름이 {c1.radius}인 원의 면적은 {c1.getArea()}이고 둘레는 {c1.getPrimeter()}입니다."
)
c2 = Circle(12)
print(
    f"반지름이 {c2.radius}인 원의 면적은 {c2.getArea()}이고 둘레는 {c2.getPrimeter()}입니다."
)
