"""
구현: <로봇 청소기>

1. 아이디어:
    주어진 조건대로 구현하기
    조건
        1. 현재 위치 청소
        2. if:
            왼쪽에 청소X, 빈공간O -> 왼쪽으로 회전, 전진후 1번 조건으로 돌아간다.
           else:
            왼쪽 방향으로 회전 -> 1번으로 돌아간다.
        if 회전 count == 4:
            if 뒤 == 벽:
                return -1
            else:
                한 칸 후진

    dfs를 통하여 구한다.
"""
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N, M = map(int, input().strip().split())
x, y, v = map(int, input().strip().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().strip().split())))

visited = [[False] * (M) for _ in range(N)]
# v: 0 북 / 1 동 / 2 남 / 3 서

# 북 동 남 서
dx = [1,0,-1,0]
dy = [0,-1,0,1]

# 서, 북, 동, 남
tx = [0, -1, 0, 1]
ty = [-1, 0, 1, 0]
answer = 0
def dfs(x, y, v, cnt):
    global answer
    # 종료 조건: 4바퀴 회전한 경우
    if cnt == 4:
        # 현재 위치에서 후진 하기
        nx = x + dx[v]
        ny = y + dy[v]
        if (0<=nx<N and 0<=ny<M) and arr[nx][ny] != 1:
            dfs(nx, ny, v, 0)
        else:
            return
    else:
        nx = x + tx[v]
        ny = y + ty[v]

        # 범위를 벗어나는 경우 or 벽인 경우
        if (nx<0 or ny<0 or nx>=N or ny>=M) or arr[nx][ny] == 1 or visited[nx][ny] == True:
            v = v - 1
            if v == -1:
                v = 3
            dfs(x, y, v, cnt+1)
            return

        # 정상적으로 이동이 가능한 경우
        visited[nx][ny] = True
        answer += 1
        v = v - 1
        if v == -1:
            v = 3
        dfs(nx, ny, v, 0)
    return


if (x<0 or x>=N or y<0 or y>=M) or arr[x][y] == 1:
    print(0)
else:
    visited[x][y] = True
    dfs(x, y, v, 0)

print(answer+1)











