'''
프로그래머스(level1): <로또의 최고 순위와 최저 순위>
'''

# 내 풀이

'''
lottos = [44,1,0,0,31,25]
win_nums = [31,10,45,1,6,19]

def solution(lottos, win_nums):
    cnt = 0
    rank = []
    for w in win_nums:
        if w in lottos:
            cnt += 1

    zero_count = lottos.count(0)

    t1 = cnt + zero_count
    t2 = cnt

    r1 = 6
    r2 = 6

    if t1 == 6:
        r1 = 1
    elif t1 == 5:
        r1 = 2
    elif t1 == 4:
        r1 = 3
    elif t1 == 3:
        r1 = 4
    elif t1 == 2:
        r1 = 5

    if t2 == 6:
        r2 = 1
    elif t2 == 5:
        r2 = 2
    elif t2 == 4:
        r2 = 3
    elif t2 == 3:
        r2 = 4
    elif t2 == 2:
        r2 = 5

    rank = [r1, r2]
    return rank
'''

# 다른 사람 풀이법
lottos = [0,0,0,0,0,0]
win_nums = [31,10,45,1,6,19]

ranks = [6,6,5,4,3,2,1] # 꼴등 1등 2등 3등 4등 5등

def solution(lottos,win_nums):
    zero_count = lottos.count(0)
    cnt = 0
    rank = []

    for w in win_nums:
        if w in lottos:
            cnt +=1

    r1 =  rank[cnt + zero_count]
    r2 =  rank[cnt]
    rank = [r1,r2]
    return rank
print(solution(lottos,win_nums))







