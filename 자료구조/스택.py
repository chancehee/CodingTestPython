'''
자료구조 : <스택>
'''
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
stack = deque()
for _ in range(t):
    a = input()

    b = a.split()

    if b[0] == 'push':
        stack.append(int(b[1]))
    elif b[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif b[0] == 'size':
        print(len(stack))
    elif b[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif b[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

