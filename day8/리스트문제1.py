'''
여러가지 숫자가 있는 리스트에서 5 이상인 숫자만 비어있는 리스트에 추가하고 오름차순으로 변경해서 출력
3,7,8,6,10,4,2,5,0,1
'''

number = [3,7,8,6,10,4,2,5,0,1]
number_empty =[]

for num in number:
    if num > 5:
        number_empty.append(num)
number_empty.sort()
print(number_empty)




# append() : 리스트 끝에 요소를 추가하는 메서드




