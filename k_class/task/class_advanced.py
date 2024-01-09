# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).
class User:
    # private: 자신의 클래스에서만 접근 가능 (변수명 앞에 __ 붙인다)
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
    # 정적 변수는 필드의 모든 객체가 공유한다.
    __user_number = 0

    def __init__(self, user_id, user_password, user_name):
        # 생성자를 통해 객체를 생성할때 마다 정적변수에 1식 증가시킨다
        # 이유는 생성자가 실행 되었다는건 새로운 객체를 만들었다는 뜻이기 때문
        # 이 문제에서는 생성자가 실행되었다는건 사용자가 회원가입을 했다는걸 의미하기 때문이다.
        User.__user_number += 1
        # private 정적 변수는 외부에서는 사용을 못하지만 내부에서는 언제든 사용이 가능하다
        self.user_number = User.__user_number
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name

    @staticmethod
    def get_number():
        return User.__user_number

    @classmethod
    def set_admin(cls, **kwargs):
        kwargs['user_id'] = 'admin_' + kwargs['user_id']
        return cls(**kwargs)


user = User('hds', '1234', '한동석')
print(user.user_id)

admin = User.set_admin(user_id='hds', user_password='1234', user_name='한동석')
print(admin.user_id)


print(User.get_number())









