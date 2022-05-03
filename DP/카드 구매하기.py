"""
DP: <카드 구매하기>

1. 아이디어:
    N개의 카드를 갖기 위한 방법으로, 카드 개수를 딱 맞게 사야한다. (가장 비싸게 사야함)
    예)
    4장을 사려한다
    1장팩: 1원, 2장팩: 5원, 3장팩: 6원, 4장팩: 7원
        4장을 사는 경우
        1장팩 * 4 = 4원
        2장팩 * 2 = 10원
        3장팩 + 1장팩 = 7원
        4장팩 = 7원
        답: 10원

    모든 경우를 조합하기엔 N의 범위가 1000이고, 그리디로 풀 수 없다.
    따라서 메모이제이션을 통해서, 카드를 1~N개 까지 사는 경우에 대한 최대 값을 저장해두고 재활용 해야 한다.

    위의 예제에서
    (인덱스 시작을 0으로 정의 하겠다.)
    dp[1] = arr[1] = 1
    dp[2] = arr[2] vs dp[1]+dp[1] = 5
    dp[3] = arr[3] vs dp[1]+dp[2] vs dp[2]+dp[1] = 6
    dp[4] = arr[4] vs dp[1]+dp[3] vs dp[2]+dp[2] vs dp[3]+dp[1] = 10
    이렇게 최대값을 반복문을 통해 탐색하여 값을 찾는다.
"""

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().strip().split()))
dp = [0] * (N+1)
dp[1] = arr[0]

for i in range(2, N+1):
    dp[i] = arr[i-1]
    for j in range(1, i):
        dp[i] = max(dp[i-j] + dp[j], dp[i])

print(dp[N])
