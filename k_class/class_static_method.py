class Student:
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    # static method는 self를 사용하고 싶지 않을때 사용한다
    # 대신 해당 메서드는 필드에 올라가는게 아니라 정적 변수들과 함께 클래스가 실행되자마자 메모리에 올라간다
    # 그래서 객체 접근해서 사용하는게 아니라 클래스에 접근해서 사용해야 한다
    @staticmethod
    def print_start_time_of_study():
        print('9시 땡')
        Student.status = '공부 중'


han = Student(0, 0, 0)
hong = Student(0, 0, 0)
print(Student.status)

Student.print_start_time_of_study()

print(Student.status)
