class A:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.age = 20
        # 항상 상속의 관계에서는 부모 클래스가 자식 클래스 보다 먼저 생성자가 실행된다.
        print('부모 생성자')

    def print_intro(self):
        print('A')


class B(A):
    def __init__(self, name):
        super().__init__(name)
        print('자식 생성자')

    def add(self, number1, number2):
        return number1 + number2

    # 부모클래스의 메서드 중 같은 이름의 메서드를 자식 클래스에서 사용하고 싶거나
    # 부모클래스의 메서드를 사용하고 싶지 않고 새로 만들고 싶거나
    # 부모클래스의 메서드의 기능은 유지하고 기능을 추가 하고 싶을 때
    # 오버라이드라는 기술을 사용한다.
    def print_intro(self):
        # super()는 부모의 메소드를 그대로 사용하고자 할 때(선택 사항)
        # 부모클래스 필드중 변수를 사용하고 싶다면 self로 접근하면 된다
        # super는 무조건 메서드만 가능하다
        super().print_intro()
        # 부모 필드 변수는 self를 사용하면 된다.
        print(self.age)
        # 자식의 메소드에서 추가할 내용 작성
        print('B')

# B클래스 생성자를 통해서 B 객체 생성
b = B('백시현')
print(b.name)
# b객체를 통해 B필드에 접근해서 print_intro메서드 실행
b.print_intro()
print(b.add(1, 2))

a = A('홍길동')
a.print_intro()
