'''
최단 경로 알고리즘: 가장 짧은 경로를 찾는 알고리즘(= 길 찾기 문제)
    -유형이 다양하다
    -상황에 맞는 효율적인 알고리즘이 이미 정립되어 있다.
    -노드 / 간선
    -코딩 테스트 문제는 최단 경로를 출력하는 문제보다는 단순히 최단 거리를 출력하는 문제가 많이 출제된다.
    -주로 많이 등장하는 알고리즘 2가지: 다익스트라 최단경로, 플로이드 워셜 알고리즘
    -그리디 알고리즘과 다이나믹 프로그래밍이 적용된다.

    1.다익스트라 알고리즘(=데이크스트라)
        조건: '음의 간선'이 없을 때 정상적으로 동작한다.
        기본적으로 그리디 알고리즘으로 분류한다 ( 매번 가장 비용이 적은 노드를 선택하는 과정을 반복하기 때문)
        알고리즘 원리:
        1)출발 노드를 설정한다.
        2)최단 거리 테이블을 초기화 한다.
        3)방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
        4)해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
        5)위 과정에서 3과4번을 반복한다.
        구현 방법2가지: 구현하기 쉽지만 느리게 동작하는 코드, 구현하기 까다롭지만 동작이 빠른 코드
        후자를 공부해야 한다.

        초기 최단 거리를 무한으로 세팅 1e9(10억)
        출발 노드로의 거리는 0
        최단 거리값이 같을 때는 일반적으로 번호가 작은 노드를 선택한다.
'''

#간단한 다익스트라 알고리즘: 시간복잡도 O(V^2) V는 노드의 갯수
import sys
input = sys.stdin.readline
INF = int(1e9) #무한대

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF] * (n+1)

#모든 간선 정보 받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def djikstra(start):
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost<distance[j[0]]:
                distance[j[0]] = cost


djikstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])