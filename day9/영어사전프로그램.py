'''
딕셔너리 생성
flower : 꽃
food : 음식
4가지 생성

사용자로부터 영어 단어 입력받기
사용자가 입력한 단어가 딕셔너리에 있는지 확인 (in 연산자)
사용자가 입력한 단어가 있다면 flower : 꽃 출력
사용자가 입력한 값이 사전에 없다면
단어의 뜻을 입력해 주세요
입력한 단어와 뜻을 딕셔너리에 추가
 food : 음식 (사전에 추가되었습니다!)  출력
'''

english_dict = {
    "flower" : "꽃",
    "food" : "음식",
    "dog" : "강아지",
    "cat" : "고양이"

}

user_word = input("영어 단어를 입력하세요 : ")
if user_word in english_dict:
    print(f"{user_word} : {english_dict[user_word]}")
else:
    print(f"{user_word}는 사전에 없습니다.")
    add_value = input("단어의 뜻을 입력하세요 : ")
    english_dict[user_word] = add_value
    print(f"{user_word} : {english_dict[user_word]} (사전에 추가되었습니다!)")
