import random
import time
from threading import Thread
import signal
import os

def main():
    d=0
    v=0
    l=0
    global got_input, com
    got_input = False

    def restart_game():
        global d, v, l
        while True:
            restart = input('한 판 더? (y/n)')
            if restart == 'n' or restart =='ㅜ':
                print('게임을 종료합니다.')
                print(v,'승 ', d,'무 ',l,'패',)
                exit()
            elif restart == 'y' or restart =='ㅛ':
                return True
            else:
                print('유효하지 않은 입력입니다. y 또는 n 중에 입력하세요.')

    while True:
        com_pae = ['바위', '가위', '보']
        com = random.choice(com_pae)

        def countdown(duration):
            global got_input
            for _ in range(duration):
                time.sleep(1)
                if got_input:
                    return
            if not got_input:
                os.kill(os.getpid(), signal.SIGINT)

        (t := Thread(target=countdown, args=[5])).start()
        try:
            player = input('안 내면 진 거 가위, 바위, 보!')
            got_input = True
        except KeyboardInterrupt:
            print('\n시간초과 패!')
            l += 1
        finally:
            t.join()
        if player == com:
            print(com)
            print('무승부!')
            d += 1
            if not restart_game():
                exit()
            break
        elif (player =='바위'and com == '가위') or (player == '가위' and com == '보') or (player == '보' and com == '바위'):
            print(com)
            print('승!')
            v += 1
        else:
            print(com)
            print('패!')
            l += 1
        if not restart_game():
            exit()
        else:
            break

if __name__ == '__main__':
    main()