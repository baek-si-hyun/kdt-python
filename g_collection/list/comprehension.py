# Comprehension(어떤뜻을 내포하고 있다)
# 반복하거나 특정 조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension
# [표현식 for 항목 in iterator (if 조건)]
number_list = [1, 2, 3, 4]
result_list = [number * 3 for number in number_list]
print(result_list)

number_list = [1, 2, 3, 4]
# [6, 12]
result_list = [number * 3 for number in number_list if number % 2 == 0]
print(result_list)

# [표현식 if 조건 else 표현식 for 항목 in iterator]
# [1, 6, 3, 12]
number_list = [1, 2, 3, 4]
result_list = [number * 3 if number % 2 == 0 else number for number in number_list]
print(result_list)

# 아래의 list에서 '양수'만 추출한 뒤 새로운 list에 담기
number_list = [10, 20, 30, -20, -3, 50, -70]

result_list = [number for number in number_list if number > 0]
print(result_list)

# # n개의 0으로만 채워진 list
message = '정수를 입력하세요: '
length = int(input(message))
# number의 개수만큼 0을 출력해야 함으로 0을 입력
number_list = [0 for i in range(length)]
print(number_list)

# 제곱의 결과가 10보다 큰 결과만 담은 list
number_list = [1, -2, 3, -4, 5]
# 제곱의 결과가 10보다 커야함으로 number ** number > 10
# 그 이후 별다른 연산이 필요하지 않으므로 number
result_list = [number for number in number_list if number ** 2 > 10]
print(result_list)

# 0~9까지 중 3의 배수만 담은 list
# 3까지만 반복문을 돌아도 됨으로 if 0 < number <= 3
# 3을 곱해야 3의 배수가 완성 됨으로 number * 3으로 list에 담는다.
number_list = [number * 3 for number in range(10) if 0 < number <= 3]
print(number_list)
