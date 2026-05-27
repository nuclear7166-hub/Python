import math


# Circle 클래스를 정의한다.
class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def prtCitcleInfo(self):
        print(
            f"반지름이 {self.radius}인 원의 면적은 {self.getArea()}이고 둘레는 {self.getPerimeter()}입니다."
        )
        # Circle 객체를 생성한다.


c = Circle(10)
print("원의 면적", c.getArea())
print("원의 면적", c.getPerimeter())
