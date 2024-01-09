# TV에 사용한 필드를 재사용하기 위해 상속을 사용했다
class TV:
    def __init__(self):
        self.power = False
        self.channel = 1
        self.volume = 1

    def display_info(self):
        print(f'전원: {self.power}')
        print(f'채널: {self.channel}')
        print(f'불륨: {self.volume}')


tv = TV()
tv.display_info()


# SmartTV가 TV클래스를 상속받아 TV클래스의 필드를 사용할 수 있게 되었다
class SmartTV(TV):
    def __init__(self):
        # 직접 자식 자식 생성자를 생성하면 반드시 부모 생성자도 직접 호출한다
        # 직접 작성하지 않으면 생략되고 컴파일러가 알아서 해준다.
        super().__init__()
        # 부모클래스에서 사용하는 필드말고 새로운 필드를 추가하기 위해 __init__생성자를 직접 작성했다
        self.ip = '192.168.0.1'

    # 부모클래스와 같은 이름의 메서드를 자식클래스에서 선언하면 오버라이드 된다
    # 부모클래스의 객체에 접근할 경우 부모클래스에 있는 메서드가, 자식 클래스의 객체에 접근하면 자식 클래스의 메서드가 사용된다
    def display_info(self):
        # 부모클래스의 필드(메서드만) 접근하기 위해선 super()메서드를 사용해야 한다
        super().display_info()
        print(f'IP: {self.ip}')


# 자식 클래스의 생성자를 토앻 객체화 시키면 자식 생성자보다 부모 생성자가 먼저 실행된다
# 부모 클래스들의 필드들이 먼저 메모리에 올라가고 그다음 자식클래스의 생성자가 실행된다.
smart_tv = SmartTV()
smart_tv.display_info()
