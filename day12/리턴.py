'''
def 함수이름(매개변수1,매개변수2,매개변수3,...):
    코드
    return 함수 밖으로 전달하고 싶은 값
'''

def plus(a,b):
    return(a+b)

sum = plus(10,20)
print(sum)


def miltiply(num):
    result = num * 7
    return result

print(miltiply(3))


'''
7의 배수라면 True 반환
아니라면 False 반환
'''

def check_divide_seven(num):
    if (num % 7 ==0):
        return True
    else:
        return False

print(check_divide_seven(49))