# 여러개의 변수를 한줄에 선언
a = 10;
b = 20;
c = 30
print(a, b, c, sep=', ')

a, b, c = 100, 200, 300
print(a, b, c, sep=', ')

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b, sep=', ')

# temp = a
# a = b
# b = temp
# print(a, temp)

a, b = b, a
print(a, b)

# 동적 바인딩
a = 10
print(type(a))

a = 10.5
print(type(a))

a = 'A'
print(type(a))

a = "ABC"
print(type(a))

a = ['A', 'B', 'C']
print(type(a))

a = {'A': 1, 'B': 2, 'C': 3}
print(type(a))

# a = True
a = 5 > 2
print(a)
print(type(a))

# 변수명 직접 바꿔보기
# 아무의미가 없는 값(정수, 실수, 문자열, 리스트, 딕셔러니)임을 표현해보고자 했다.
# 이름이 겹칠거 같으면 스네이크 케이스로 구분해 보았다
number = 10
print(type(number))

float = 10.5
print(type(float))

string_a = 'A'
print(type(string_a))

string_abc = "ABC"
print(type(string_abc))

list = ['A', 'B', 'C']
print(type(list))

dict = {'A': 1, 'B': 2, 'C': 3}
print(type(dict))

boolean = True
print(type(boolean))

# 서식문자
# 5의 경우에는 5의 앞자리가 홀수인 경우에 올림을 하고 짝수인 경우에 버림을 하여 짝수로 만들어준다.
# 예를 들어 53.45는 53.4로 32.75는 32.8로 반올림한다.
# 이를 오사오입(round-to-nearest-even)이라고 한다.

name = '백시현'
age = 20
height = 140.550000

# print('이름: %s' % name)
# print('나이: %d' % age)
# print('키: %.2f' % height)
print('이름: %s\n나이: %d살\n키: %.2fcm' % (name, age, height))

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래에 형식으로 출력하기
# 1 + 3 = 4
sum1 = 1
sum2 = 3
total = sum1 + sum2
ex_formatting = '%d + %d = %d' % (sum1, sum2, total)
print(ex_formatting)

# format 함수
name = '백시현'
age = 20
height = 150.26
print('이름: {}\n나이: {}\n키: {:.1f}'.format(name, age, height))
print("=" * 20)
formatting = "이름: %s\n나이: %d살\n키: %.1fcm" % (name, age, height)
print(formatting)
print("=" * 20)

# 순서정하기
print('이름: {1}\n나이: {0}\n키: {2:.1f}'.format(name, age, height))
print('이름: {name}\n나이: {age}\n키: {height:.1f}'.format(name=name, age=age, height=height))
formatting1 = '이름: {}\n나이: {}\n키: {:.1f}'.format(name, age, height)
formatting2 = '이름: {1}\n나이: {0}\n키: {2:.1f}'.format(name, age, height)
formatting3 = '이름: {name}\n나이: {age}\n키: {height:.1f}'.format(name=name, age=age, height=height)
print(formatting1)
print(formatting2)
print(formatting3)

# 실습
# 아래 메세지를 format함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !

python_kor, python_eng = '파이썬', 'Python'
django_kor, django_eng = '장고', 'Django'
react_kor, react_eng = '리액트', 'React'

# 자동으로 해당 순서에 값이 반영된다.
python_formatting = 'Hello {}, {} is fantastic !'.format(python_kor, python_eng)

# 값에 할당된 번호를 작성하면 해당 값이 반영된다.
django_formatting = 'Hello {0}, {1} is fantastic !'.format(django_kor, django_eng)

# 값에 이름을 붙이면 해당 이름에 있는 값이 반영된다.
react_formatting = 'Hello {kor}, {eng} is fantastic !'.format(kor=react_kor, eng=react_eng)

print(python_formatting, django_formatting, react_formatting, sep='\n')

# format stirng
name = '백시현'
age = 50
height = 180.26

# round(실수값, 반올림 자리 수)
print(f'이름: {name}, 나이: {age}살,  키: {height:.1f}cm')
print(f'이름: {name}, 나이: {age}살,  키: {round(height, 1)}cm')

# 실습
# 아래 메세지를 format stirng을 사용하여 출력한다
# Hello 파이썬, Python is fantastic
# Hello 장고, Django is fantastic
# Hello 리액트, React is fantastic
print(f'Hello {python_kor}, {python_eng} is fantastic')
print(f'Hello {django_kor}, {django_eng} is fantastic')
print(f'Hello {react_kor}, {react_eng} is fantastic')
