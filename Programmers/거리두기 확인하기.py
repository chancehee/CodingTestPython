'''
프로그래머스(level2): <거리두기 확인하기>
'''
# 유형 bfs
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque

def check(place, sr, sc):
    res = 1

    dy,dx = (-1,0,1,0),(0,1,0,-1)
    visited = [[False]*5 for _ in range(5)]
    visited[sr][sc] = True

    que = deque([(sr,sc,0)])

    while que:
        cr,cc,cd = que.popleft()

        for i in range(4):
            nr,nc = cr+dy[i], cc+dx[i]

            if 0 <= nr <5 and 0<=nc<5 and not visited[nr][nc]:
                if place[nr][nc]=='0' and cd<1:
                    visited[nr][nc] = True
                    que.append((nr,nc,cd+1))
                else:
                    if place[nr][nc]=='P':
                        res = 0
                        break
            if res==0:
                break
    return res

def solution(places):
    answer = []
    for place in places:
        is_safe = 1

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    is_safe = check(place, i, j)

                    if is_safe==0:
                        break
            if is_safe==0:
                break

        answer.append(is_safe)
    return answer
print(solution(places))



