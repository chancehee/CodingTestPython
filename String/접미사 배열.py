'''
문자열: <접미사 배열>
'''

import sys

input = sys.stdin.readline

s = input().rstrip()

result = []
for i in range(len(s)):
    result.append(s[i:])

result.sort()

for r in result:
    print(r)