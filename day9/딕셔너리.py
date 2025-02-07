'''
딕셔너리 : 키와 쌍으로 이루어진 데이터 구조

key1 : value,
key2 : value2
'''

me = {
    "name" : "ParkJunSeok",
    "age" : 20, # 숫자나 불리언 값은 따옴표 없이 사용 가능
    "phone" : "010-1234-5678",
    "class" : ["c언어","python","java"] # 값을 리스트로도 가질 수 있다.
}
print(me)
print(me["phone"])
print(me["name"])
print(me["age"])
print(me["class"])
print(me["class"][0])

# 폰에 대한 딕셔너리
# 키 : name / price / color / storage

my_phone = {
    "name" : "IPhone 25",
    "price" : "2000000 원",
    "color" : "Black",
    "storage" : "100TB"
}

print(my_phone)
print(my_phone["name"])
print(my_phone["price"])
print(my_phone["color"])
print(my_phone["storage"])

friends = {} # 빈 딕셔너리
friends["도현"] = 19 # 정보 추가
friends["길동"] = 27 # 정보 추가
print(friends)
print(friends["길동"])

friends["도현"] = 29 # 도현 정보 수정
print(friends)

del friends["길동"] # 길동 삭제
print(friends)

friends.clear() # 모든 정보 초기화
print(friends)