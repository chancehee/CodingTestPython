'''
DP: <타일 장식물>
'''

n = int(input())

dp = [0 for _ in range(n+2)]

dp[1] = 4
dp[2] = 6


for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])