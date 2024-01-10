class A:
    # __new__메서드는 생략되어 있다
    # 메모리에 필드를 할당하는 메서드는 __new__이다
    # 실제로 생성자는 __new__이지만 생략되어있기 때문에
    # __init__을 생성자라고 많이들한다
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = super().__new__(cls)
        return obj

    # __new__가 할당한 주소를 self를 통해 __init__이 받은것이다.
    # 우리가 원하는 데이터들을 받아서 처리하는 메서드는  __init__이다.
    # __new__가 메모리에 필드를 할당해야 필드의 주소를 가져올수 있기 때문에
    # 항상 __init__보다 __new__가 먼저 실행된다.
    def __init__(self, data1, data2, name=''):
        print('__init__')
        print(self)
        # self.하면 해당 필드에 접근한다는 뜻이다
        # 이유는 __new__가 할당한 필드를 self를 통해 사용할 수 있기 때문이다.
        # self는 필드의 주소값을 가지고 있다.
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # def print_name(self, name):
    #     print(name)

    def print_name(self):
        print(self.name)


# a는 객체이다
# 생성자를 통해 객체를 생성하고
# 이 객체는 필드의 주소값을 가지고 있다.
# A()는 생성자이고 필드를 구체화 시키는 객체화 작업을 진행한다
# a는 객체화의 결과인 객체이다
# a = A()
a = A(10, 20, 'a')
print(a)
# a.data1 = 10
# a.data2 = 20
print(a.data1, a.data2)
# a.print_name('a')
a.print_name()

# b = A()
b = A(100, 200, 'b')
print(b)
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()
