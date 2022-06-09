"""
그래프 이론: <특정 거리의 도시 찾기>

1. 아이디어:
    특정 지점에서 다른 노드에 대하여 BFS를 수행하여 최단 거리를 구한다.
    거리 배열 선언
    자기 자신으로 가는 거리 = 0
    인접 노드들 에서 방문을 안했다면, 이전 노드 + 1로 거리 갱신
    방문 여부를 따로 기록할 필요 없이, 최초 선언 값이 변했다면 방문을 한 것으로 간주

"""
from collections import deque
import sys
input = sys.stdin.readline
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시
n, m, k, x = map(int, input().strip().split())
# 도시의 연결 정보를 2차원 인접 리스트 방식으로 표현 (0번째 칸은 사용 x)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    # 단방향, a -> b 이므로, graph[a]에 인접한 도시 b를 추가해준다.
    graph[a].append(b)
INF = -1
# 거리 정보를 나타내는 배열 생성 (0번째 칸은 사용 x)
distance = [INF] * (n+1)

q = deque()
# 시작위치를 큐에 넣어준다.
q.append(x)
# 자기 자신으로 가는 거리는 0
distance[x] = 0

while q:
    # 현재 노드 번호
    now = q.popleft()

    # 현재 노드에서 인접한 노드들 방문
    for g in graph[now]:
        # 만약 방문한적이 없다면
        if distance[g] == INF:
            # 거리 갱신
            distance[g] = distance[now] + 1
            q.append(g)

cnt = 0
for i,d in enumerate(distance):
    if d == k:
        cnt += 1
        print(i)

if cnt == 0:
    print(-1)