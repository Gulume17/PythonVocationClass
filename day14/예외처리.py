'''
1. 에러 : 프로그램 오류 또는 시스템 문제가 발생하는 예외 (개발자가 직접 해결해야함)
2. 예외 : 사용자의 입력에 따라 발생하는 예외
'''

# print(7/0) # 에러 (1로 바꾸면 에러 안남)

# num1 = int(input("첫 번째 정수를 입력 : "))
# num2 = int(input("두 번째 정수를 입력 : "))
#
# if(num2 == 0):
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f"num1 나누기 num2의 결과는 : {num1/num2}입니다.")

# print(f"num1 나누기 num2의 결과는 : {num1/num2}입니다.") # 두번째 정수에 0 을 쓰면 에러가 남 -> 예외 (if문으로 해결 했지만 문자를 쓰면 다시 에러가 남)


'''
예외 처리
1. BaseExceprion : 최상위 예외클래스
2. Exception : 대부분 예외클래스의 슈퍼클래스
3. ArithmeticError : 산술연산 오류
    - OverflowError : 산술 연산의 결과가 너무 커서 표현할 수 없을 때
    - ZeroDivisionError ; 0으로 나누려고 할 때
    - FloatingPointError : 실수 연산에서 오류가 발생할 때
4. AttributeError : 잘못된 속성 참조
5. EOFError : 파일에서 더이상 읽을 데이터가 없을 때
6. ModuleNotfoundError : import할 모듈이 없을 때
7. FileNotFoundError : 존재하지 않는 파일
8. IndexError : 잘못된 인덱스 사용
9. NameError : 변수를 선언하지 않고 사용하려 할 때
10. SyntaxError : 코드 작성 규칙을 지키지 않았을 때
11. ValueError : 계산하려는 데이터 값의 오류
12. TypeError : 서로 다른 타입끼리 계산하려 할 때
# mdn 참고 (구글링)
'''


'''
try-except
try: 
    예외가 발생할 수 있는 코드
except:
    예외가 발생했을 때 수행하는 코드
'''

# try:
#     num1 = int(input("첫 번째 정수를 입력 : "))
#     num2 = int(input("두 번째 정수를 입력 : "))
#     print(f"{num1}나누기 {num2}는 {num1/num2}입니다.")
#
# except ArithmeticError:
#     print("산술연산 예외가 발생했습니다!")
#
# except ValueError:
#     print("입력값 예외가 발생했습니다!")


'''
리스트 만들기 - 숫자 4가지
인덱스 에러를 발생시켜서 인덱스 범위를 벗어났습니다. 출력
'''


# try:
#     list = [1, 2, 3, 4]
#     print(list[4])
#
# except IndexError:
#     print("인덱스 범위를 벗어났습니다.")


try:
    num1 = int(input("첫 번째 정수를 입력 : "))
    num2 = int(input("두 번째 정수를 입력 : "))
    print(f"{num1}나누기 {num2}는 {num1/num2}입니다.")

except ArithmeticError as e:
    print(f"산술연산 예외가 발생했습니다. 상세 메시지는 {e} 입니다.")

except ValueError as E:
    print(f"입력값 예외가 발생했습니다. 상세 에러 메시지는 {E} 입니다.")







