print("교집합")
# 세트의 교집합
'''
1. &연산자 사용 : 두 세트를 &연산자로 연결하여 새로운 세트를 만들며, 이 때 중복되는 요소는 제거한다.
2. intersection() : 두 세트를 인자로 전달하여 교집합을 반환
'''

set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a)
print(set_b)

# intersection()
intersection_a_b = set_a.intersection(set_b)
print(intersection_a_b)

# &연산자 사용
a_and_b = set_a & set_b
print(a_and_b)

'''
과일바구니 : strawberry orange cherry
내가 좋아하는 과일 : grape orange strawberry
'''
set_fruits = ("strawberry" , "orange" , "cherry")
set_favorites = {"grape" , "orange" , "strawberry"}

# &연산자 사용
and_fruits = set_fruits & set_favorites
print(and_fruits)

# intersection()
intersection_fruits = set_fruits.intersection(set_favorites)
print(intersection_fruits)

print()
print("합집합")
# 세트의 합집합
'''
1. | (하이프) 연산자 사용
2. union() 사용
'''

set_c = {1,2,3}
set_d = {3,4,5,}

# | (하이프) 연산자 사용
pipe_set = set_c | set_d
print(pipe_set)

# union() 사용
union_set = set_c.union(set_d)
print(union_set)

'''
수학반 : 엘사 , 모아나 , 라푼젤
과학반 : 엘사, 안나, 모아나
학원생 전원의 명단을 뽑아보기
'''

# | (하이프) 연산자 사용
student_math = {"엘사","모아나","라푼젤"}
student_science = {"엘사","안나","모아나"}
all_student = student_math | student_science
print(all_student)

# union() 사용
all_student_union = student_math.union(student_science)
print(all_student_union)

print()
print("차집합")
# 세트의 차집합
'''
1. - 연산자 사용
2. difference() 
'''

set_e = {1,2,3,4}
set_f = {3,4,5,6}

# - 연산자 사용
minus_set = set_e - set_f
print(minus_set)

# difference()
difference_set = set_e.difference(set_f)
print(difference_set)

'''
음악반 학생 : 알라딘 오로라 자스민
역사반 학생 : 오로라 자스민
음악만 공부하는 학생 출력하기
'''

student_music = {"알라딘" , "오로라" , "자스민"}
student_history = {"오로라" , "자스민"}

# - 연산자 사용
only_music = student_music - student_history
print(only_music)

# difference()
only_music_method = student_music.difference(student_history)
print(only_music_method)
