"""
브루트포스: <N-Queen>

1. 아이디어:
    각 행에는 퀸이 한개만 올 수 있고, 퀸이 한개가 놓인 경우에 아래 행에 퀸을
    놓을 수 있는 경우에 DFS로 깊이 우선 탐색한다.
    놓을 수 없는 경우(같은 행, 열, 대각선에 위치하는 경우 X),
    BT기법을 통해 뒤로 돌아가서 다른 모든 경우를 탐색한다.
    만약 최대 깊이에 들어간 경우 퀸을 놓을 수 있는 경우로 간주, 반대의 경우 놓을 수 없는 경우로 간주

2. 시간복잡도:

3. 변수명:

"""

# 로직에 따라서 시간 복잡도의 차이가 많이 나므로 주의, 보드판을 1차원 배열로 표현하고, 유망한지 검사하는 로직이 중요하다.
# 백준 저지에서 python3로 제출시 시간초과, pypy3로 제출시에 통과함.

n = int(input())
# 인덱스가 행, 값이 열
col = [0] * (n+1)
result = 0


# 퀸을 놓는 함수
def n_queen(cnt, col):

    global result

    # 퀸을 보드에 다 놓은 경우
    if cnt == n:
        # print(col)
        result += 1
        return
    else:
        for j in range(1, n + 1):
            # 열에 대한 정보 1~n을 col 배열에 넣어주기
            col[cnt + 1] = j
            # 퀸 놓을 수 있는지 검사
            if promising(cnt+1, col):
                n_queen(cnt + 1, col)


# 유망한가 판단하는 함수
def promising(cnt, col):
    for j in range(1, cnt):
        if col[cnt] == col[j]:
            return False
        elif abs(col[cnt] - col[j]) == cnt - j:
            return False
    return True


n_queen(0, col)
print(result)
