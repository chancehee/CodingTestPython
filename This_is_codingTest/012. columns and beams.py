"""
구현: <012. 기둥과 보 설치>

1. 아이디어:
   구현 방법을 혼자 생각해보고 구현 하였으나 2일 정도 에러를 고치지 못해서 블로그 글을
   참조하였다.
   구현 아이디어의 핵심은 관통하였으나, 가독성이 좋고 헷갈리지 않게 코드를 짜는 노력이
   필요했다.

   현재 기둥과 보가 설치되었는가를 나타내는 N x N 의 2차원 리스트를 생성하고
   build_frame의 내용물을 순서대로 처리해주면서 2차원 리스트를 갱신한다.
   최종 갱신 2차원 리스트에서 정답 리스트만 추출하여 리턴.

   기둥과 보를 설치 할 때는, 현재 위치에서만 조건 판단을 해주면 되지만
   기둥과 보를 삭제 할 때는, 영향을 줄 수 있는 위치에서도 조건 판단을 해줘야한다.
   ex1) 기둥을 삭제 할 때:
    1) 위 칸이 기둥이면 안된다. (무너짐)
    2) 기둥이 왼쪽 보 아래에 있을 경우
    3) 기둥이 오른쪽 보 아래에 있을 경우
     2), 3)은 보를 지탱하는 기둥이 1개일 경우에 삭제 할 수 없기 때문에 (체크해줘야 한다.)

    ex2) 보를 삭제 할 때:
     1) 왼쪽 보 위에 기둥이 있을 때
     2) 오른쪽 보 위에 기둥이 있을 때
     3) 양 옆의 보가 양쪽에서 지탱하고 있을 경우엔 삭제 불가능.
"""

n = 5

build_frame = [[0, 0, 0, 1],
               [2, 0, 0, 1],
               [4, 0, 0, 1],
               [0, 1, 1, 1],
               [1, 1, 1, 1],
               [2, 1, 1, 1],
               [3, 1, 1, 1],
               [2, 0, 0, 0],
               [1, 1, 1, 0],
               [2, 2, 0, 1]]

# box: 기둥과 보의 상태를 나타내는 2차원 리스트 / 형태: [x좌표, y좌표, 기둥, 보] (존재: 1, 없음: 0)
box = [[] for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        # 기둥, 보 없음 상태로 초기화
        box[i].append([i, j, 0, 0])


# x, y 좌표에서 문제의 조건을 충족 하는가 판단하는 함수
def check(box, x, y):
    # 기둥과 보가 둘다 존재 한다면, 2가지 모두 조건을 만족해야 한다.
    res = True

    # 기둥이 존재 할 때
    if box[x][y][2] == 1:
        # 조건을 만족하는 경우
        # 바닥인 경우 / 기둥위에 설치하는 경우 / 보의 한쪽 위에 설치하는 경우
        if y == 0 or box[x][y-1][2] == 1 or box[x][y][3] == 1 or (x>0 and box[x-1][y][3] == 1):
            res = True
        else:
            return False

    # 보가 존재 할 때
    if box[x][y][3] == 1:
        # 조건을 만족하는 경우
        # 보의 한쪽이 기둥위에 존재 할 때 / 보의 양쪽에 보가 존재 할 때
        if (0<x<n and box[x-1][y][3]==1 and box[x+1][y][3] == 1) or (y>0 and box[x][y-1][2] == 1) or (x<n and y>0 and box[x+1][y-1][2] == 1):
            res = True
        else:
            return False

    return res

# 건설 목록을 순차로 진행
for i, build in enumerate(build_frame):
    # x좌표, y좌표, 기둥(0)인가 보인가(1), 삭제(0)인가 설치(1)인가
    x, y, typ, act = build

    # 설치
    if act == 1:
        # 기둥
        if typ == 0:
            # 기둥을 설치
            box[x][y][2] += 1
            if check(box, x, y) is False:
                box[x][y][2] -= 1
        # 보
        else:
            box[x][y][3] += 1
            if check(box, x, y) is False:
                box[x][y][3] -= 1


    # 삭제
    else:
        # 기둥
        if typ == 0:
            # 기둥이 존재할 때 (존재 하지 않는다면 삭제하면 안된다.)
            if box[x][y][2] > 0:
                box[x][y][2] -= 1
                # 영향을 줄 수 있는 모든 위치에서 검사.
                if (check(box, x, y) and check(box, x, y+1) and check(box, x-1, y+1)) is False:
                    box[x][y][2] += 1
        # 보
        else:
            if box[x][y][3] > 0:
                box[x][y][3] -= 1
                # 영향을 줄 수 있는 모든 위치에서 검사.
                if (check(box, x, y) and check(box, x+1, y) and check(box, x-1, y)) is False:
                    box[x][y][3] += 1

result = []
for i in range(n+1):
    for j in range(n+1):
        if box[i][j][2] == 1:
            result.append([i, j, 0])

        if box[i][j][3] == 1:
            result.append([i, j, 1])

print(result)