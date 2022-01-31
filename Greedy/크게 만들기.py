'''
그리디: <크게 만들기>
'''
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
a =k
data = list(input())
queue = deque()

for i in range(n):
    while k and len(queue) > 0:
        if queue[-1] < data[i]:
            queue.pop()
            k = k - 1
        else:
            break
    queue.append(data[i])
result = list(queue)
print(int("".join(result[:n-a])))







