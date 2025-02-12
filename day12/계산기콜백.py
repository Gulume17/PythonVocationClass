'''
숫자 2개와 연산자(함수)를 받는 함수 생성 -> 연산자(매개변수1,매개변수2)

1. 더하기 함수
2. 마이너스 함수
3. 곱하기 함수
4. 나누기 함수
'''

def calculator(x,y,operation):
    # x : 첫번째 숫자
    # y : 두번째 숫자

    return operation(x,y)


def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiple(x,y):
    return x * y

def divide (x,y):
    if y == 0:
        return " 0으로 나눌 수 없다!"
    return x / y

plus_result = calculator(1,2,plus)
minus_result = calculator(8,5,minus)
multiple_result = calculator(3,6,multiple)
divide_result = calculator(8,5,divide)

print(plus_result)
print(minus_result)
print(multiple_result)
print(divide_result)

















