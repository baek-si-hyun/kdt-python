# 문자열끼리만 연결(+)이 가능하다
# data = 3
# print('안' + str(data))

# name = input('이름: ')
# formatting = f'{name}님 환영합니다.'
# print(formatting)

# 제 이름은 ???, 키는 ???cm입니다.
# name = input('이름: ')
# body = input('키: ')
# formatting = f'제 이름은 {name}, 키는 {body}cm입니다.'
# print(formatting)

# 두 정수를 입력받은 후 곱셈 결과 출력
# message1 = '첫 번째 정수: '
# message2 = '두 번째 정수: '
# number1 = int(input(message1))
# number2 = int(input(message2))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
# print(formatting)

# message = '두 정수를 입력하세요'
# example = 'ex)1,2'
# number1, number2 = map(int, input(message + '\n' + example + '\n').split(' '))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
# print(result)

# map()은 값을 변경할때 사용한다.
# 현재 시간을 입력하고 시와 분으로 분리하여 출력
message1 = '현재 시간을 입력하세요'
example1 = 'ex) 2:30'
hours, minutes = input(message1 + '\n' + example1 + '\n').split(':')
formatting1 = f'{hours}시 {minutes}분'
print(formatting1)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
message2 = '전화번호를 입력하세요 (하이푼 포함)'
number1, number2, number3 = input(message2 + '\n').split('-')
print(number1 + number2 + number3)

# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
message3 = '이름과 나이를 입력하세요'
example3 = 'ex)백시현, 25'
name, age = input(message3 + '\n' + example3 + '\n').split(', ')
formatting2 = f'{name}님의 나이는{age}살'
print(formatting2)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
message4 = '세 정수를 입력하세요'
example4 = 'ex)1,2,3'
number1, number2, number3 = map(int, input(message4 + '\n' + example4 + '\n').split(','))
result = number1 + number2 + number3
formatting3 = f'{number1} + {number2} + {number3} = {result}'
print(formatting3)
