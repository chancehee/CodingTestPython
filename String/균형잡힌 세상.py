'''
문자열: <균형잡힌 세상>
'''

import sys
from collections import deque
input = sys.stdin.readline

data = ["[","]","(",")"]
while True:
    a = input().rstrip()

    if a == '.':
        break

    stack = deque()

    # 공백 제거


    # 괄호만 비교하기
    for i in a:
        if i in data:
            stack.append(i)

            if len(stack) >= 2:
                if stack[-2]=="[" and stack[-1]=="]":
                    stack.pop()
                    stack.pop()
                elif stack[-2]=="(" and stack[-1]==")":
                    stack.pop()
                    stack.pop()

    if stack:
        print("no")
    else:
        print("yes")

