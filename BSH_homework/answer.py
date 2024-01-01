# # if문 정답
# result = ''
# message1, message2, message3, message4 = \
#     '당신은 외향적이신가요?', '당신은 감각적이신가요?', '당신은 이성적이신가요?', '당신은 계획적이신가요?'
# warning_message = '예 아니요로 대답하세요'
# answer1, answer2, answer3, answer4 = \
#     input(message1), input(message2), input(message3), input(message4)
# print(warning_message)
# if answer1 == '예':
#     result += 'E'
# else:
#     result += 'I'
# if answer2 == '예':
#     result += 'S'
# else:
#     result += 'N'
# if answer3 == '예':
#     result += 'T'
# else:
#     result += 'F'
# if answer4 == '예':
#     result += 'J'
# else:
#     result += 'P'
#
# print(f'당신의 mbti는 {result} 입니다.')
#
#
#
#
# # for문 정답
# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print(f"{i} * {j} = {result}")
#
#         if j == 6:
#             break
#     if i == 3:
#         break




# while문 정답
# boolean = False
# value = None
# condition1 = value == '박유진'
# condition2 = value == '박지원' or value == '문우람' or value == '백시현' or value == '김규일'
# while not boolean:
#     value = input("4조장 이름은? ")
#     if condition1:
#         print('정답입니다.')
#         boolean = True
#     elif condition2:
#         print('팀원 이름입니다. 조장이름을 입력하세요')
#     else:
#         print('다시입력하세요')

# boolean = False
# value = None
# while not boolean:
#     value = input("4조장 이름은? ")
#     if value == '박유진':
#         print('정답입니다.')
#         boolean = True
#     elif value == '박지원' or value == '문우람' or value == '백시현' or value == '김규일':
#         print('팀원 이름입니다. 조장이름을 입력하세요')
#     else:
#         print('다시입력하세요')