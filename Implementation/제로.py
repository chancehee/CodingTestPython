'''
구현: <제로>
'''

from collections import deque
import sys

N = int(input())

input = sys.stdin.readline

record = deque()

for i in range(N):
    a = int(input().strip())
    if a != 0:
        record.append(a)
    else:
        record.pop()


print(sum(record))

