'''
그리디: <통나무 건너뛰기>
'''
# 아이디어 큐자료형을 활용하고 데이터를 정렬후 가장 작은 숫자부터 양 옆에 어떤 숫자를 놓아야 차이가 적게 될까를 고려하며 구현

from collections import deque
import sys
input = sys.stdin.readline

def solution(n,data):
    data.sort()
    queue = deque()
    # 데이터가 5개 이상이므로 처음 3개는 큐에 넣고 시작한다.
    # 큐에 데이터를 올바르게 넣었을때 그중에서 차이가 가장많이나는것을 M으로설정(=난이도)
    queue.append(data[0])
    queue.append(data[1])
    queue.appendleft(data[2])
    M = max(abs(queue[2] - queue[1]),abs(queue[0] - queue[1]))
    idx = 3
    while True:
        # 종료 조건
        if idx>=n:
            break

        # 일반적인 경우 : 뒤에 데이터가 2개 이상 있을 때
        if idx+1 < n:
            a,b = data[idx],data[idx+1]
            m1 = a - queue[0]
            m2 = b - queue[-1]
            m = max(abs(m1),abs(m2))
            s1 = b - queue[0]
            s2 = a - queue[-1]
            s = max(abs(s1),abs(s2))
            if m <= s:
                queue.append(b)
                queue.appendleft(a)
                if m > M:
                    M = m
            else:
                queue.append(a)
                queue.appendleft(b)
                if s > M:
                    M = s

            idx += 2
        # 특수한 경우 : 뒤에 데이터가 1개 남은 경우
        else:
            a = data[idx]
            m1 = a - queue[0]
            m2 = a - queue[-1]
            if m1 < m2:
                queue.appendleft(a)
            else:
                queue.append(a)
            x = max(m1,m2)
            if x > M:
                M = x
            idx += 1
    print(M)


t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))

    solution(n,data)






