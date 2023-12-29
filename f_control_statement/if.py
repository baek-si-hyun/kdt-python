# number = 15
# if number % 3 == 0:
#     print(f'{number}는 3의 배수입니다.')
# if number % 5 == 0:
#     print(f'{number}는 5의 배수입니다.')

# number가 양수인지, 음수인지, 0인지 검사
# number = -9
# is_positive = number > 0
# is_negative = number < 0
#
# if is_positive:
#     print('양수입니다.')
# elif is_negative:
#     print('음수입니다.')
# else:
#     print('0입니다.')

# 나이를 입력받은 후 미성년자인지 검사
# message = '나이: '
# age = int(input(message))
# is_teenager = 0 < age < 20
# age_error = age <= 0
# if is_teenager:
#     print('미성년자입니다.')
# elif age_error:
#     print('잘못 입력하셨습니다.')
# else:
#     print('성인입니다.')

# 두 정수를 입력받은 후 대소 비교 진행
message = '정수 두개를 입력하세요'
examlple_message = 'ex) 1,2'
# 선언할 때 넣을 값을 모를 경우 초기값을 넣어준다
result_massage = ''

number1, number2 = map(int, input(message + '\n' + examlple_message + '\n').split(','))

# elif를 사용할때는 elif의 조건식만 보지말고 위의 if문의 조건식도 봐야한다
# 이유는 if의 조건식을 거쳤기 때문에 elif에서는 조건식을 두개를 사용한 것과 같기 때문이다.

# 일괄처리
# 각 분기별로 결과를 처리하기 않고
# 모든 분기 종료 후 한번에 처리하는
if number1 > number2:
    result_massage = f'{number1}이 {number2} 보다 큽니다.'
elif number1 != number2:
    result_massage = f'{number1}이 {number2} 보다 작습니다.'
else:
    result_massage = f'{number1}이 {number2} 과 같습니다.'

print(result_massage)

