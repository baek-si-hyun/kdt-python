# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
# message = '이메일을 입력하세요\n'
# email_id, email_domain = input(message).split("@")
# formatting = f'id: {email_id}\ndomain: {email_domain}'
# print(formatting)
'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''
# round(값, 원하는 자리수): 소수점이 맞춰진 결과값
yard_message = 'yard 입력: '
inch_message = 'inch 입력: '

yard, inch = float(input(yard_message + '\n')), float(input(inch_message + '\n'))

yard_conversion = round(yard * 91.44, 2)
inch_conversion = round(inch * 2.54, 2)

result_message = f'{yard} yard는 {yard_conversion}cm\n{inch} inch는 {inch_conversion}cm'
print(result_message)
