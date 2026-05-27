class Person:
    def __init__(self, name, socNumber):
        self.name = name
        self.socNumber = socNumber


class Student(Person):
    UNDERGRADUATE = 0
    POSTGRADUATE = 1

    def __init__(self, name, socNumber, studentType):
        super().__init__(name, socNumber)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []

    def enrollCourse(self, course):
        self.classes.append(course)

    def __str__(self):
        return f"\n 이름={self.name}\n주민번호={self.socNumber}\n수강과목={str(self.classes)}\n평점={str(self.gpa)}"


class Teacher(Person):
    def __init__(self, name, socNumber):
        super().__init__(name, socNumber)
        self.courses = []
        self.salary = 3000000

    def assignTeaching(self, course):
        self.courses.append(course)

    def __str__(self):
        return "\n이름=+self.name+ \n주민번호=+self.number+\
\n강의과목=+str(self.courses)+ \n월급=+str(self.salary)"


s1 = Student("홍길동", "123456-7890123", Student.UNDERGRADUATE)
s1.enrollCourse("파이썬 프로그래밍")
s1.enrollCourse("자료구조")
print(s1)

t1 = Teacher("김길동", "098765-4321098")
t1 = assignTeaching("파이썬 프로그래밍")
t1 = assignTeaching("자료 구조")
print(t1)
