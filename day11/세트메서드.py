'''
요소 추가하기
1. add() : 한 번에 하나의 요소를 추가
2. update() : 여러개의 요소를 한 번에 추가 (리스트나 튜플도 인자로 받아들임)

요소 삭제하기
1. remove() : 특정 요소 제거 (제거할 요소가 없으면 오류 발생)
2. discard() : 특정 요소를 제거 (요소가 없어도 오류 발생 X)
3. pop() : 임의의 요소를 제거하고 반환 (순서 없음)
4. clear() : 세트의 모든 요소를 제거
'''

# add()
set = {1,2,3}
set.add(4)
print(set)

# update()
set.update({5,6})
print(set)

# remove()
set_b = {"a","s","d","f","g","h","j","k","l"}
set_b.remove("a")
print(set_b)
# set_b.remove("강아지") # 제거할 요소가 없으므로 오류가 발생
print(set_b)

# discard()
set_b.discard("고양이") # 요소가 없어도 오류 발생 X
print(set_b)

# pop()
set_red={'r','e','d'}
print(set_red)
print(set_red.pop()) # 임의의 요소를 랜덤하게 제거
print(set_red)

# clear()
set_blue={'b','l','u','e'}
set_blue.clear()
print(set_blue)




