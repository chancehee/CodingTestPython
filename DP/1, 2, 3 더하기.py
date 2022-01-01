'''
DP: <1, 2, 3 더하기>
'''

# 1 2 3의 합으로 입력 받은 정수 n 구하기 방법의 수는?
# 점화식을 찾는게 오래걸렸다.
# f(n) = f(n-1) + f(n-2) + f(n-3)
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(12)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(n):
    a = int(input())
    print(dp[a])


