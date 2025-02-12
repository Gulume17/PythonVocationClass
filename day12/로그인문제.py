'''
1.정해진 아이디와 비밀번호를 만들어놓기
2. 함수를 만들어서 두개의 매개변수르 받을것! (id,pw)
3. 매개변수로 받은 아이디와 정해진 아이디가 일치하고 , 비번도 일치하면 = 로그인 되었습니다.
4. 아이디 맞고 비번을 틀림 = 비번 불일치
5. 아이디 불일치 = 아이디 불일치
'''

right_id = "junseok"
right_pw = 1234

def login(id,pw):
    if right_id == id:
        if right_pw == pw:
            print("로그인 되었습니다!")
        else:
            print("비밀번호가 일치하지 않습니다.")
    else:
        print("아이디가 일치하지 않습니다.")


user_id = input("아이디를 입력하세요 : ")
user_pw = int(input("비밀번호를 입력하세요 : "))

login(user_id,user_pw)




