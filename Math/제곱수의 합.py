'''
수학: <제곱수의 합>
'''

# 그리디 문제인줄 알았더니 12일경우 큰수부터 접근하면 답이 아니다.
# 따라서 DP로 접근하자
# 이해하기 어려워서 블로그글 참조 :
# 모든 수는 1의 제곱으로 만들 수 있으며 그 때 합의 갯수는 숫자 n일때 n개이다.
# 4일 때는 1의제곱 4개도 가능하지만, 2의 제곱 1개로 만들 수 있다.
# dp[4] = min(dp[4],dp[4-(2*2)+1] 따라서 n의 숫자보다 적은 범위내에서 모든 경우의 수를 따져봐야한다.

import math

n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i] = i
    for j in range(1,int(math.sqrt(i))+1):
        dp[i] = min(dp[i],dp[i - j*j]+1)
print(dp[n])