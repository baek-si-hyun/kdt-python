# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
#
# # 추가(초보자용)
# # def insert(*, number, name):
# #     '''
# #
# #     :param number: 회원 번호
# #     :param name: 회원 이름
# #     '''
# #     user_info.append({'number': number, 'name': name})
#
#
# # 추가
# # 회원 번호는 자동 증가한다.
# number = 5
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': name})
#
#
# # 목록
# def select_all():
#     return user_info
#
#
# # 조회(번호로 조회)
# def select(number):
#     for user in user_info:
#         if user['number'] == number:
#             return user
#     return {}
#
#
# # 수정(번호로 이름 수정)
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#     '''
#     select(kwargs.get('number'))['name'] = kwargs.get('name')
#
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 전역변수
number = 5


# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
def insert(**kwargs):
    '''

    :param kwargs: {'title': '게시글 제목', 'content': '게시글 내용', 'file': '파일의 경로'},
    :return:
    '''
    global number
    number += 1
    post = {
        'number': number,
        'title': kwargs.get('title'),
        'content': kwargs.get('content'),
        'file': kwargs.get('file'),
        'read_count': 0
    }
    # append()를 사용하게 되면 list의 마지막 요소로 추가된다
    post_info.append(post)


# 목록(최신순으로 조회)
def select_all():
    # slice를 사용해 역순으로 정렬한다
    return post_info[::-1]


# 조회(번호로 조회, 조회수 1 증가)
# update()와 delete()에도 select()함수가 사용됨으로
# select()와 조회수를 카운팅하는 read()를 분리한다
# 하나의 함수에는 왠만하면 하나의 기능만 만들수 있게 신경쓰자
def read(number):
    # select()함수에 number를 전달하고
    # select()함수의 리턴값을 post에 저장한다
    post = select(number)
    post['read_count'] += 1
    return post


def select(number):
    # post_info을 global로 선언해 사용하지 않는 이유는
    # list인 post_info를 재할당하지 않았기 때문이다.
    for post in post_info:
        if post['number'] == number:
            return post
    # for문 안에서 if문의 조건에 만족하지 않으면 아무 값도 return하지않는다
    # 하지만 select()는 반드시 리턴값이 있어야하는 함수이다
    # 이유는 select함수의 목적과 재사용성 용이함이 있다
    return {}


# 수정(번호로 정보 수정)
def update(**kwargs):
    # list에서 dict로 이루어진 요소를 통째로 바꾸는 방법도 있다
    # 하지만 추후 DB를 작업하기 용이하기 위해서,
    # 코드의 가독성 등의 이유로 요소인 dict의 내부의 값을
    # 직접 수정해 주는게 좋다/많이 쓰인다
    post = select(kwargs.get('number'))
    post['title'] = kwargs.get('title')
    post['content'] = kwargs['content']
    post['file'] = kwargs.get('file')


# 삭제(번호로 삭제)
def delete(number):
    # select함수 number값을 전달하면 post_info의 요소들 둥
    # number와 같은 값을 가진 post_info의 요소를 가져올수 있다
    # post_info의 요소중 하나를 index()의 인수로 전달하게 되면 해당 요소의 index값을 구할수 있다
    # post_info[post_info.index(select(number))로부터 받은 인덱스 값이 들어온다]
    # 앞에 del을 사용하면 해당 index를 가진 요소가 삭제된다
    del post_info[post_info.index(select(number))]


# **kwargs는 dict 타입이다.
insert(title='테스트 제목6', content='테스트 내용6', file='')
print(select_all())
print(read(5))
print(read(5))
print(read(5))
post = read(5)
post['title'] = '수정된 제목'
# update 함수는 인수로 **kwargs을 받는다
# 그러므로 update함수는 인자를 전달받을때
update(number=1, title='Updated Title', content='Updated Content', file='/usr/post/file/updated.png')
# 형식으로 전달 받아야하지만 dict자체를 전달받을때는 인자 앞에 **을 붙여야한다
# {'number': 1, 'title': 'Updated Title', 'content': 'Updated Content', 'file': '/usr/post/file/updated.png'}을
# number=1, title='Updated Title', content='Updated Content', file='/usr/post/file/updated.png' 이렇게 알아서 바꿔준다
update(**post)
print(read(5))
delete(5)
print(select_all())
