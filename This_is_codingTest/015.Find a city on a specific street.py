"""
DFS/BFS: <015.특정 거리의 도시 찾기>

1. 아이디어:
    거리 테이블 선언
    시작점에서 자기 자신으로 가는 거리 0으로 설정
    BFS방식으로 인접한 모든 노드에 대한 거리 테이블 업데이트
"""
from collections import deque
import sys
input = sys.stdin.readline
INF = 1e9
# 도시의 개수,
N, M, K, start = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)

q = deque()
q.append(start)
distance[start] = 0

while q:
    now = q.popleft()
    for g in graph[now]:
        # 처음 방문인 경우
        if distance[g] == INF:
            if distance[g] > distance[now] + 1:
                distance[g] = distance[now] + 1
            q.append(g)

flag = True
for i in range(len(distance)):
    if distance[i] == K:
        print(i)
        flag = False

if flag:
    print(-1)
