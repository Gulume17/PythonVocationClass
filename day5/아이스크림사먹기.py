'''
우리가 가진돈 : 5000 원
아이스크림 : 1000
아이스크림을 2번 사먹을거임

아이스크림을 1번 사먹었다! 남은 돈 ?? 원
아이스크림을 2번 사먹었다! 남은 돈 ?? 원
'''

money = 5000
icecream_price = 1000
icecream_count = 1

while icecream_count <= 2:
    money -= icecream_price
    print(f"아이스크림을 {icecream_count}번 사먹었다! 남은 돈은 {money}원 밖에 안남음 ㅜㅜ")
    icecream_count += 1


