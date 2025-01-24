num1 = 100
num2 = 55

num1 = num1 - 20
print(num1)

num2 = num2 + 45
print(num2)

# 복합 대입 연산자
'''
복합 대입 연산자 종류
1. a+=b (a = a+b)
2. a-=b (a = a-b)
3. a*=b (a = a*b)
4. a/=b (a = a/b)
5. a//=b (a = a // b)
6. a%=b (a = a%b)
'''

number = 4
number += 1 # number = number + 1
print(number)
number = number + 1
print(number)

seven = 7
three = 3

ten = seven + three #10
seven+=three #10
print(seven)

ten-=seven #0
print(ten)

three *= seven #30
print(three)

three /= seven #3.0
print(three)

five = 5
two = 2
five //= two #2 (나누기 에서 정수만 나오게 하고 싶을 때)
print(five)

two **= five #4
print(two)

two += 1 #5
print(two)

two %= five #1
print(two)

