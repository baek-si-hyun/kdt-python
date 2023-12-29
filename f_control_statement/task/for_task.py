# 1~15까지 출력
# for i in range(15):
#     print(i+1)

# 30~1까지 출력
# for i in range(30, 0, -1):
#     print(i+1)

# 1~100까지 중 홀수만 출력
# for i in range(50):
#     print(i * 2 + 1, end=' ')

# 1~10까지 합 출력
# num=0
# for i in range(10)
#     num += i + 1
# print(num)

# 1~n까지 합 출력
# num=0
# for i in range(50):
#     num += i
# print(num)

# 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(3):
#     print(i % 4 + 3, end=' ')


# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 횐색



# '1,235,500'를 1235500으로 출력
data = '1,235,500'
result = ''
for i in data:
    if i != ',':
        result += i

result = int(result)
print(result + 5)
