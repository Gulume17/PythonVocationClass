'''
range함수를 사용해서 2단 출력하기
'''

# for gugudan3 in range(1,10):
#     print(f"2 X {gugudan3} = {gugudan3 * 2}")

for gugudan in range(1, 10): # 단
    for gugudan2 in range(1,10):
        print(f"{gugudan} X {gugudan2} = {gugudan * gugudan2}")

    print()

    '''
    반복문의 종류에는 while,for
    break / continue
    '''
