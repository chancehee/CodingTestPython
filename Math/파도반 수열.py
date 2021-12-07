'''
수학: <파도반 수열>
'''

from collections import deque

T = int(input())
data = []

queue = deque([1,1,1,2,2])

i = 0
while True:
    if i==95:
        break
    queue.append(queue[-1]+queue[i])
    i += 1

for _ in range(T):
    n = int(input())
    print(queue[n-1])


