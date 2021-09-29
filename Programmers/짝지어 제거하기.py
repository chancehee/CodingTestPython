'''
프로그래머스(level2): 짝지어 제거하기
'''

# 1차 시도: 문자열 모든 경우에서 replace를 사용 -> 시간초과
# 2차 시도: 큐, 스택 자료구조를 활용하여 문자열 원소를 즉각적으로 판별  -> 성공

s='baabaa'

from collections import deque

queue = deque()

for i in s:
    if len(queue)==0:
        queue.append(i)
    elif queue[-1]==i:
        queue.pop()
    else:
        queue.append(i)

if queue:
    print(0)
else:
    print(1)



