"""
브루트 포스: <연구소>

1. 아이디어:
    벽 3개를 세운 후
    2가 있는 모든 경우에서 바이러스 퍼뜨리기
    0의 개수 출력
"""
import copy

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

z = []
t = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            z.append([i,j])
        elif arr[i][j] == 2:
            t.append([i,j])

visited = [False] * len(z)
result = 0


def zero_dfs(cnt):
    global result
    answer = 0
    if cnt==3:
        w = copy.deepcopy(arr)
        for two in t:
            x, y = two
            solve(w, x, y)
        for a in w:
            answer += a.count(0)
        result = max(result, answer)
        return

    for i in range(len(z)):
        if not visited[i]:
            visited[i] = True
            arr[z[i][0]][z[i][1]] = 1
            zero_dfs(cnt + 1)
            visited[i] = False
            arr[z[i][0]][z[i][1]] = 0


dx = [0,0,1,-1]
dy = [-1,1,0,0]


def solve(w, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if w[nx][ny] == 0:
                w[nx][ny] = 2

                solve(w, nx, ny)


zero_dfs(0)
print(result)