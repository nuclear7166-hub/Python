try:
    numerator = int(input("분자 입력 : "))
    denominator = int(input("분모 입력 : "))

    quotient = numerator // denominator
    remainder = numerator % denominator

    print(f"{numerator}/{denominator} = {numerator/denominator}")
    print(f"몫 = {quotient}, 나머지 = {remainder}")
except ValueError:
    print("분모에 0이 입력되어서 계산을 할 수 없는 불능 상태입니다.")
except ZeroDivisionError:
    print("정수를 입력하세요.")


# 몫과 나머지 자리에 무엇이든 적기 가능
# 최초 접근법 print(f"quotient = {quotient}, remainder = {remainder}")
# try: 와 except 사용이 나옴 "체크"
