'''
문자열의 특징
1. 순서(인덱스)가 있다 -> 0부터 시작
2. 한 번 만들어진 문자열은 수정할 수 없다. (text[0] = "언")
3. 여러가지 함수를 사용할 수 있다!
'''

text = '안녕하세용'
print(text[0]) # 안
print(text[-1]) # 용

'''
대소문자 변환
1. upper() - 대문자로 변환
2. lower() - 소문자로 변환
3. capitalize() - 첫글자만 대문자로 변환

문자열 찾기
1. find() - 특정 글자가 어디에 있는지 찾기
2. count() - 특정 글자가 몇 번 등장하는지 세기

문자열 변경하기
1. replace() - 특정 글자를 다른 글자로 바꾸기

문자열 나누고 합치기
1. split() - 특정 기준으로 문자열 나우기 (리스트로 변환)
2. join() - 리스트를 문자열로 합치기

공백제거함수 
1. strip() -  양쪽 공백 제거
2. lsrtip() - 왼쪽 공백 제거
3. rstrip() - 오른쪽 공백 제거

문자열이 특정조건을 만족하는지 확인하기
1. startswith() - 특정문자로 시작하는지 확인
2. endswith() - 특정문자로 끝나는지 확인
3. isdigit() - 숫자로만 이루어져 있는지 확인
4. isalpha() - 알파벳으로만 이루어져 있는지 확인

문자열 길이 구하기
1. len() = 문자열의 글자 개수 구하기
'''

# upper
hello = "hello"
print(hello.upper())

# lower
python = "PYTHON"
print(python.lower())

# capitalize
money = "money"
print(money.capitalize())

# find
find_text = "find text"
print(find_text.find("text"))
print(find_text.find("java")) # 찾는 글자가 없다면 -1 출력

# count
banana = "banana"
print(banana.count("a")) # a가 3개

# replace
replace_text = "I Like dog"
print(replace_text.replace("Like","Love"))

# split
split_text = "apple,pizza,pasta"
print(split_text.split(","))

# join
words = ['apple,pizza,pasta']
print(",".join(words))

# startswith
swith_text = "start swith"
print(swith_text.startswith("start")) # true
print(swith_text.startswith("swith")) # false

# endswith
print(swith_text.endswith("start")) # false
print(swith_text.endswith("swith")) # true

# isdigit
isdigit_text = "12345"
print(isdigit_text.isdigit()) # true

isdigit_text = "12345abc"
print(isdigit_text.isdigit()) # false

#isalpha
isalpha_text = "python"
print(isalpha_text.isalpha()) # true

isalpha_text = "python345"
print(isalpha_text.isalpha()) # false

# len
len_text = "eunji"
print(len(len_text)) # 5





