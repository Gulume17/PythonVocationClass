'''
시작 숫자는 : 0
숫자는 30 까지 증가할 것
5의 배수는 출력하지 않으며, 짝수도 출력하지 않는다.
27전 까지만 출력할 것이다.
break,continue 둘다 사용하기
'''

start_number = 0
while start_number < 30:
    start_number += 1
    if start_number % 5 == 0:
        continue
    if start_number % 2 == 0:
        continue
    elif start_number > 27:
        break
    print(start_number)




