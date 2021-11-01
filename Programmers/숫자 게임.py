'''
프로그래머스(level3) : <숫자 게임>
'''


# 비교 숫자가 큰 경우에는 승점을 올리고, A 숫자를 제거하고 , B 커서 이동
# 아닌경우에는 A 숫자는 유지하고, B 커서 이동만 한다
# while 문을 통해 A의 숫자가 없거나 / B 커서가 전부 이동한 경우 종료

from collections import deque

A = [5,1,3,7]
B = [2,2,6,8]


def solution(A, B):
    A.sort()
    B.sort()
    q1 = deque(A)

    win = 0
    i = 0
    while q1 and i != len(A):
        if q1[0] < B[i]:
            win = win + 1

            q1.popleft()
            i = i + 1

        else:
            i = i + 1

    return win

print(solution(A,B))



