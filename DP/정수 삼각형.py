'''
DP: <정수 삼각형>
'''

import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

if n==1:
    print(data[0][0])
else:
    data[1][0] = data[0][0] + data[1][0]
    data[1][1] = data[0][0] + data[1][1]

    for i in range(2,n):
        for j in range(len(data[i])):
            if j==0:
                data[i][j] = data[i-1][j]+data[i][j]
            elif j== len(data[i]) - 1:
                data[i][j] = data[i-1][j-1] + data[i][j]
            else:
                data[i][j] = max(data[i-1][j-1] + data[i][j], data[i-1][j] + data[i][j])

    print(max(data[-1]))



