animals = ['dog', 'cat', 'bird', 'fish']
print(animals)
print(type(animals))

# 인덱스로 접근
# 인덱스가 0부터 시작하는 이유는 시작주소를 가지고 있기 때문이다
print(animals[1])
print(animals[2])

# 음수 인덱스 가능 (가장 마지막부터 순서대로 앞으로 이동한다)
# list의 길이 -1로 계산된다.
print(animals[-1])
# list의 길이 -2로 계산된다.
print(animals[-2])

# len()
print(len(animals))

# append()
animals.append('hamster')
print(len(animals))
print(animals)
# list는 중복을 허용한다
animals.append('cat')
print(animals)

# insert()
animals.insert(1, 'dog')
print(animals)

# remove()
animals.remove('fish')
print(animals)

# del()
del (animals[1])
print(animals)
del animals[1]
print(animals)

# clear()
# animals.clear()
# print(animals)

# index()
print(animals.index('bird'))
# print(animals.index('tiger'))

# 수정
index = animals.index('bird')
animals[index] = 'lion'
print(animals)

# 그 외
animals = ['dog', 'cat', 'bird', 'fish']
print(animals * 2)

print('dog' in animals)
print('tiger' in animals)

for animal in animals:
    print(animal)

# 실습
# 1~90까지 list에 담고 출력
list_data = [0] * 90
for i in list_data:
    list_data[i] = i + 1
print(list_data)

# 1~100까지 중 짝수만 list에 담고 출력
list_data = [0] * 50
for i in range(list_data):
    list_data[i] = (i + 1) * 2
print(list_data)

# 1~10까지 list에 담은 후 짝수만 출력
list_data = []
for i in range(10):
    i += 1
    print(i)
    if i % 2 == 0:
        list_data.append(i)
print(list_data)

# 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
list_data = ['박씨', '백씨', '김씨', '문씨']
list_data[1] = '고씨'
del list_data[-1]
print(list_data)

# '189,000 원'을 189000으로 변경 (제너레이터 사용)
string1 = '189,000 원'
list_data = []
for item in string1:
    list_data.append(item)
    if ',' in list_data:
        delete_index1 = list_data.index(',')
        del list_data[delete_index1]
    if ' ' in list_data:
        delete_index2 = list_data.index(' ')
        del list_data[delete_index2]
    if '원' in list_data:
        delete_index3 = list_data.index('원')
        del list_data[delete_index3]

string2 = ''
for item in list_data:
    string2 += item
print(string2)

# list안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
print(number_list[0][0])
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])
