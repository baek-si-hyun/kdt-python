# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트
# 전체 내용을 문자열로 가져오기: file.read()

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

# alice.txt 파일을 가져와서 읽는다
with open('alice.txt', 'r', encoding='utf-8') as file:
    # 해당 파일의 데이터를 가져오서 바로 전부 소문자로 변환한다
    content = file.read().lower()

# temp는 임시 저장소라는 뜻의 변수명이다
temp = ""
# content는 문자열이다. 문자열은 각 자리마다 인덱스를 가짐으로 반복문이 가능하다
for character in content:
    # 'a' ~ 'z'는 아스키 코드값을 가져와서 비교한다
    if 'a' <= character <= 'z':
        # a~z까지만 문자열을 이어붙인다
        temp += character
        continue
    # 모든 단어가 띄워쓰기 없이 이어지는 것을 막기위해 반복문을 한번씩 돌때마다 공백을 넣어준다
    temp += " "

content = temp

words = [
    word
    for word in content.split()
    if len(word) > 1
]

result = {}
for word in words:
    if result.get(word) is not None:
        # result.get()이 값을 찾으면 해당 key값의 value에 1을 더해준다
        result[word] += 1
    # 그렇지 않으면 아직 해당 키가 없다는 뜻으로 새로운 요소를 추가해준다
    else:
        result[word] = 1
# comprehantion을 앞에 key:value로 사용하고 {}로 감싸면 dict타입으로 result가 생성된다
result = {word: result[word] for word in result if result[word] >= 100}
# dict에서 sordted는 key값으로 정렬이 아니라 값으로 정렬을 할것이기 때문에 result.get 함수를 key로 전달해서 정렬하고 reverse한다
# 정렬은 값으로 했지만 리턴은 key값을 리턴한다
sorted_key = sorted(result, key=result.get, reverse=True)
# 정렬 순서대로 key값을 정렬한 sorted_key을 가지고 다시 값과 함께 출력한다
for key in sorted_key:
    print(key, result[key])

#
#
#
# def change(data):
#     return data * -1
#
# datas = [1, 2, 3, 4]
#
# print(sorted(datas, key=change))

# print(list({"A": 1, "B": 2, "C": 3}))