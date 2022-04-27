"""
DP: <가장 긴 증가하는 부분 수열>

1. 아이디어:
    맨 앞에서 숫자가 증가하는 방향으로
    맨 뒤에서 숫자가 감소하는 방향으로
    df = [] 테이블을 생성 후 값을 갱신 해주는 방법
    연습 필요

"""
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().strip().split()))
dp = [1] * (n+1)

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
