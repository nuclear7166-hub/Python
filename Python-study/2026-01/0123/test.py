x = 1
y = 2
print(f"x={x}, y]{y}")
x, y = y, x
print(f"x={x}, y={y}")


def add(*numbers):
    sum = 0

    for n in numbers:
        sum = sum + n
    return sum


print(f"sum = {add(10)}, {add(10, 20)}, {add(10, 20, 30)}")


def display(massage, count):
    for i in range(count):
        print(massage)


display("환영합니다.", 5)


def addsub(x, y):
    return x + y, x - y


print(addsub(1, 2))
print(addsub(4, 3))
print(addsub(6, 4))


def nameAge():
    name = input("이름 : ")
    age = int(input("나이 : "))
    return name, age


a, b = nameAge()
print(f"이름은 {a}이고, 나이는 {b}살 입니다.")


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = eval(input("정수를 입력하시오:"))
print(n, "!= ", factorial(n))
