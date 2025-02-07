fruit_colors = {
    "Red" : "apple",
    "Yellow" : "banana",
    "Purple" : "blueberry"
}

#키 값을 출력해주세용
print(fruit_colors.keys())

for i in fruit_colors.keys():
    print(i)

# 리스트로 변경하기
color_list = list(fruit_colors.keys())
print(color_list)

# 추가하기
color_list.append("Pink")
print(color_list)


