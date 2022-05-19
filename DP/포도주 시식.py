"""
DP: <포도주 시식>

1. 아이디어:
    포도주를 연속으로 2개까지만 마실수 있다.
    이 조건에 따라서 n개의 포도주 중에서 최대로 마시는 경우를 생각해본다.
    ex) 6 10 13 9 8 1
    거꾸로 생각해본다.
    1. 한 칸 이전을 마신경우 두 칸전은 마실 수 없다.
        dp[6] = s[6] + s[5] + dp[3]
    2. 한 칸 이전을 마시지 않은 경우, 두 칸전에서 최대로 마시는 경우.
        dp[6] = dp[4]
    3. 현재 포도주를 마시지 않는 경우
        dp[6] = dp[5]

"""
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n+1)
if n==1:
    print(arr[0])
elif n==2:
    print(arr[0]+arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[1], arr[1]+arr[2], arr[0]+arr[2])

    for i in range(3,n):
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1],dp[i-1])

    print(max(dp))