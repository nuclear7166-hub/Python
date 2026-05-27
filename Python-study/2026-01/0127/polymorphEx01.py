class Shape:
    def __init__(self, name):
        self.name = name

    def getArea(self):
        raise NotImplementedError("이것은 추상 메소드입니다.")


class Circle:
    def __init__(self, name, radius):
        super().__init__()
        self.radius = radius

    def getArea(self):
        return 3.141592 * self.radius**2


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def getArea(self):
        return self.height * self.width


c1 = Circle("원", 10)
r1 = Rectangle("사각형", 10, 20)
objList = [c1, r1]
for i in objList:
    print(f"면적 = {i.getArea()}")
