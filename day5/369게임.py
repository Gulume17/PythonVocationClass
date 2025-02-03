'''
초기값 : 0
반복문을 사용해서 10까지 증가
3의 배수라면 "짝" 을 출력
'''

game = 0

while game < 10:
    game += 1
    if game % 3 == 0:
        print("짝", end = " ")
        continue
    print(game, end = " ")