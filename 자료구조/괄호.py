'''
자료구조 : <괄호>
'''
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    q= deque()
    d = list(input().strip())
    for i in d:
        q.append(i)
        if len(q)>=2:
            if q[-2]+q[-1] == "()":
                q.pop()
                q.pop()

    if q:
        print('NO')
    else:
        print('YES')
