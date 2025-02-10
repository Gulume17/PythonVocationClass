'''
딕셔너리 만들기
딕셔너리 값이 학생들이 좋아하는 과목 리스트일것 (2가지)

어떤 과목을 좋아하는 학생을 찾을까요? - 과학

**학생이 **을(를) 좋아해요!
'''

students = {
    "정우" : ["체육" , "과학"],
    "범진" : ["영어" , "국어"],
    "승진" : ["체육" , "수학"],
    "한별" : ["국어" , "과학"],
    "수빈" : ["영어" , "미술"]
}

subject_input = input("어떤 과목을 좋아하는 학생을 찾을까요?")

found = False # 과목을 찾았는지 여부를 저장할 변수

for name,subject in students.items():
    if subject_input in subject:
        print(f"{name} 학생이 {subject}을(를) 좋아합니다!")
        found = True # 과목을 찾았으면  True로 변경

if not found:
             print(f"입력하신 {subject_input}은(는) 없는 과목입니다.")



