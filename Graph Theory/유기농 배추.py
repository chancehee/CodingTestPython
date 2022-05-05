"""
그래프이론: <유기농 배추>

1. 아이디어:
    방문 하지 않은 노드를 방문하여 이어져있는 덩어리가 몇개인지 탐색한다.
    dfs로 풀이 예정
    python으로 백준 저지에 제출 할 때 setrecursionlimit를 설정해주어야지 런타임에러를 막을 수 있다.
    기본 재귀 깊이가 1000으로 설정되어있기 때문에 늘려줘야한다.
"""


import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue

        if visited[nx][ny]:
            continue

        if arr[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)

    return True


for _ in range(T):
    N, M, K = map(int, input().strip().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().strip().split())
        arr[x][y] = 1

    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 1:
                if dfs(i, j):
                    cnt += 1
    print(cnt)