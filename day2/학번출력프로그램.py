# 학번 입력받기

# 1번째 숫자는 학년
# 2번째 숫자는 반
# 3번째 숫자는 번호
# *학년 *반 *번

student_id = input("4자리 학번을 입력하세요 : ")

grade = student_id[0]
class_num = student_id[1:2] # [2]랑 같다.
student_num = student_id[2:4]

print(f"{grade}학년 {class_num}반 {student_num}번")
