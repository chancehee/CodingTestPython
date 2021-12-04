'''
그리디: <알바생 강호>
'''
import sys
input = sys.stdin.readline
n = int(input())
data = []
ans = 0
for i in range(n):
    a = int(input())
    data.append(a)
data.sort(reverse=True)

for i in range(len(data)):
    tip = data[i] - (i+1 - 1)

    if tip <0:
        break

    ans += tip
print(ans)


