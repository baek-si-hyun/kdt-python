# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {'사과': 2000, '배': 1000, '딸기':1700, '자두':500}
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
        new_name, new_price = input(append_message).split()
        if new_name not in data_dict.keys():
            data_dict[new_name] = new_price
        else:
            result_message = append_error_message

    # 수정
    elif menu_option == '2':
        name = input(search_name_message_for_update).strip()
        if name in data_dict.keys():
            new_name, new_price = input(update_message).split()
            data_dict[new_name] = new_price
            continue
        else:
            result_message = update_error_message1

    # 삭제
    elif menu_option == '3':
        name = input(delete_message).strip()
        if name in data_dict:
            del data_dict[name]
        else:
            result_message = delete_error_message


    # 검색
    elif menu_option == '4':
        search_menu_option = input(search_menu + '\n')
        if search_menu_option == '1':
            search_name = input(search_name_message + ' ').strip()
            if search_name in data_dict.keys():
                print(
                    f'{search_name_message} {search_name}, {search_price_message} {data_dict[search_name]}')
            else:
                result_message = search_error_message
        elif search_menu_option == '2':
            check = False
            price = int(input(search_price_message))
            min_price = price * 0.5
            max_price = price * 1.5
            for key, value in data_dict.items():
                if min_price <= int(value) <= max_price:
                    check = True
                    print(f'{search_name_message} {key}, {search_price_message} {value}')
            if check:
                continue
            else:
                result_message = search_error_message


    # 목록
    elif menu_option == '5':
        if len(data_dict) != 0:
            for key, value in data_dict.items():
                print(f'{search_name_message} {key}, {search_price_message} {value}',
                      end='\n')
                continue
        else:
            result_message = no_item_message


    # 나가기
    elif menu_option == '6':
        break

    else:
        result_message = error_message
    print(result_message)
    result_message = ""
