"""
프로그래머스: <게임 맵 최단거리>

1. 아이디어:
    최단거리를 구하기 위한 방법으로 bfs를 떠올렸다.
    길이 없을 경우 (목적지 값이 업데이트 안되어 1인경우) -1 출력
    maps: 미로 지도 정보
    1: 길
    0: 벽
"""
from collections import deque

maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

# 상 하 좌 우 (방향 벡터)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = len(maps)
m = len(maps[0])


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 미로 범위에 존재하지 않을 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 이동해야할 곳이 벽인 경우(갈 수 없는 경우)
            if maps[nx][ny] == 0:
                continue

            # 이동이 가능하고, 처음 방문하는 경우( 값이 1인 경우)
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx, ny])


# 길 탐색 0,0 좌표부터 시작
bfs(0, 0)
# 목적지에 도달하지 못한 경우 -1 출력
if maps[n - 1][m - 1] ==  1:
    print(-1)
# 목적지에 도달한 경우, 최단거리 값 출력
else:
    print(maps[n - 1][m - 1])
