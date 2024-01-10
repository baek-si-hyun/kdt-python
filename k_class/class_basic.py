# 동물
# 이름, 나이, 성별, 음식 개수, 체력 개수
# 먹기, 산책하기

class Animal:
    # __new__ 메서드는 생략되었다
    # __init__메서드는 __new__메서드에서 메모리에 할당한 필드의 주소를 가지고있다
    # 필드에 올라간 변수들은 self를 통해 접근할 수 있다
    # feed_count = 1, life = 1 는 default args를 사용했다
    def __init__(self, name, age, gender, feed_count=1, life=1):
        # 생성자가 매개변수로 받는 값들을 필드에 올리는 과정
        self.name = name
        self.age = age
        self.gender = gender
        self.feed_count = feed_count
        self.life = life

    # 음식 1개 소모, 제력 1개 획득
    def eat(self):
        self.feed_count -= 1
        self.life += 1

    # 체력 1개 소모, 음식 1개 획득
    def walk(self):
        self.feed_count += 1
        self.life -= 1

tiger = Animal(name='호랑이', age=20, gender='수컷')
lion = Animal(name='사자', age=10, gender='암컷')
print(tiger.name, tiger.age, tiger.gender, tiger.feed_count, tiger.life)
