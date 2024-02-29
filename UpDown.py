import random
def restart_game():
    while True:
        restart = input('게임을 재시작하시겠습니까? (y/n)')
        if restart == 'n' or restart =='ㅜ':
            print('게임을 종료합니다.')
            exit()
        elif restart == 'y' or restart =='ㅛ':
            return True
        else:
            print('유효하지 않은 입력입니다. y 또는 n 중에 입력하세요.')

while True:
    com_num = random.randrange(1, 101)
    count = 1

    print('1~100 사이의 숫자 하나를 입력하세요: ')

    while True:
        game = input('')

        try: player = int(game)
        except ValueError:
            print('유효하지 않은 입력입니다. 숫자를 입력하세요.')
            continue

        if player < 1 or player > 100:
            print('1부터 100까지 중의 숫자만 입력 가능합니다: ')
        elif player < com_num:
            print('UP!')
            print('이번엔 맞힐 수 있을까요?: ')
            count += 1
        elif player > com_num:
            print('DOWN!')
            print('이번엔 맞힐 수 있을까요?: ')
            count += 1
        elif player == com_num:
            print('정답입니다! '+str(count)+'회만에 성공했어요!')
            if not restart_game():
                exit()
            break