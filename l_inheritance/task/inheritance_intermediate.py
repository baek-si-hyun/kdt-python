# [종합 실습]
# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막
#
# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호
# 중복검사 서비스가 있다.
#
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기
# (새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.

# 매개변수 앞에 *을 쓰게 되면 매개젼수들을 키값으로 사용할 수 있다
def check(*, key: str, value: str) -> dict:
    # 클래스 내의 정적변수에 접근 할때는 클래스명.변수명 을 사용해야 한다
    # banks 리스트의 요소를 순회하면서 check_account_number, check_phone 메서드에서 전달하는 값으로
    # 중복을 검사한다
    for bank in Bank.banks:
        for user in bank:
            # value는 사용자가 입력한 값이다
            # 기존데이터에 사용자가 입력한 데이터가 존재하면 해당 데이터를 반환한다

            if user[key] == value:
                # ex) if user['account_number'] == '11012302133'}:
                #     if문이 Ture이면
                #     return {'account_number': '11012302133'}
                return user
    # 아무것도 찾지 못하면 None을 반환한다
    # None도 값으로 볼 수 있다(boolean)
    return None


class Bank:
    total_count = 3
    # Comprehension을 사용해 2차원 배열을 생성한다
    banks = [[] for i in range(total_count)]

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # self는 해당 필드의 주소값을 가지고 있다
        # 필드의 주소를 object라는 필드에 저장함으로 언제든지 해당 필드에 접근할 수 있다
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    # 클래스 메서드가 실행되기전에 생성자를 먼저 실행한다
    # 클래스 메서드는 생성자가 받는 매개변수를 무조건 포함해서 받아야한다
    # 생성자가 필요로 하는 값들은 kwargs로 별도로 필요한 값은 따로 받는다
    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        # [ShinHan, KookMin, KaKao]라는 list에서 사용자가 입력한 bank_choice에 1을 빼면
        # 해당 list의 인덱스 번호이다 ex) data_list[1]
        # data_list[1]는 KookMin임으로 뒤에 ()를 붙이면 생성자가 된다
        # KookMin()에 해당 생성자가 필요로하는 값들을 전달한다 ex) KookMin(**kwargs)
        bank = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # cls는 Bank 클래스 그 자체이다
        # cls를 Bank와 같다고 봐도 된다
        # ex) Bank.banks[1].append(bank.__dict__)
        # __dict__ 매직 메서드는 해당값을 dict로 만들어준다
        cls.banks[bank_choice - 1].append(bank.__dict__)
        # bank를 반환한 이유는 사용자가 추가되면 bank데이터를 보기 위함이다
        return bank

    # static method이기 때문에 클래스 호출과 동시에 메모리에 올라간다
    # self를 사용하지 않음으로 클래스의 다른 필드들과 개별적으로 실행할 수 있다
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        # check함수에게 {'account_number':account_number} 형식으로 값을 전달한다
        return check(key='account_number', value=account_number)

    @staticmethod
    def check_phone(phone: str) -> dict:
        return check(key='phone', value=phone)

    # 추상화를 한다
    # 자식클래스들에서 구체화하고 부모클래스에서는 공통으로 사용될 코드들을 구현한다
    def deposit(self, money: int):
        # money를 전달 받아 deposit 메서드가 실행되면 필드에 있는 money에
        # 전달 받은 money를 더해준다
        self.money += money

    def withdraw(self, money: int):
        # money를 전달 받아 withdraw 메서드가 실행되면 필드에 있는 money에
        # 전달 받은 money를 빼준다
        self.money -= money

    def balance(self):
        return self.money

    # __str__는 해당 객체를 문자열로 표현하고자 할때 사용된다
    # 원래는 __repr__이 생략되어 있지만
    # __str__를 재정의 하는 순간 __repr__대신 __str__로 대체된다
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):
    def deposit(self, money: int):
        # 해당 값을 나눈 몫을 money에 저장한다
        money //= 2
        # super()를 사용했으므로 부모 클래스의 deposit 메서드를 호출할수 있다
        # 오버라이드하고 super를 사용할 경우
        # 부모메서드의 기능에서 더 추가로 기능을 구현할 때 사용한다
        super().deposit(money)


class KookMin(Bank):
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))


class KaKao(Bank):
    def balance(self):
        self.money //= 2
        return super().balance()


if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))
            if menu_choice == 5:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)
                # 사용자가 기존 데이터와 중복되지 않은 값을 입력할때까지 반복한다
                while True:
                    account_number = input(account_number_message)
                    # 사용자가 입력한 데이터를 Bank클래스에 있는 check_account_number 메서드에 전달한다
                    if Bank.check_account_number(account_number) is None:
                        # 중복이 없다면 Bank.check_account_number(account_number)는 None일것이고
                        # while문을 break을 사용해 멈춘다
                        break

                while True:
                    phone = input(phone_message)
                    # 위에 account_number 검사하는 것과 같은 원리
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)
                    # 비밀번호가 4자리수인지 확인한다
                    # 4자리수이면 반복문을 중단한다
                    if len(password) == 4:
                        break
                # 사용자에게 예치금을 입력받는다
                money = int(input(money_message))
                # 사용자에게 입력받은 값들을 Bank의 open_account메서드를 통해 전달한다
                # open_account는 클래스메서드이기 때문에 실행되기전에 생성자를 실행한다 (__init__)
                # bank_choice (선택한 은행)의 값도 같이 전달해준다
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone,
                                         password=password, money=money)
                print(user)

            # 입금
            # 개설한 은행에서만 입금 가능
            elif menu_choice == 2:
                account_number = input(account_number_message)
                # 중복 검사
                user = Bank.check_account_number(account_number)
                if user is not None:
                    # 사용자에게 password를 입력받는다
                    # 입력 받는 값이 user['password']와 동일한지 확인한다
                    if user['password'] == input(password_message):
                        # 사용자에게 입금할 금액을 입력 받는다
                        deposit_money = int(input(deposit_message))
                        # user['object']는 객체 자기 자신을 담고있다
                        # 해당 객체에 deposit 메서드에 deposit_money을 전달한다
                        user['object'].deposit(deposit_money)
                        # 입금 까지 완료했으면 나머지 모든 코드들을 건너뛰고
                        # 다시 while문 처음으로 돌아간다
                        continue

                else:
                    print(error_message)

            # 출금
            elif menu_choice == 3:
                # 중복 검사
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    # password 맞나 확인
                    if user['password'] == input(password_message):
                        # 출금할 돈 입력 받기
                        withdraw_money = int(input(withdraw_message))
                        # ininstance는 첫번쨰로 받은 객체가 두번째로 받은 클래스의 객체인지 확인하는 메서드이다
                        # ex) 10000 * (1.5 if True else 1) <= 30000
                        # if문이 True이면 1.5를 곱하고 아니면 1을 곱한다
                        # 그리고 사용자가 출금할 금액과 곱한 금액이 기존에 있는 금액보다 작거나 같은지 확인한다
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            # if문이 True이면 해당 객체에 사용자가 입력한 withdraw_money을 전달한다
                            # user['object']는 해당 필드의 주소값을 가지고 있다
                            # 해당 필드에 있는 withdraw를 호출해 withdraw_money를 전달한다
                            user['object'].withdraw(withdraw_money)
                            continue
                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                # 중복 검사
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        # 해당 필드의 주소로 필드에 접근해 balance메서드를 호출한다
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                pass

            else:
                print(error_message)
