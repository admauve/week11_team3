import random
def play():
    wins, losses, ties = 0, 0, 0  # 승리, 패배, 비김 횟수 초기화
    while True:
        user = input("가위 = S, 바위 = R, 보 = P (다시 시작 = RE, 종료 = Q): ").upper()
        if user == 'Q':  # 게임 종료
            total_games = wins + losses + ties
            if total_games == 0:
                print("게임을 한 번도 하지 않았습니다.")
            else:
                win_rate = (wins / total_games) * 100
                print(f"\n게임 종료! 총 {total_games}판 중 {wins}승, {losses}패, {ties}무승부")
                print(f"승률: {win_rate:.2f}%")
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
            ties += 1
        elif win(user, computer):
            print("이겼습니다.")
            wins += 1
        else:
            print("졌습니다.")
            losses += 1
def win(player, opponent):
    return (player == 'R' and opponent == 'S') or \
           (player == 'S' and opponent == 'P') or \
           (player == 'P' and opponent == 'R')
# 게임 시작
play()
