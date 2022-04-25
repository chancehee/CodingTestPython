"""
DP: <연속합>

1. 아이디어:
    10만개의 정수가 주어지므로 시간복잡도가 n^2이상을 갖는 다면 시간 초과가 걸린다.
    따라서 재귀나 반복문으로는 해결 X
    동적프로그래밍을 떠올린다.

    규칙을 직접 찾아보고 -> 규칙을 점화식으로 표현하자
    연속된 몇 개의 수의 합 중에서 가장 큰 합을 구하는 것이므로
    각 항에서 최대를 저장하는 배열을 생성한 후
    dp[2] = dp[1] + s[2] vs s[2]  (s는 현재배열)
    이런식으로 최대합이 되는 경우를 갱신해준다.
        1.현재 가장 큰 경우 (시작점 변경)
        2.이전의 합들이 큰 경우 (시작점 유지)

2. 시간 복잡도:
    n번 탐색하면 되기 때문에
    O(n)

"""

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
dp = [0] * n

dp[0] = arr[0]
for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))




