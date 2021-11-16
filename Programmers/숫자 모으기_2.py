'''
프로그래머스(level3): <숫자 모으기_2>
'''

# DP 문제
from collections import deque
sticker = [14, 6, 5, 11, 3, 9, 2, 10]
# 고려해야할 것
# 예를 들어 숫자가 5개인경우 1 3 5 / 2 4  말고 1 4 /2 5 이런식으로 숫자가 큰 경우도 있을 수 있다.


def solution(sticker):
    table1 = [0 for _ in range(len(sticker))]
    table1[0] = sticker[0]
    table1[1] = table1[0]

    # 맨 앞 스티커를 떼는 경우
    for i in range(2, len(sticker)-1):
        table1[i] = max(table1[i-1],table1[i-2] + sticker[i])
    value = max(table1)

    # 맨 앞 스티커를 떼지 않는 경우
    table1 = [0 for _ in range(len(sticker))]
    table1[0] = 0
    table1[1] = sticker[1]
    for i in range(2,len(sticker)):
        table1[i] = max(table1[i-1],table1[i-2]+sticker[i])

    print(value, max(table1))

solution(sticker)



