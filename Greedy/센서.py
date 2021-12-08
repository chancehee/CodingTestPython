'''
그리디 : <센서>
'''

import sys
input= sys.stdin.readline

N =int(input())
G = int(input())
data = list(map(int, input().split()))
data.sort()
sub_data = []
for i in range(N-1):
    sub_data.append(data[i+1]-data[i])
sub_data.sort(reverse=True)


if sub_data:
    for _ in range(G-1):
        sub_data.pop(0)
    print(sum(sub_data))
else:
    print(0)




