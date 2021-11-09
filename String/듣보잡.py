'''
문자열: <듣보잡>
'''
# 듣보잡 수와 그 명단을 사전순으로 출력

import sys

result = set()

input = sys.stdin.readline

N, M = map(int,input().split())
a = set()
for i in range(N):
    a.add(input().rstrip())

for _ in range(M):
    x = input().rstrip()
    if x in a:
        result.add(x)

result_list = list(result)
result_list.sort()


print(len(result))
for i in result_list:
    print(i)



