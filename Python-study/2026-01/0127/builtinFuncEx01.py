class Person:
    def __init__(self, name, phone, addr, age):
        self.name = name
        self.phone = phone
        self.addr = addr
        self.age = age

    def __str__(self):
        return f"{self.name},{self.phone},{self.age}"


p1 = Person("홍길동", "123456-7890123", "우산국", 500)
p2 = Person("박길동", "189756-8790123", "정산국", 505)
p3 = Person("강길동", "157234-3890123", "강산국", 555)
personList = [p1, p2, p3]
for i in personList:
    print(i)


def keyName(person):
    return person.name


sorted_list = sorted(personList, key=lambda p: p.name)

for p in sorted_list:
    print(p)
