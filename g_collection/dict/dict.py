# student = {
#     'name': '백시현',
#     'email': 'qortlgus100@gmail.com'
# }
#
# print(student['name'])
# print(student.get('name'))
# # get()을 사용하면 key를 찾지 못했을때 원하는 default 값으로 설정이 가능하다
# # default 값이 없을 때에는 None을 가져온다
# # print(student['phone']) # 오류
# print(student.get('phone', '01012341234'))
#
# # 'name' key값이 이미 있기 때문에 아래의 코드는 수정이다
# student['name'] = '홍길동'
# print(student)
#
# # 'phone'' key값이 없기 때문에 아래의 코드는 추가이다
# student['phone'] = '01022222222'
# print(student)
#
#
# if 'email' in student:
#     # 수정
#     student['email'] = 'hgd123@gmail.com'
# else:
#     # 추가
#     student['email'] = 'hgd123@gmail.com'
# print(student)
#
# my_dict = {
#     1: '백시현', 'two': '20살',
#     False: [10, 20, 30],
#     'row': [
#         {'name': 'ted', 'age': 40},
#         {'name': 'jack', 'age': 50},
#         {'name': 'john', 'age': 60}
#     ]}
#
# # row에 있는 3명의 회원 정보를 모두 출력
# data_list = my_dict.get('row')
# if 'row' in my_dict:
#     for item in data_list:
#         print(f'이름: {item.get("name")}, 나이: {item.get("age")}')
#
# # 1 ~ 10중 홀수와 짝수가 있다
# # 사용자가 '짝수'를 입력하면 짝수만 출력한다
# # '홀수'를 입력하면 홀수만 출력한다
# # dict를 사용한다
# data_dict = {'짝수': [i * 2 + 1 for i in range(5)], '홀수': [(i + 1) * 2 for i in range(5)]}
# print(", ".join(map(str, data_dict.get(input('짝수 혹은 홀수: ')))))

student = {
    'name': '백시현',
    'email': 'qortlgus100@gmail.com'
}
# 키 분리
print(student.keys())
# value 분리
print(student.values())
# item 분리
print(student.items())
for key, value in student.items():
    print(key, value)
