'''
그리디: <2+1 세일>
'''

import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)
count = n // 3

k = 2
for i in range(count):
    data[k] = 0
    k = k+3

print(sum(data))