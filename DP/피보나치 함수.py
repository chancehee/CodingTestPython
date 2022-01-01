'''
DP: <피보나치 함수>
'''

import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

dp = [[0,0] for _ in range(41)]

dp[0] = [1,0]
dp[1] = [0,1]

if max(data) >= 2:
    for i in range(2,max(data)+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

for d in data:
    print(dp[d][0], dp[d][1])

