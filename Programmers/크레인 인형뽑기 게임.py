'''
프로그래머스(level1): <크레인 인형뽑기 게임>

'''
# 단순한 아이디어지만 구현부분에서 어려움을 느끼고 시간이 오래걸렸다..
# 배열을 능숙하게 다루는 기술이 필요하다고 느꼈다
board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]
moves = [1,5,3,5,1,2,1,4]

cnt = 0

b=[]

for move in moves:
    for i in range(len(board)):
        if board[i][move-1] == 0:
            continue

        b.append(board[i][move-1])
        board[i][move - 1]=0

        if len(b)>=2:
            if b[-1]==b[-2]:
                cnt=cnt+2
                del b[-2:]
        break
print(cnt)









