class Car:
    # 정적변수(static variable)
    # 객체를 통해 접근하지 않아도 된다
    # 모든 객체가 공유한다
    # 클래스에서 직접 접근한다
    # 생성자를 통해서 메모리에 올라가는게 안니라
    # 컴파일러가 제일 먼저 그냥 메모리에 올린다
    wheel = 4

    def __init__(self, brand='', color='', price=0):
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_end(self):
        print(self.brand + '시동 꺼짐')


# mom_car = Car('Benz', 'black', 15000)
# daddy_car = Car('bmw', 'blue', 8800)
#
# mom_car.engine_start()
# daddy_car.engine_start()
#
# print(Car.wheel)
# Car.wheel = 6
# print(Car.wheel)

cars = [Car, Car]
mom_car = cars[0]()
daddy_car = cars[1]()
print(mom_car, daddy_car, sep='\n')
