# 정렬
number_list = [5, 4, 6, 1, 3]
# 1. sort()
# 원본을 직접 수정한다.
# number_list.sort(reverse=True)
# print(number_list)

# 2. sorted()
# 원본을 유지하고 새로운 list가 만들어 진다 (불변성)
sorted_list = sorted(number_list, reverse=True)
print(number_list)
print(sorted_list)
