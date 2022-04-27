"""
그래프 이론: <단지번호붙이기>

1. 아이디어:
    그래프에서 1인 경우(방문 안한 경우) 탐색 시작
    탐색 안에서 dfs를 통해서 연결된 모든 단지 카운트 세기, 덩어리 카운트 세기

"""
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))

visited = [[False] * N for _ in range(N)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if arr[nx][ny] == 0:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = True
            cnt += 1
            dfs(nx, ny)

    return

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i,j)
            if cnt == 0:
                result.append(1)
            else:
                result.append(cnt)

print(len(result))
result.sort()
for r in result:
    print(r)


