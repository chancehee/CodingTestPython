"""
브루트포스: <치킨 배달>

1. 아이디어:
    조합을 사용하여(순열 X) 치킨집을 폐업 시킨다.
    탐색을 통해 치킨 거리 최소의 합을 구한다.
    최소의 합중에서 가장 작은 값을 리턴
"""

from itertools import combinations
import copy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 2의 좌표가 담긴 좌표리스트 생성
two_list = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            two_list.append([i,j])

# 조합을 통해서 치킨집을 제거해야하는 조합의 좌표를 구한다
com = list(combinations(two_list, len(two_list)-M))


# 치킨 거리 최소값을 구하는 함수
def solve(arr, x, y):
    temp = 999
    for two in two_list:
        a,b = two
        if arr[a][b] == 2:
            temp = min(temp, abs(a-x) + abs(b-y))
    return temp


result = []
for i in range(len(com)):
    graph = copy.deepcopy(arr)
    # 제거해야하는 치킨집들을 0으로 만들어준다.
    for c in com[i]:
        x,y = c
        graph[x][y] = 0
    answer = 0

    # 제거된 상태의 배열에서 치킨 거리를 구해준다.
    # 구한 치킨 거리의 합을 배열에 담는다.
    for a in range(N):
        for b in range(N):
            if graph[a][b] == 1:
                answer += solve(graph, a, b)
    result.append(answer)
# 배열중에서 최소값을 출력해준다.
print(min(result))


