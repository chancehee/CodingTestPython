'''
문자열: <단어 정렬>
'''

import sys
input = sys.stdin.readline

N = int(input())
temp = set()
for i in range(N):
    temp.add(input().strip())

a = list(temp)
a.sort(key=lambda x : (len(x),x))


for x in a:
    print(x)