'''
프로그래머스(level2): <프렌즈4블록>
'''
array = [
    "TTTANT",
    "RRFACC",
    "RRRFCC",
    "TRRRAA",
    "TTMMMF",
    "TMMTTJ"
]

def solution(m,n,board):
    answer = 0

    #문자열 -> 리스트
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        #같은 모양의 2X2 블록을 찾으면 remove 배열에 1로 표시
        remove = [[0]*n for _ in range(m)]

        for i in range(5):
            for j in range(5):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    remove[i][j], remove[i][j+1], remove[i+1][j], remove[i+1][j+1] = 1,1,1,1

        # 지워진 블록 개수 세기
        count = 0
        for i in range(6):
            count = count+ sum(remove[i])
        answer = answer + count

            #종료 조건
        if count==0:
            break

        # 지워진 블록을 위의 블록으로 채우기
        for i in range(5, -1, -1): # 5 4 3 2 1 0
            for j in range(6): # 0 1 2 3 4 5
                if remove[i][j] == 1:
                    x = i-1
                    while x >=0 and remove[x][j] == 1:
                        x = x-1
                    if x<0:
                        board[i][j]=0
                    else:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1

    return answer




print(solution(6,6,array))


