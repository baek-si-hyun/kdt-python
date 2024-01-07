def set_key(key):
    formatting = ''

    # 클로저
    def set_value(value):
        # set_value안에서 formatting를 수정하려면
        # nonlocal을 사용해서 사용만하는게 아니라 수정도 할거라고
        # 알려줘야한다
        # 파이썬은 함수 스코프 개념이다.
        # nonlocal을 안쓰고 set_value안에서 formatting 변수를 수정하게 되면
        # set_key에서 선언된 변수랑 완전 다른 변수라고 인식하게 된다
        # 그래서 nonlocal을 사용해서 외부변수를 사용중이라고 알려줘야한다
        nonlocal formatting
        formatting = f'{key}: {value}'
        # 굳이 return을 안해도 formatting은 수정된다
        # 하지만 set_value함수가 종료했을때
        # 결과값을 도출해야하기 때문에 return을 사용해야 한다
        return formatting

    # set_value의 주소값을 return한다
    # 이렇게 되면 함수를 실행하는게 아니라
    # 함수를 알아서 실행 할ㅅ수 있도록 위치값을 전달하는 것이다
    # 이렇게 되면 원할때 set_key함수에서 set_value함수를 꺼내 사용할 수 있다
    return set_value


set_name = set_key('이름')
formatting = set_name('백시현')

# '나이: 00살'
# 클로저를 사용하는 방법은 클로저를 감싸고 있는 외부함수를 호출하는 로직을 작성하고
# ex)'set_key()'
# 그뒤에 ()를 붙여주면 된다
# ex)'set_key()()'
print(f"{formatting}, {set_key('나이')('00살')}")


# 실습
# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.


def set_topic(**kwargs):
    # kwargs는 dict이다
    # kwargs에 'name'이라는 key값이 있는지 확인한다
    if 'name' in kwargs:
        # 함수안에 함수가 있으므로 클로저이다.
        # sep이라는 매개변수에 기본값으로 ', '을 사용한다 (default args)
        def set_format(sep=', '):
            # formatting을 선언하고 할당한 다음
            formatting = f'name{sep}{kwargs.get("name")}'
            # set_format의 실행 결과를 반환한다
            return formatting

        # set_format의 주소값을 result에 담았다
        result = set_format
    else:
        def set_format(sep=', '):
            formatting = f'{kwargs.get("topic")}{sep}{kwargs.get("point")}'
            return formatting

        result = set_format

    return result


print(set_topic(name='한동석')(': '))
print(set_topic(topic='지구 온난화', point='오존층 파괴를 막기 위해 인간이 해야할 일')('\n'))


# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

def set_product(*args):
    # args는 튜플이다
    number = 0
    # 상품 정보를 전달 받고 모든 요소에 number값을 추가한다
    for product in args:
        number += 1
        #product에 'number'라는 키가 없으면 새로운 키:값 을 추가한다
        product['number'] = number

    def insert(**kwargs):
        # insert함수 안에서 외부 함수의 number를 수정하려면 nonlocal을 사용해야한다
        nonlocal number, args
        number += 1
        # dict를 튜플로 감싸고 기존에 있던 args에 추가한다(병합)
        # 연산자를 사용하는 이유는 args는 불변성이기 때문에
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},

    def update(**kwargs):
        for product in args:
            if product['number'] == kwargs.get('number'):
                product['name'] = kwargs.get('name')
                product['price'] = kwargs.get('price')
                break

    def select_all():
        return args
    # dict형식으로 사용하고자 하는 클로저 함수를 사용 할수 있게 만든다
    return {'insert': insert, 'update': update, 'select_all': select_all}


products = [
    {'name': '마우스', 'price': 5000},
    {'name': '키보드', 'price': 25000}
]
# products가 리스트이지만 앞에 *을 붙여서 *products로 전달하게 되면 리스트가 풀리고 튜플로 전환된다.
product_service = set_product(*products)
# print(products)
product_service.get('insert')(name='모니터', price=80000)
# print(product_service.get('select_all')())
product_service.get('update')(name='키보드', price=20000, number=2)
# print(product_service.get('select_all')())
