'''
비행기는 총 3대 운항할 것
프로그램을 실행하면 (1번째 비행기 탑승 준비!) 출력
비행기는 여권을 가진 사람이 2명이 탑승하면 출발

승객에게 질문 : * 번재 고객님 여권이 있나요? (yes,no)
여권이 없다면 (여권이 없어요! 다음 승객 기다리기...) 출력 후
다음 승객에게 다시 여권 유무 묻기
여권 있는 승객이 나타났다면 * 번재 승객이 탑승했습니다! 출력 후
한명 밖에 안 탔으니까 다시 여권 유무 묻는 반복을 실행

여권을 가진 2명이 나타나서 승객이 다 채워졌다면
비행기 출발 후 다음 비행기 운항 (1번 째 비행기 탑승 준비!) 출력
'''

flight = 1
while flight <= 3:
    print(f"{flight}번째 비행기 탑승 준비!")
    passenger = 1
    count = 0
    while count < 2:
        passport = input(f"{passenger}번째 고객님 여권이 있나요? (y/n) : ")
        if passport != "y":
            print("여권이 없어요! 다음 승객 기다리기...")
            passenger += 1
            continue

        print(f"{passenger}번째 승객이 탑승했어요!")
        count += 1
        passenger += 1

    print("비행기 출발!")
    flight += 1
    print()











