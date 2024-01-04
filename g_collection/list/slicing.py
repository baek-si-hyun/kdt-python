# 인덱스 슬라이싱
animals = ['dog', 'dog', 'cat', 'bird', 'fish']

# list[inclusive_start=0 : exclusive_end=len(list)] -> list
print(animals[0])
print(animals[0:3])
print(animals[1:4])
print(animals[:2])
print(animals[2:])

# list[inclusive_start=0 : exclusive_end=len(list) : step=1] -> list
# step은 메모리를 많이 사용함으로 잘 사용하지 않는다.
food = ['noodle', 'meat', 'bread', 'chicken']
print(food[:3:2])
print(food[2::2])

# 역순 출력
# print(food[::-1])

# 실습
number_list = list(range(1, 11))
print(number_list)
# [1, 3, 5, 7, 9]
print(number_list[::2])
# [6, 5, 4, 3, 2]
print(number_list[5:0:-1])
# [2, 4, 6]
print(number_list[1:6:2])
# [2, 3, 4, 5, 6, 7]
print(number_list[1:7])

animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['panda', 'giraffe']

# 기존 값은 사라지고 zoo list 안에 있는 요소가 각각 들어간다.
animals[1:2] = zoo
print(animals)

# 기존 값은 뒤로 밀리고 해당 자리에 값이 들어간다.
animals.insert(animals.index('dog') + 1, 'giraffe')
print(animals)

# 기존 값은 뒤로 밀리고 zoo list 통채로 들어간다.
animals.insert(animals.index('dog') + 1, zoo)
print(animals)

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']
del animals[animals.index('cat')]
# animals.remove('cat')
list_data = ['hamster', 'fish', 'dog']
# animals[1] = list_data 과 animals[1:2] = list_data 차이점
# animals[1:2]를 하게 되면 ['hamster', 'fish', 'dog']의 요소들의 순회하기 때문에 list가 벗겨지게 된다.
# 하지만 그냥 animals[1]를 하게 되면 순회하지 않기 때문에 list자체가 들어가게 된다.
animals[1:2] = list_data
animals.insert(-1, 'whale')
print(animals)