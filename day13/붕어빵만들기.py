'''
붕어빵 클래스를 만들것
맛과 개수를 생성자로 생성할거임
붕어빵이 만들어지면 붕어빵 클래스와 메서드로 **맛 붕어빵 **개 나왔습니다~! 출력

붕어빵을 만들어달라고 할 때 어떤 맛 몇개 전달할거임
'''

class Fish_bread:
    def __init__(self,taste,count):
        self.taste = taste
        self.count = count
    def making(self):
        print(f"{self.taste}맛 붕어빵 {self.count}개 나왔습니다~!")


fish_bread1 = Fish_bread("피자",3)
fish_bread2 = Fish_bread("슈크림",1)
fish_bread3 = Fish_bread("팥",2)

fish_bread1.making()
fish_bread2.making()
fish_bread3.making()


