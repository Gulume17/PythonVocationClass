'''
num = 7 원래 사용하던 변수
nums = [1,2,3,4] 여러개의 변수를 한꺼번에 생성
'''

number = [0,1,2,3] # 숫자 리스트
alphabet = ['a','b','c'] # 문자 리스트
bools = [True,False,True] # 논리값 리스트
greetings = ["hello" , "오늘은 파이썬" , "8일차"] # 문자열 리스트

mixed = [1,'apple',3.14,True] # 혼합리스트
print(mixed)
print(mixed[1]) # apple (1번째 출력) 0부터 시작

mixed[1] = 'mango' # apple -> mango로 바뀜
print(mixed[1]) # mango

print(mixed[-1]) # True (뒤에서 1번째 출력) 마이너스는 0부터 시작 X

# 오름차순으로 정렬
num_list = [99,98,97,95,96,92,94,93]
num_list.sort()
print(num_list)

# 내림차순으로 정렬
num_list = [99,98,97,95,96,92,94,93]
num_list.sort(reverse=True)
print(num_list)

korean = ["가","나","바","사","다","라","마","아","차","자","하"]
korean.sort()
print(korean)

korean2 = sorted(korean)
print(korean2) # 오름차순
print(korean)

korean = ["가","가","나","나","바","사","다","라","마","아","차","자","하"]
korean3 = sorted(set(korean))
print(korean3)

'''
sort : 오름차순 (기존 리스트 변경된)
sorted : 기존 리스트 변경 없이 오름차순
sort(reverse = True) : 역순으로 출력 (내림차순)
set() : 중복제거
'''