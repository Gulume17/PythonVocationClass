'''
"바" 가 들어있는 단어들만 새 리스트에 추가
["사과","바나나","포도","딸기","망고","바람","바이올린"]
in연산자 활용
'''

words = ["사과","바나나","포도","딸기","망고","바람","바이올린"]
select_word = []

for word in words:
    if "바" in word:
        select_word.append(word)
print(f"선택된 단어들 : {select_word}")

