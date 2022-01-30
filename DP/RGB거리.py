'''
DP: <RGB거리>
'''

import sys

input = sys.stdin.readline

data = []
n = int(input())
for i in range(n):
    data.append(list(map(int, input().split())))


# 이전 min값 + 현재 R, G, B 일 경우 더해주기
# 최소값 누적 시키기
for i in range(1,n):
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
    data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]

print(min(data[n-1]))


