'''
프로그래머스(level2) : <조이스틱>
'''
# A: 65
# B: 66
# N: 78
# Z: 90
name= 'ZZAAAZZ'
def solution(name):
    # 아스키코드를 활용한 숫자변경을 위한 횟수 값 구하기 (반을 기준으로 적은 숫자 선택)
    cnt = 0
    for i in range(len(name)):
        o = ord(name[i]) - ord('A')
        if o > 13:
            o = 26 - o
        cnt = cnt + o


    c = 1
    c2 = 1


    if name[1] == 'A':
        for i in range(2, len(name)):
            if name[i] == 'A':
                c = c + 1
            else:
                break

    if name[-1] == 'A':
        for i in range(2, len(name)):
            if name[-i] == 'A':
                c2 = c2 + 1
            else:
                break

    # 위 두가지 경우가 아닌 경우
    c3 = len(name) - 1

    # 갔다가 돌아오는 경우
    c4 = 0
    c44 = 0
    for i in range(len(name) - 1):
        if name[i + 1] == 'A':
            c44 = name[::-1].find('A')
            break
        else:
            c4 = c4 + 1
    c5 = c4 * 2 + c44


    if name[1] == 'A' and name[-1] == 'A':
        r = len(name) - min(c, c2) - 1
    elif name[1] == 'A':
        r = len(name) - c - 1
    elif name[-1] == 'A':
        r = len(name) - c2 - 1
    else:
        r = min(c3, c5)

    return cnt + r
print(solution(name))