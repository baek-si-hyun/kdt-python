# f(x) = 2x+1
# def f(x):
#     return 2 * x + 1
#
# result = f(2)
# print(result)

# # 두 정수의 곱셈 함수
# def multiple(number1, number2):
#     return number1 * number2
#
# multiple(1,2)
# # 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# def divide(number1, number2):
#     if number2 != 0:
#         return number1 // number2, number1 % number2
#     return None
#
#
# # 1~10까지 print()로 출력하는 함수
# def print_from1_to10():
#     for i in range(10):
#         print(i + 1, end=' ')
#
#
# # 이름을 n번 print()로 출력하는 함수
# def fn4(name, number):
#     for i in range(number):
#         print(name)
#
#
# result = fn4('qortlgus', 4)
#
#
# # 1~n까지의 합을 구해주는 함수
# def fn5(number):
#     result = 0
#     for i in range(number):
#         result += i + 1
#         print(result)
#
#
# result = fn5(4)
#
#
# # 1~100까지 중 n의 배수를 print()로 출력하는 함수
# def fn6(number):
#     for i in range(100):
#         if number * (i + 1) <= 100:
#             print(i)
#
#
# result = fn6(4)
#
#
# # 세 정수의 뺄셈 함수
# def fn7(number1, number2, number3):
#     return number1 - number2 - number3
#
#
# fn7(3, 2, 1)


# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
def fn8(string, letter):
    length = string.count(letter)
    return length



print(fn8('qortlgussss', 's'))


'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수
'''
string, letter = input('문자열을 입력하세요: '), input('문자를 입력하세요: ')


def find_index_fn(string, letter):
    is_find = string.find(letter)
    find_index = 0
    if is_find != -1:
        find_index = string.index(letter)
    else:
        find_index = -1
    return find_index


result = find_index_fn(string, letter)
print(result)
