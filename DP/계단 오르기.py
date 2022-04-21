"""
DP: <계단 오르기>

1. 아이디어:
    계단을 오르는 방법은 1칸 아니면 2칸씩 이동 할 수 있고
    계단에 쓰여진 숫자의 합이 최대가 되야하고 도착칸은 무조건 밟아야 하므로,
    1칸전 혹은 2칸전 계단을 밟았을 경우 2가지의 경우에서 최대의 값을 메모이제이션 해준다.

"""

import sys
input = sys.stdin.readline

n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

if n==1:
    print(stair[0])
else:
    dp = [0] * (n+1)

    dp[1] = stair[0]
    dp[2] = stair[0] + stair[1]

    for i in range(3, n+1):
        dp[i] = max(stair[i-1]+stair[i-2]+dp[i-3], stair[i-1]+dp[i-2])

    print(dp[n])