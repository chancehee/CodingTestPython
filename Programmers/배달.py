'''
프로그래머스(level2) : <배달>
'''

# 다익스트라 알고리즘 # 공부하기위하여 블로그 글 참조 # 최단거리 # heap자료구조
# 한번에 이해가 가지 않는다.. 반복해서 숙지할 것.
import heapq

N=5
road=[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

# adj구성 : 비용, 노드 (인접행렬)
def dijkstra(dis, adj):
    heap = []
    # 시작점인 1번노드에서 비용이 0인 상태로 시작
    heapq.heappush(heap, [0,1])

    while heap:

        cost, node = heapq.heappop(heap)
        # 현재 비용은 0, 노드는 1

        for c,n in adj[node]:
            # 1번 노드로 가는 비용이 가장 작은 값으로 거리 테이블 수정
            if cost+c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost+c, n])

def solution(N,road,K):
    INF = float('inf')
    # 거리 테이블 생성
    dis = [INF]*(N+1)
    dis[1] = 0
    # 인접 행렬
    adj = [[] for _ in range(N+1)]

    for r in road:
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(dis,adj)
    return len([x for x in dis if x<=K])

print(solution(N,road,K))






