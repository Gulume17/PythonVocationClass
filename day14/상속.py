'''
상속이란 부모클래스(슈퍼클래스)가 가지고 있던 속성과 메서드들을
자식 클래스(서브클래스)가 물려받아 사용하는 개념
'''

class Animal:
    def __init__(self,type):
        self.type = type

    def make_sound(self):
        print("소리를 냅니다!")


class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__("강아지")
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("멍멍!")
    # overriding : 재정의

dog = Dog("구름","말티즈")
print(f"{dog.name}은(는) {dog.breed}이며, {dog.type}입니다.")
dog.make_sound()

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__("고양이")
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("야옹!")

cat = Cat("나비","턱시도냥")
print(f"{cat.name}은(는) {cat.breed}이며, {cat.type}입니다.")
cat.make_sound()

class Bird(Animal):
    def __init__(self,name,breed):
        super().__init__("새")
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("짹짹!")

bird = Bird("짹짹이","참새")
print(f"{bird.name}은(는) {bird.breed}이며, {bird.type}입니다.")
bird.make_sound()



animals = [Dog("바둑이","리트리버"),Cat("치즈","길냥이"),Bird("짹짹이","참새")]
for animal in animals:
    print(f"{animal.type}({animal.name}) 이(가) 소리를 냅니다.")
    animal.make_sound()






