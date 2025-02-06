'''
리스트 결합
1. + 연산자
2. extend() : 기존 리스트에 추가
'''

list1 = ['a','b','c']
list2 = ['d','e']

# + 연산자
list3 = list1 + list2
print(list3)

# extend()
list1.extend(list2)
print(list1)

# + 는 새로운 리스트를 생성하기 때문에 기존의 리스트는 변하지 않는다.
# extend() 메서드는 기존 리스트에 새로운 리스트를 추가하여 리스트를 확장하는 기능 (원본 변경됨)

list4 = list2 * 3 # 곱한 수 만큼 반복함
print(list4)

result = len(list4)
print(result)


# in 연산자 - True / False 중 하나로 출력 됨
print('d' in list4)

# count()
result2 = list4.count('e')
print(result2)

list5 = [99,55,12,469,72,3,2,14,6,8]
print(max(list5)) # 최대값
print(min(list5)) # 최소값

