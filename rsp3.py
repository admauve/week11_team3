import random

def play():
    while True:
        user = input("가위 = S, 바위 = R, 보 = P (다시 시작 = RE, 종료 = Q): ").upper()
        if user == 'Q':  # 게임 종료
            print("게임을 종료합니다.")
            break
        elif user == 'RE':  # 게임 다시 시작
            print("게임을 다시 시작합니다!")
            continue
        elif user not in ['S', 'R', 'P']:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

        computer = random.choice(['R', 'S', 'P'])
        print(f"컴퓨터의 선택: {computer}")
        
        if user == computer:
            print("비겼습니다.")
        elif win(user, computer):
            print("이겼습니다.")
        else:
            print("졌습니다.")

def win(player, opponent):
    return (player == 'R' and opponent == 'S') or \
           (player == 'S' and opponent == 'P') or \
           (player == 'P' and opponent == 'R')

# 게임 시작
play()
