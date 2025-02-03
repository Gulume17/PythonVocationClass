'''
점수 입력받기
90점 이상이면 A학점 참 잘했어요
80점 이상이면 B
70 이상이면 C
범위안에 없다면 F학점으로 재시험
'''

score = int(input("점수를 입력해주세요 : "))
if score >= 90:
    print(f"{score}점수는 A학점 참 잘했어용~~")
elif score >= 80:
    print(f"{score}점수는 B학점")
elif score >=70:
    print(f"{score}점수는 C학점")
else:
    print(f"{score}점수는 F학점으로 재시험")


'''
좋아하는 달은 몇월입니까?
3,4,5 = 봄
6,7,8 = 여름
9,10,11 = 가을
12,1,2 = 겨울
'''

month = int(input("좋아하는 월은 몇월입니까? (1~12 중 택 1) : "))
if 3 <= month <= 5:
    print("봄을 좋아하시는군요!")
elif 6 <= month <= 8:
    print("여름휴가! 바다로 떠나용가리 ~")
elif 9 <= month <= 11:
    print("가을은 낙엽이 떨어지는 계절~")
else:
    print("겨울입니다. 스키장 가요~")