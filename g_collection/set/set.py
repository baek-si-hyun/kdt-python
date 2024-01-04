# 중복이 없고 순서가 없다
# 값을 가져올수 없다
# 값이 있는지 없는지 확인용
# 중복제거용

# 중관호를 썻다고 dict로 보면 안됨
world_set = {'korea', 'america', 'japan', 'china'}

print(type(world_set))
print(len(world_set))
# print(world_set[1]) # set은 가져올수 없다
world_set.add('korea')
# print를 사용했는데 출력이 가능한 이유는
# 자체적으로 set을 다른구조로 변환해서 set도 출력이 가능하게 된다.
# 결론 set은 값을 가져올수 없다
print(world_set)

# set으로 중복을 제거하면서 list로 순서를 정렬한다.
# 순서가 없다가 list로 인해서 순서가 생겼기 때문이다.
data = [1, 2, 3, 3, 3, 4, 1, 1, 2]
print(list(set(data)))
