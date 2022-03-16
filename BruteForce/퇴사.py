'''
브루트포스: <퇴사>
'''

import sys
input = sys.stdin.readline

n = int(input())
schedule = []

for i in range(n):
    schedule.append(list(map(int,input().split())))

dp = [0 for _ in range(n+1)]

# 거꾸로 생각
for i in range(n-1, -1, -1):
    # 날짜가 초과되어 상담이 불가한 경우
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # 당일 보상 + 다음 보상 vs 당일 일을 하지 않고 넘어 갈때 보상
        # max_pay[i] = max(pay + max_pay[i+day] , max_pay[i+1])
        dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i+1])

print(dp[0])
