#

# mutable - 변할수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1)

# immutable - 변할수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
# data_tuple2[0] = 10 # tuple은 변경이 불가능하다
data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)
print(data_tuple1)

datas = 1, 2
print(type(datas))
print(datas[0])

# 변수명이 전부 대문자이면 상수라고 의심해 봐야 한다
ERROR_CODE = 1,
print(type(ERROR_CODE))

