'''
브루트 포스: <체스판 다시 칠하기>
'''

import sys
input = sys.stdin.readline
n,m = map(int, input().split())

result = []
data = []
for i in range(n):
    data.append(input().rstrip())

# 반복 횟수
a = n - 7
b = m - 7

x=-1
y=-1
# 시작점 정의
for _ in range(a):
    x += 1
    y = -1
    for _ in range(b):
        y += 1
        # print("시작점: ",x,y)
        cnt1 = 0
        cnt2 = 0
        for i in range(x,8+x):
            for j in range(y,8+y):
                #data[i][j]
                if i%2==0:
                    if j%2==0:
                        if data[i][j] != 'W':
                            cnt1 += 1
                        if data[i][j] != 'B':
                            cnt2 += 1
                    else:
                        if data[i][j] != 'B':
                            cnt1 += 1
                        if data[i][j] != 'W':
                            cnt2 += 1
                else:
                    if j%2==0:
                        if data[i][j] != 'B':
                            cnt1 += 1
                        if data[i][j] != 'W':
                            cnt2 += 1
                    else:
                        if data[i][j] != 'W':
                            cnt1 += 1
                        if data[i][j] != 'B':
                            cnt2 += 1

        result.append(min(cnt1,cnt2))

print(min(result))














