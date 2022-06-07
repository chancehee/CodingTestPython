"""
그리디: <A와 B>

1. 아이디어:
    문자열 S, 문자열 T가 입력으로 주어진다.
    2가지 연산만을 통하여 S를 T로 바꾸려고 할 때, 가능한지 판단하는 함수 작성하기
    1. 문자열의 뒤에 A를 추가한다.
    2. 문자열을 뒤집고 뒤에 B를 추가한다.

    T의 마지막 문자가 A인 경우 제거
    B인 경우 제거하고 문자열 뒤집기를 반복하여
    len(S)와 len(T) 길이가 같아졌을 때 -> 같다면 가능 아니면 불가능 판단.
"""
from collections import deque
import sys
input = sys.stdin.readline
S = input().strip()
T = input().strip()
length = len(T) - len(S)
q = deque(T)


for i in range(length):
    if q[-1] == 'A':
        q.pop()
    else:
        q = q.reverse()
        if q[-1] == 'B':
            q.pop()

result = ''.join(q)

if result == S:
    print(1)
else:
    print(0)