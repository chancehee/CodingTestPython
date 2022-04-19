"""
브루트포스: <보물섬>

1. 아이디어:
    이동이 가능한 모든 좌표(육지)에서 이동을 끝까지 하는 경우의 최단거리를 모두 구하고
    그 중에서 값이 가장 큰 경우 (= 보물은 가장 긴 시간이 걸리는 육지 두 곳)를 리턴 해준다.

    최단 경로 = BFS, 모든 좌표 = 브루트포스

    상, 하, 좌, 우를 탐색 할 때 for문으로 4가지 방향을 탐색하는 경우보다
    미리 다음 동작이 가능한지 판단하는 것이 더 빠르다.
"""

import sys
from collections import deque

input = sys.stdin.readline

# 지도: 행,열
n, m = map(int, input().split())

# 지도: 2차원 배열
graph = [list(input().strip()) for _ in range(n)]

# 정답
answer = 0


# 최단 거리 탐색 함수
def bfs(x, y):
    global answer

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        if x + 1 < n and visited[x + 1][y] == 0 and graph[x + 1][y] == 'L':
            q.append((x + 1, y))
            visited[x + 1][y] = visited[x][y] + 1

        if x - 1 >= 0 and visited[x - 1][y] == 0 and graph[x - 1][y] == 'L':
            q.append((x - 1, y))
            visited[x - 1][y] = visited[x][y] + 1

        if y + 1 < m and visited[x][y + 1] == 0 and graph[x][y + 1] == 'L':
            q.append((x, y + 1))
            visited[x][y + 1] = visited[x][y] + 1

        if y - 1 >= 0 and visited[x][y - 1] == 0 and graph[x][y - 1] == 'L':
            q.append((x, y - 1))
            visited[x][y - 1] = visited[x][y] + 1

    # 탐색을 마친 경우
    # print(visited[x][y])
    answer = max(answer, visited[x][y])


# 브루트포스: 모든 경우 탐색
for i in range(n):
    for j in range(m):
        # 바다인 경우 진행 못함
        if graph[i][j] == 'W':
            continue
        # 방문 여부 체크 배열 생성
        visited = [[0] * m for _ in range(n)]
        # 최단거리 탐색
        bfs(i, j)

# 시작점에서 거리 1을 더해주었으므로 -1을 해준 값 출력
print(answer - 1)
