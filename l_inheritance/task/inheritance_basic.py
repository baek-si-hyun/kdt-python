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
    # 자식 생성자를 통해 부모 생성자의 매개변수를 전달하기 때문에
    # 부모 생성자에게 해당 값들을 전달해줘야 한다
    # 그래야 부모클래스의 필드에 해당 값들을 메모리에 올릴수 있다
    def __init__(self, name, age, zoo):
        # super().__init__(부모 변수 필드들)을 전달한다
        # 부모클래스의 생성자에게 필드들을 전달하는 과정이다.
        super().__init__(name, age)
        # 자식 클래스의 필드는 따로 평상시 처럼 올린다.
        self.zoo = zoo

    def walk(self):
        super().walk()
        print('네발로 걷습니다.')


monkey = Monkey('김개똥', 20, '에버랜드')
monkey.walk()
