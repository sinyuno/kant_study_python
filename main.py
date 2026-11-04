# 가위 바위 보 게임 미니 프로젝트

import random


# 승 패 횟수
win_count = 0
lose_count = 0

# 타이틀
print("=" * 30)
print("가위 / 바위 / 보 / 게임")
print("=" * 30)

while True:
    # 1 ~ 3 난수 발생
    number = random.randint(1, 3)
    
    print("1. 가위 / 2. 바위 / 3. 보")
    user_input = input("번호를 선택하세요. : ")

    if number == 1: number = "가위"
    elif number == 2: number = "바위"
    elif number == 3 : number = "보"
    
    # 플레이어가 문자를 입력 했을 때
    if not user_input.isdecimal():
        print("숫자만 입력해주세요.")
        continue

    user_input = int(user_input)

    # 플레이어의 숫자가 요구 값보다 크거나 작을 때
    if user_input > 3 or user_input < 1:
        print("1~3 사이의 숫자만 입력해주세요.")
        continue


    if user_input == 1: user_input = "가위"
    elif user_input == 2: user_input = "바위"
    elif user_input == 3: user_input = "보"

    # 게임 결과 표시
    print("[게임 결과]")
    print(f"나: {user_input}   VS   컴퓨터: {number}")



    # 컴퓨터가 가위를 냈을 때
    if number == "가위" and user_input == "가위":
        print("비겼습니다.")
    
    elif number == "가위" and user_input == "바위":
        print("플레이어 승!")
        win_count += 1
    
    elif number == "가위" and user_input == "보":
        print("컴퓨터 승!")
        lose_count += 1
    

    # 컴퓨터가 바위를 냈을 때
    if number == "바위" and user_input == "바위":
        print("비겼습니다.")
    
    elif number == "바위" and user_input == "보":
        print("플레이어 승!")
        win_count += 1
    
    elif number == "바위" and user_input == "가위":
        print("컴퓨터 승!")
        lose_count += 1
    

    # 컴퓨터가 보를 냈을 때
    if number == "보" and user_input == "보":
        print("비겼습니다.")
    
    elif number == "보" and user_input == "가위":
        print("플레이어 승!")
        win_count += 1
    
    elif number == "보" and user_input == "바위":
        print("컴퓨터 승!")
        lose_count += 1
    
    # 현재 스코어 표시
    print(f"현재 스코어 나 {win_count} : {lose_count} 컴퓨터")


    # 승리 카운트 누적으로 승 패 결정하기
    if win_count == 2:
        print("플레이어가 최종 승리하였습니다.")
        while True:
            user_continue = input("다시 도전 하시겠습니까? (Y/N) :")
            if user_continue == "y" or user_continue == "Y":
                win_count = 0
                lose_count = 0
                break
            elif user_continue == "n" or user_continue == "N":
                break
            else:
                print("Y/N 만 입력해 주세요.")
                continue
        if user_continue == "y" or user_continue == "Y":
            continue
        elif user_continue == "n" or user_continue == "N":
            print("게임을 종료합니다.")
            break

    elif lose_count == 2:
        print("컴퓨터가 최종 승리하였습니다.")
        while True:
            user_continue = input("다시 도전 하시겠습니까? (Y/N) :")
            if user_continue == "y" or user_continue == "Y":
                 win_count = 0
                 lose_count = 0
                 break
            elif user_continue == "n" or user_continue == "N":
                break
            else:
                print("Y/N 만 입력해 주세요.")
                continue
        if user_continue == "y" or user_continue == "Y":
            continue
        elif user_continue == "n" or user_continue == "N":
            print("게임을 종료합니다.")
            break