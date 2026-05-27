def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 테스트
num = int(input("몇 번째 피보나치 수를 구할까요? "))
print(f"{num}번째 피보나치 수는 {fibonacci(num)}입니다.")


# 피보나치 수 계산 재귀
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 피보나치 수열 합 계산 재귀
def fibonacci_sum(n):
    if n == 0:
        return 0
    else:
        return fibonacci(n) + fibonacci_sum(n - 1)


# 테스트
num = int(input("몇 번째 피보나치 수까지 합을 구할까요? "))
print(f"0부터 {num}번째 피보나치 수까지 합은 {fibonacci_sum(num)}입니다.")


gx = 100


def myfunc():
    global gx  # 전역변수 gx를 사용한다.
    # 위 라인이 없는 경우와 있는 경우를 설명
    gx = 200
    print(gx)


myfunc()
print(gx)
