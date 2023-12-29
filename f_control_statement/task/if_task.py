# 사용자가 입력한 번호의 색상을 영어로 출력한다.
title = "색상은 골라주세요!\n"
menu = "1. 빨간색\n" \
       "2. 검은색\n" \
       "3. 노란색\n" \
       "4. 흰색\n"

choice = int(input(title + menu))
choice1, choice2, choice3, choice4 = choice == 1, choice == 2, choice == 3, choice == 4
color1, color2, color3, color4 = "red", "black", "yellow", "white"
result = None

if choice1:
    result = color1
elif choice2:
    result = color2
elif choice3:
    result = color3
elif choice4:
    result = color4

print(result)