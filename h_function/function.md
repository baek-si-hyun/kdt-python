## 함수 - 이름 뒤에 소괄호, 작성돈 코드의 주소값을 담고 있는 주소공간
    f       (x)     =       2x+1
    함수명   매개변수          리턴 값

### 함수 선언
    def 함수명(매개변수, ...):
        실행할 문장
        return 리턴값

### 함수 사용
    함수명(값1, ...)

### 함수를 사용하는 목적
    1. 재사용
        절대 특정성을 부여하면 안된다
    2. 간결화

### 함수 선언 순서
    문제) 두 정수의 덧셈을 해주는 함수 구현
    
    1. 함수명을 생각한다
        def add():

    2. 매개변수를 생각한다
        def add(number1, number2):

    3. 실행할 문장을 생각한다.
        def add(number1, number2):
            result = number1 + number2
    
    4. 리턴 값을 생각한다
        def add(number1, number2):
            result = number1 + number2
            return result

### 매개변수 선언 방법
    - packing(args)
        여러개의 값을 마구잡이로 받을 때 사용한다
    - kwargs
        여러개의 값을 key=value 형식으로 받는다
    - unpacking
        매개변수에 *로 시작하면 kwargs 형식과 동일하게 받아야 하고,
        그냥 매개변수가 나열어 있으면, 값만 전달해도 된다

### packing(agrs) 함수 사용 방법
    - 여러개의 값을 ,로 구분하여전달
    - 여러개의 값을 묶은 뒤, 앞에 *을 작성하여 전달

### kwrags 함수 사용 방법
    - 여러개의 값을 ,로 구분하여 key=value 형태로 전달
    - dict에 정보를 담은 뒤 **을 앞에 붙여서 전달