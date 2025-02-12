import time

def timer(second,callback):
    print("타이머 시작")
    print(f"{second}초 뒤에 요청한 함수를 호출합니다.")

    time.sleep(second)
    # time.sleep() : time모듈에 들어있는 기능 (프로그램을 일정 시간동안 멈추게 하는 함수)
    callback()

    print("타이머 종료")


def print_text():
    print("5초 뒤 실행될 함수입니다.")

timer(5,print_text)

