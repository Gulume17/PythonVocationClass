'''
람다함수 : 익명함수

일반 함수
def 함수이름(매개변수):
    return 결과
=====================================
람다 함수
lambda 매개변수:결과
'''
from day9.리스트컴프리헨션 import even_numbers


#일반 함수
def add(x,y):
    return x + y
print(add(5,1))

# 람다 함수
lambda_function = lambda x,y : x + y
print(lambda_function(5,5))

# 람다 함수 심화
numbers = list(range(20))
print(numbers)

even_number = list(filter(lambda x : x % 2 == 0,numbers))
print(even_number)
# filter(function, iterable) : 조건에 맞는 요소만 걸러주는 함수
# function 조건 만족한다면 true 불만족 false

# 람다 정렬 ((x,y) 중 x번째 값 기준)
list_in_tuple = [(1,10),(4,2),(99,6),(5,1),(8,12),(-3,20)]
sorted_tuple = sorted(list_in_tuple)
print(sorted_tuple)

# 람다 정렬 ((x,y) 중 y번째 값 기준)
sorted_tuple2 = sorted(list_in_tuple,key=lambda index:index[1])
print(sorted_tuple2)


