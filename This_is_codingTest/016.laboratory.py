"""
이코테
DFS/BFS: <016.연구소>

1. 아이디어:
    2: 바이러스
    1: 벽
    0: 바이러스가 퍼질 수 있는 공간

    바이러스가 벽에 완벽히 갇힌게 아니라면 0이있는 곳으로 퍼진다.
    주어진 행렬에서 벽 3개를 새로 새웠을 때(dfs), 행렬을 copy.deepcopy 한 후 바이러스가 퍼지는 경우 체크 -> 안전영역이 제일 큰 경우 답으로 리턴
    브루트포스 기법 사용

2. 구현:
    1) 행렬에 벽을 3개 세우기 : 0의 좌표 리스트를 추출한 후, 방문 리스트를 활용하여 조합을 구한다.
    2) 세웠을 때, 바이러스 퍼뜨리기
    3) 안전영역의 최대 크기 구하기

"""
import copy

N, M = map(int, input().split())
graph = []
for i in range(N):
    a = list(map(int, input().split()))
    graph.append(a)

# 0인 위치들에 dfs를 통해 가벽을 세워준다.
# 그래프에 영향을 주면 안되기 때문에, copy.deepcopy를 사용한다.
# 벽을 세운 후, 2를 퍼뜨리고, 0의 크기를 구한다.

# 0의 위치를 담을 배열
z_list = []
# 2의 위치를 담을 배열
t_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            z_list.append((i, j))
        elif graph[i][j] == 2:
            t_list.append((i, j))

# 방문처리를 위한 배열
visited = [False] * (len(z_list))
# 최종 리턴할 정답 값
result = 0


# dfs 방식으로 벽을 3개 세운 후, 복사 그래프에 바이러스를 퍼뜨리고, 안전영역의 크기를 구한다.
def mk_wall(cnt):
    global result
    answer = 0
    # 벽이 3개 되었을 때
    if cnt == 3:
        w = copy.deepcopy(graph)
        for two in t_list:
            x, y = two
            mk_virus(w, x, y)
        for a in w:
            answer += a.count(0)
        # 최종 결과값에 안전영역의 최대 크기를 업데이트 해준다.
        result = max(result, answer)
        return

    # 벽 세우기
    for i in range(len(z_list)):
        if not visited[i]:
            visited[i] = True
            graph[z_list[i][0]][z_list[i][1]] = 1
            mk_wall(cnt + 1)
            visited[i] = False
            graph[z_list[i][0]][z_list[i][1]] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def mk_virus(w, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if w[nx][ny] == 0:
                w[nx][ny] = 2

                mk_virus(w, nx, ny)


mk_wall(0)
print(result)
