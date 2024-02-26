import random

com_num = random.randrange(1,101)
print(com_num)

game = int(input('1~100 사이의 숫자를 입력하세요: '))
game != com_num
while True:
    if game < 1 or game > 100:
        print('입력할 수 있는 숫자는 1부터 100까지 사이의 숫자입니다.'),
        print(int(input('다시 입력하세요: ')))
    elif game > com_num:
        print('DOWN!'),
        print(int(input('이번엔 맞힐 수 있을까요?: ')))
    elif game < com_num:
        print('UP!'),
        print(int(input('이번엔 맞힐 수 있을까요?: ')))
    else:
        print('맞혔습니다!')
        break