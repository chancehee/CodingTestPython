"""
브루트포스: <테트로미노>

1.아이디어:
    하나의 지점을 기준으로 동서남북 방향으로 dfs를 해준다 (깊이 : 3)
    (방문 처리를 통해서 중복x)
    ㅗ,ㅜ,ㅏ,ㅓ 이러한 모양은 깊이가 1일때 처리해준다.
    가지치기: 선택한 값을 빼고 남은 값의 합이 최대값으로 구성되었을 경우가 기존에
    저장되어있는 최댓값보다 작다면 탈출(return)

"""

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
MAX_VALUE = max(map(max, arr))
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0


def dfs(x, y, cnt, total):
    global ans

    # 가지치기
    if total + (3 - cnt) * MAX_VALUE <= ans:
        return

    if cnt == 3:
        ans = max(ans, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if not visited[nx][ny]:
            if cnt == 1:
                visited[nx][ny] = True
                dfs(x, y, cnt + 1, total + arr[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, total + arr[nx][ny])
            visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = False

print(ans)
