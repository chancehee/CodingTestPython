'''
구현: <윷놀이>
'''

for i in range(3):
    game = list(map(int, input().split()))

    if game.count(1) == 4:
        print('E')
    elif game.count(1) == 0:
        print('D')
    elif game.count(0) == 1:
        print('A')
    elif game.count(0) == 2:
        print('B')
    elif game.count(0) == 3:
        print('C')

