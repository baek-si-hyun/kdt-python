class A:
    pass


class B(A):
    pass


a = A()
b = B()

print(isinstance(a, A))
print(isinstance(b, B))
# 모든 자식 타입은 본인 타입이면서도 부모 타입이다
# 모든 자식은 부모 타입이다.
print(isinstance(b, A))
# 부모는 절대 자식 타입일 수가 없다
print(isinstance(a, B))
