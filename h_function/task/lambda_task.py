# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
list_data = ['aPPle', 'BananA', 'meLON']
print(list(map(lambda item: item.lower(), list_data)))

# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
hangul = '공일이삼사오육칠팔구'
data = '삼오일구'
print(int(''.join(map(lambda s: str(hangul.index(s)), list(data)))))

# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
hangul = "공일이삼사오육칠팔구"
data = 3519
print(''.join(list(map(lambda s: hangul[int(s)], str(data)))))

# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
data = list(filter(lambda url: 'user' not in url, map(lambda url: url.split('/')[0], urls)))
print(data)
