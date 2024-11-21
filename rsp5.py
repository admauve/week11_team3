import random

def 가위바위보():
    while True:
        user = input("가위(S), 바위(R), 보(P) 중 하나를 선택하세요: ").upper()
        if user not in ['R', 'S', 'P']:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue

        computer = random.choice(['R', 'S', 'P'])
        print(f"사용자: {user}, 컴퓨터: {computer}")

        if user == computer:
            print("비겼습니다. 다시 가위바위보를 합니다.")
            continue  # 비긴 경우, 다시 가위바위보
        elif win(user, computer):
            print("사용자가 가위바위보에서 이겼습니다. 공격자가 됩니다!")
            return "user"
        else:
            print("컴퓨터가 가위바위보에서 이겼습니다. 공격자가 됩니다!")
            return "computer"

def 묵찌빠(attacker):
    while True:
        user = input("가위(S), 바위(R), 보(P) 중 하나를 선택하세요: ").upper()
        if user not in ['R', 'S', 'P']:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue

        computer = random.choice(['R', 'S', 'P'])
        print(f"사용자: {user}, 컴퓨터: {computer}")

        if user == computer:
            if attacker == "user":
                print("사용자가 묵찌빠에서 승리했습니다!")
            else:
                print("컴퓨터가 묵찌빠에서 승리했습니다!")
            break  # 공격자가 승리했으므로 게임 종료
        else:
            # 공격자 교체
            if win(user, computer):
                print("사용자가 이번 라운드에서 이겼습니다. 공격자가 됩니다!")
                attacker = "user"
            else:
                print("컴퓨터가 이번 라운드에서 이겼습니다. 공격자가 됩니다!")
                attacker = "computer"

def win(player, opponent):
    return (
        (player == 'R' and opponent == 'S') or
        (player == 'S' and opponent == 'P') or
        (player == 'P' and opponent == 'R')
    )

def 묵찌빠_게임():
    print("묵찌빠 게임을 시작합니다!")
    attacker = 가위바위보()  # 가위바위보 결과로 공격자 결정
    if attacker:
        묵찌빠(attacker)

# 게임 실행
묵찌빠_게임()
