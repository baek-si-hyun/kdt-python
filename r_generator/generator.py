# import os
# import psutil
#
# process_object = psutil.Process(os.getpid())
# memory_before = process_object.memory_info().rss / 1024 / 1024
#
# data_list = [i ** 2 for i in range(10000)]
# print(data_list)
#
# memory_after = process_object.memory_info().rss / 1024 / 1024
# print(f'memory: {memory_before} -> {memory_after}')
#
# #######################################################################
#
# memory_before = process_object.memory_info().rss / 1024 / 1024
#
# data_generator = (i ** 2 for i in range(10000))
# print(next(data_generator))
#
# memory_after = process_object.memory_info().rss / 1024 / 1024
# print(f'memory: {memory_before} -> {memory_after}')


def increase(number: int = 0):
    while True:
        number += 1
        yield number

# 제너레이터는 한번에 값을 가져오지 않고 하나씩 필요할 때 마다 가져온다
# 메모리 효율이 좋다
# 예시로는 콘솔창에서 전에 입력했던 명령어를 방향키로 하나씩 가져오는게 있다
result = increase()
while True:
    data = input("Y/n >> ")
    if data == "Y":
        print(next(result))
    else:
        break
