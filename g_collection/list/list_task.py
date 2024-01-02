# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    menu_option = input(title + '\n' + menu)

    # 추가
    if menu_option == '1':
        # 사용자에게 과일명과 과일 가격을 입력받고 실수로 입력할수 있는 앞뒤 공백을 제거한다
        new_name, new_price = input(append_message).split()
        # 사용자가 입력한 데이터가 기존 데이터에 있는지 중복 검사를 한다
        if new_name not in name_list:
            # 중복 검사에 통과 했으면 list에 추가한다
            name_list.append(new_name)
            price_list.append(int(new_price))
        # 중복되면 에러 메세지를 출력한다
        else:
            result_message = append_error_message

    # 수정
    elif menu_option == '2':
        # 수정할 과일명을 사용자에게 입력받는다
        name = input(search_name_message_for_update).strip()
        # 사용자가 입력한 과일명이 데이터에 존재하는지 확인한다
        if name in name_list:
            # 사용자가 '상품명 가격' 형태로 입력할 것이기 때문에 공백을 기준으로 둘로 나눈다
            new_name, new_price = input(update_message).split()
            # 기존 데이터에 수정한 값이 존재하는지 중복검사를 한다
            if new_name not in name_list:
                # 입력받은 데이터의 index를 찾는다
                # 기존에 데이터를 수정하기 위해서는 기존 데이터릐 index를 알아야 한다.
                find_index = name_list.index(name)
                # 찾았으면 해당 index에 있는 데이터를 수정한다
                name_list[find_index], price_list[find_index] = new_name, new_price
            # 중복되면 에러 메세지를 출력한다
            else:
                result_message = update_error_message2
        else:
            result_message = update_error_message1

    # 삭제
    elif menu_option == '3':
        # 사용자에게 삭제할 과일명을 입력 받는다
        name = input(delete_message).strip()
        # 입력받은 데이터가 기존 데이터에 존재하는지 확인한다.
        if name in name_list:
            # 존재하면 해당 데이터의 index를 찾아 삭제한다.
            find_index = name_list.index(name)
            # name_list의 find_index번째에 있는 요소를 삭제한다
            del name_list[find_index]
            del price_list[find_index]

        else:
            result_message = delete_error_message


    # 검색
    elif menu_option == '4':
        # 사용자에게 이름으로 검색할건지 가격으로 물어볼건지 물어본다
        search_menu_option = input(search_menu + '\n')
        # 이름으로 검색할 경우
        if search_menu_option == '1':
            # 검색할 이름을 사용자에게 입력 받는다
            search_name = input(search_name_message + ' ').strip()
            # 기존 데이터에 사용자가 입력한 이름이 있는지 확인한다
            if search_name in name_list:
                # 있다면 해당 데이터의 index를 찾아 출력한다
                find_index = name_list.index(search_name)
                print(
                    f'{search_name_message} {name_list[find_index]}, {search_price_message} {price_list[find_index]}')
            # 사용자가 입력한 이름이 기존 데이터에 없다면 에러를 출력한다
            else:
                result_message = search_error_message
        # 가격으로 검색 할 경우
        elif search_menu_option == '2':
            # 오차범위를 계산 하기위해 int로 형변환한다
            price = int(input(search_price_message))
            min_price = price * 0.5
            max_price = price * 1.5
            # Comprehension을 사용해 검색 결과가 존재하는지 찾아본다
            # for price in price_list으로 반복문을 돌면서 min_price <= price <= max_price조건에 맞는 데이터가 있는지 찾는다
            # 찾았다면 for 앞에 있는 price에 list형태로 저장된다
            # 저장된 list 데이터로 다시 for문을 수행하면서  price_list.index(i)통해 list들의 데이터를 result_index에 list형태로 저장한다.
            result_index = [price_list.index(i) for i in
                            [price for price in price_list if min_price <= price <= max_price]]
            # result_index의 데이터릐 길이가 0이 아니면 검색 조건에 만족한 데이터가 있다는 뜻이다
            if len(result_index) != 0:
                # 검색 결과에 만족한 데이터들을 반복문을 활용해 하나씩 출력한다
                for i in result_index:
                    print(f'{search_name_message} {name_list[i]}, {search_price_message} {price_list[i]}')
            # 데이터의 길이가 0이라면 검색 결과가 없는 것이므로 에러메세지를 출력한다
            else:
                result_message = search_error_message


    # 목록
    elif menu_option == '5':
        # 기존 데이터의 길이가 0이 아닌경우엔 데이터들이 존재한다는 의미로 목록을 출력할수 있다
        if len(name_list) != 0:
            # name_list의 길이만큼 반복문을 돌면서 차례로 값을 출력한다
            for i in range(len(name_list)):
                print(f'{search_name_message} {name_list[i]}, {search_price_message} {price_list[i]}',
                      end='\n')
                # 반복문이 끝났다면 continue를 사용해 해당위치의 아래에 있는 코드들을 건너뛴다
                continue
        # 기존 데이터의 길이가 0 이라면 데이터가 존재하지 않는다는 뜻이므로 에러를 출력한다
        else:
            result_message = no_item_message


    # 나가기
    elif menu_option == '6':
        # 사용자가 while문을 끝내려고 한다면 break를 사용해 반복문을 즉시 종료한다
        break



    else:
        result_message = error_message
    # 에러코드는 에러가 생길때마다 print함수를 사용하기 보다는 변수에 해당 오류들을 저장해 놓고
    # 일괄처리해 코드의 가독성을 높인다
    print(result_message)
    # 에러코드를 출력했다면 초기화 하여 생긴 오류와 다른오류가 result_message에 저장되지 않도록 한다
    result_message = ""

