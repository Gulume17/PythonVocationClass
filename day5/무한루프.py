# 무한루프
'''
count = 0
while count < 3:
    print(count)
'''

# break : while 문을 강제로 종료함
# continue : while 문의 다음에 오는 코드를 무시 하고 조건을 검사

count = 0
while count < 10:
    print(count)
    count += 1

# break
while count == 5:
    break
# count < 5
print()
print()

# continue
num = 0
while num < 20:
    num += 1
    if num == 5:
        continue # 실행되었다면 다음에 오는 코드를 무시하고 다음 반복을 실행
    print(num,end=" ") # 가로로 코드가 나옴 "" 안에는 , 혹은 공백을 많이 씀