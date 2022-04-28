"""
수학: <쉽게 푸는 문제>

1. 아이디어:
    1 2 2 3 3 3 4 4 4 4 ...
    이런식으로 규칙이 있고 끝의 범위의 최대값이 1000이므로
    합의 공식을 통해 45 ( 45 + 1) / 2 >= 1000 을 넘기는 최소의 숫자 이므로
    45까지 반복문을 통하여 규칙이 있는 배열을 생성하고
    주어진 인덱스사이의 값을 구한다.

"""

import sys
input = sys.stdin.readline

arr = []
for i in range(1,46):
    for j in range(i):
        arr.append(i)

A, B = map(int, input().strip().split())

answer = 0
for i in range(A, B+1):
    answer += arr[i-1]

print(answer)