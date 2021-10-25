'''
프로그래머스(level2) : <방문 길이>
'''

dirs = "ULURRDLLU"
visited = set()

v = [[0,1],[0,-1],[-1,0],[1,0]]
# 시작 좌표
x,y = 0,0

# 아이디어: 고유한 식별자 필요 / 0,0 -> 0,1 로 이동한 경우  0,1 -> 0,0 이동한 경우  0001 0010 0001
# 1,1 -> 0,1 이동한 경우  1011 -> 0111 2가지 중첩되는 경우를 set으로 중복 방지 처리 해주기

# 정답이긴 하였으나 코드가 비효율 적으로 길다..
# 다른 사람의 풀이 참고 해보기

for d in dirs:
    temp_x = ""
    temp_y = ""
    temp_1 = ""
    temp_2 = ""
    if d == 'U':
        if y+v[0][1] >5:
            continue
        else:
            # 처리 전 x,y
            temp_x = str(x)
            temp_y = str(y)
            y = y+v[0][1]
            temp_1 = temp_x + str(x)
            temp_1 = list(temp_1)
            temp_1.sort()
            temp_1 = "".join(temp_1)

            temp_2 = temp_y + str(y)
            temp_2 = list(temp_2)
            temp_2.sort()
            temp_2 = "".join(temp_2)
    elif d == 'D':
        if y+v[1][1] <-5:
            continue
        else:
            temp_x = str(x)
            temp_y = str(y)
            y = y+v[1][1]
            temp_1 = temp_x + str(x)
            temp_1 = list(temp_1)
            temp_1.sort()
            temp_1 = "".join(temp_1)

            temp_2 = temp_y + str(y)
            temp_2 = list(temp_2)
            temp_2.sort()
            temp_2 = "".join(temp_2)
    elif d == 'L':
        if x+v[2][0] < -5:
            continue
        else:
            temp_x = str(x)
            temp_y = str(y)
            x =x+v[2][0]
            temp_1 = temp_x + str(x)
            temp_1 = list(temp_1)
            temp_1.sort()
            temp_1 = "".join(temp_1)

            temp_2 = temp_y + str(y)
            temp_2 = list(temp_2)
            temp_2.sort()
            temp_2 = "".join(temp_2)
    else:
        if x+v[3][0] >5:
            continue
        else:
            temp_x = str(x)
            temp_y = str(y)
            x =x+v[3][0]
            temp_1 = temp_x + str(x)
            temp_1 = list(temp_1)
            temp_1.sort()
            temp_1 = "".join(temp_1)

            temp_2 = temp_y + str(y)
            temp_2 = list(temp_2)
            temp_2.sort()
            temp_2 = "".join(temp_2)

    visited.add(temp_1+temp_2)

print(len(visited))


# 다른사람의 풀이
# 아이디어는 똑같다 / 구현 에서의 깔끔함이 느껴진다.
'''
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
'''


