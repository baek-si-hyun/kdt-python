# 인간(부모)
# 이름, 나이
# 걷기
# '두 발로 걷습니다' 출력

# 원숭이(자식)
# 이름, 나이, 동물원이름
# 걷기
# '두 발로 걷습니다', '네발로 걷습니다.' 출력

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('두발로 걷습니다')


person = Person('김개똥', 20)
person.walk()


class Monkey(Person):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo

    def walk(self):
        super().walk()
        print('네발로 걷습니다.')


monkey = Monkey('김개똥', 20, '에버랜드')
monkey.walk()
