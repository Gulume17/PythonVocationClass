'''
# 함수의 장점
1. 반복적인 코드 제거 및 재사용성 향상
2. 코드의 가독성 및 유지보수 향상
3. 오류 추적 및 디버깅 용이

# 함수의 기본형태
def 함수이름():
    코드1
    코드2
    코드3
'''

def hello(): # 함수 선언
    print("안녕 하세요")
    print("저는 준석 입니다.")
    print("파이썬 수업 중 입니다.")

hello() # 함수 호출

colors = ["red","orange","yellow","green","skyblue"]
index = 0

def change_color():
    global index # 함수 밖에 있는 변수를 가져온다
    if index >= len(colors):
        index = 0
    print(f"배경색을 {colors[index]}로 변경합니다.")
    index += 1

change_color() # red
change_color() # orange
change_color() # yellow
change_color() # green
change_color() # skyblue
change_color() # red




