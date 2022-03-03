'''
브루트포스: 연산자 끼워넣기
'''
from itertools import permutations
from collections import deque
n = int(input())

data = list(map(int, input().split()))

op = list(map(int, input().split()))
per = []
for c,o in enumerate(op):
    if o == 0:
        continue
    for i in range(o):
        if c==0:
            per.append('+')
        elif c==1:
            per.append('-')
        elif c==2:
            per.append('*')
        elif c==3:
            per.append('/')

x = list(set(permutations(per)))
print(x)

queue = deque()
for ops in x:
    a = 0
    b = 0
    for i in range(len(data)+len(ops)):
        if i%2==0:
            queue.append(data[a])
            a = a+1
        else:
            queue.append(ops[b])
            b = b+1
    print(queue)
