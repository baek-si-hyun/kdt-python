# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]

# len(args) = 3
# count = 2

# args.index(item) - count = -2
# 0-2
# args.index(item) - count = -1
# 1-2
# args.index(item) - count = 0
# 2-2
# args.index(item) - count = 1
# 3-2
# args.index(item) - count = 2
# 4-2
# args.index(item) - count = 3
# 5-2

pay = [10000, 4000, 5000]


# 컴프리헨션 사용
def user_coupon(*args, **kwargs):
    '''
    pay = [10000, 4000, 5000]
    :param args: 주문 금액들
    :param kwargs: coupon=할인율, count=쿠폰 개수
    :return: 할인율이 적용된 주문 금액들
    '''
    count = kwargs['count']
    discount = kwargs['coupon'] / 100
    result = [item if args.index(item) - count >= 0 else int(item - item * discount) for item in args]
    return result


print(user_coupon(*pay, coupon=40, count=1))


# 컴프리헨션 미사용
def user_coupon(*args, **kwargs):
    count = kwargs['count']
    result = []
    for item in args:
        if count == 0:
            result.append(item)
            continue
        else:
            apply_coupon = round(item * (1 - kwargs['coupon'] * 0.01))
            result.append(apply_coupon)
        count -= 1
    return result


print(user_coupon(*pay, coupon=10, count=1))


# 강사님
def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:
        return [
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None


help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=100)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')
