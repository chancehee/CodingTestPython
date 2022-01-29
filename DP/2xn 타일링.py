'''
DP: <2xn 타일링>
'''

n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 2


def sol(n):
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1] % 10007

if n>=3:
    print(sol(n))
else:
    print(dp[n-1])






