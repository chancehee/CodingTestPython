"""
프로그래머스: <거리두기 확인하기>

대기실 5개 (5 X 5 크기)
거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2이하로 앉으면 안됨
단, 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용됨

맨해튼 거리: |x2-x1| + |y2-y1|

응시자: p
빈 테이블: o
파티션: x
대기실 정보: places 2차원 배열

5개의 대기실에서 거리두기가 잘 지키고 있는지 확인
잘 지켰다면 -> 1
아니라면 -> 0


1.아이디어:
    P의 위치에서 상하좌우 비교 P 일 경우 False
    아닐경우 맨해튼 거리가 2인경우를 비교
        이때 칸막이 여부 조건 추가

    대기실 마다 모든 P에 대하여 거리두기가 지켜진 경우 정답 배열에 1추가
    아닐경우 0추가

    정답 배열 리턴.

"""

places = [
    ["OOPOO",
     "OPOOO",
     "OOOOO",
     "OOOOO",
     "OOOOO"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

# 0    1   2   3   4    5     6   7       8           9          10        11
# 우, 좌, 하, 상, 2우, 2좌, 2하, 2상, 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위
dx = [0, 0, 1, -1, 0, 0, 2, -2, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 2, -2, 0, 0, 1, -1, -1, 1]

# 거리두기 여부를 담을 배열 (강의실 개수 만큼)
result = [[] for _ in range(5)]


def solution(places):
    global result

    def dfs(x, y, place):

        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue

            # 상하좌우(맨해튼 거리 1인 경우)
            if i < 4:
                if place[nx][ny] == 'P':
                    return False

            # 맨해튼거리 2인 경우
            else:
                if place[nx][ny] == 'P':
                    if i == 4:
                        # 칸막이가 없는 경우
                        if place[x][y + 1] == 'O':
                            return False
                    elif i == 5:
                        if place[x][y - 1] == 'O':
                            return False
                    elif i == 6:
                        if place[x + 1][y] == "O":
                            return False
                    elif i == 7:
                        if place[x - 1][y] == "O":
                            return False
                    elif i == 8:
                        # 대각선에 위치 하였을 때 칸막이가 모두 있어야 한다. (아닌 경우 False)
                        if place[x][y + 1] == 'O' or place[x + 1][y] == 'O':
                            return False
                    elif i == 9:
                        if place[x][y - 1] == 'O' or place[x + 1][y] == 'O':
                            return False
                    elif i == 10:
                        if place[x - 1][y] == 'O' or place[x][y - 1] == 'O':
                            return False
                    elif i == 11:
                        if place[x - 1][y] == 'O' or place[x][y + 1] == 'O':
                            return False

        # 위의 조건을 다 만족한 경우 (거리두기를 지킨 경우)
        return True

    for k, place in enumerate(places):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    result[k].append(dfs(i, j, place))


answer = []
solution(places)
for r in result:
    if False in r:
        answer.append(0)
        continue
    else:
        answer.append(1)

# 정답 배열 출력
print(answer)