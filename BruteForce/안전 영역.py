'''
브루트포스: <안전 영역>
1. 아이디어
    최대 높이를 구한 후, 반복문을 통해 높이에 따른 물에 잠기지 않는 지역 구하기
    물에 잠기지 않는 지역은 dfs함수를 통해 True를 반환한다. (연결된 부분)
    방문 처리 테이블을 사용하여 방문체크해준다.

2. 시간 복잡도
    for문 3번

3. 변수
    graph : 지도 정보를 담고 있는 2차원 배열
    rain : 강수량
    N : 지도의 가로 세로 길이
    visited : 방문 여부 2차원 배열
'''

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

max_values = []
for g in graph:
    max_values.append(max(g))
max_value = max(max_values)


# 연결된 지점을 탐색하여 True로 반환하는 dfs 함수
def dfs(x, y, h):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    if graph[x][y] > h and not visited[x][y]:
        visited[x][y] = True
        dfs(x - 1, y, h)
        dfs(x + 1, y, h)
        dfs(x, y - 1, h)
        dfs(x, y + 1, h)
        return True
    return False


result = []
# 높이에 따른 모든 경우를 살펴본다.
for height in range(max_value):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > height:
                if dfs(i, j, height):
                    cnt += 1
    result.append(cnt)

# 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수 출력
print(max(result))


















