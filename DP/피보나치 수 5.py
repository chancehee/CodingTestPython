'''
DP: <피보나치 수 5>
'''

n = int(input())

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 1

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


print(fibo(n))

