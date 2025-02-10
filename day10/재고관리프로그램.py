'''
창고에 4종류의 과자가 있고 각각 10개 3개 0개 5개의 재고
재고가 0 개라면 재고가 없습니다!
재고가 5개 미만이라면 재고가 부족합니다 현재 *개 남음
재고가 5개보다 많다면 재고 충분!(현재 *개 남음) 출력

items()
for 1,2 in 딕셔너리.items():
'''

stock = {
    "과자 1" : 10,
    "과자 2" : 3,
    "과자 3" : 0,
    "과자 4" : 5
}

for stock1,stock2 in stock.items():
    if stock2 == 0:
        print (f"{stock2}의 재고가 없습니다.")
    elif stock2 < 5:
        print(f"{stock2}의 재고가 부족합니다. 현재 {stock2}개 남음")
    else:
        print(f"{stock2}의 재고가 충분합니다! 현재 {stock2}개 남음")

    # items()를 사용해서 키값, 벨류값을 모두 가져와서 접근이 가능하다.