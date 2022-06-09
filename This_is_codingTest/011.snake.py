from collections import deque

# N * N 보드
N = int(input())
# 사과 개수
apple_count = int(input())
# 사과 위치 입력 받기
apples = [[0] * N for _ in range(N)]
for _ in range(apple_count):
    a, b = map(int, input().split())
    apples[a-1][b-1] = 1

# 방향 전환 개수
direction_count = int(input())
# 방향 입력 받기
directions = deque()
for _ in range(direction_count):
    a, b = input().split()
    directions.append((int(a), b))

# 방문 기록 (몸)
body = [[False] * N for _ in range(N)]
# 머리x, 머리y
head_x, head_y = 0, 0
# 경과 시간
second = 0
# 현재 방향
D = "Right"
# 이동 기록을 담을 배열
moves = deque()

while True:
    # 경과 시간
    print(second)
    # 현재 좌표 출력
    print(head_x, head_y)

    # 현재 좌표가 벽에 부딪히거나 / 몸에 닿는 다면 즉시 종료
    if head_x < 0 or head_y < 0 or head_x >= N or head_y >= N:
        break

    if body[head_x][head_y] == True:
        break



    # 이동 기록에 현재 좌표 추가
    moves.append((head_x, head_y))
    # 방문 기록
    body[head_x][head_y] = True



    # 머리x, 머리y 위치에 사과가 있다면 pass / 사과가 없다면 이동 기록 배열에서 꼬리를 자른다.
    if second > 0:
        if apple_count > 0:
            # 사과가 있는지 판단 / 없을 경우 꼬리 자르기
            # 사과가 있는 경우
            if apples[head_x][head_y] == 1:
                # 사과 먹기
                apples[head_x][head_y] = 0
                apple_count -= 1
            # 사과가 없는 경우
            else:
                # 꼬리 자르기
                tx, ty = moves.popleft()
                body[tx][ty] = False
        else:
            # 꼬리 자르기
            tx, ty = moves.popleft()
            body[tx][ty] = False

    # 현재 몸 상태 출력
    for b in body:
        print(b)
    print()

    # 현재 방향과 다음 방향의 관계에 따라서 다음 위치 좌표로 업데이트
    if len(directions) > 0:
        if second == directions[0][0]:
            time, direction = directions.popleft()
            # 현재 방향이 어디인가?
            if D == 'Right':
                # 오른쪽으로 90도
                if direction == 'D':
                    D = 'Down'
                # 왼쪽으로 90도
                elif direction == 'L':
                    D = 'Up'
            elif D == 'Down':
                if direction == 'D':
                    D = 'Left'
                elif direction == 'L':
                    D = 'Right'
            elif D == 'Left':
                if direction == 'D':
                    D = 'Up'
                elif direction == 'L':
                    D = 'Down'
            elif D == 'Up':
                if direction == 'D':
                    D = 'Right'
                elif direction == 'L':
                    D = 'Left'

    # 다음 머리x, 머리y 좌표값 업데이트하기
    if D == 'Right':
        head_y += 1
    elif D == 'Down':
        head_x += 1
    elif D == 'Left':
        head_y -= 1
    elif D == 'Up':
        head_x -= 1

    # 경과 시간 + 1
    second += 1

print(second)
