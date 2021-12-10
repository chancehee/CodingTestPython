'''
DP : <1로 만들기>
'''
# 아이디어: 모든 경우의 수를 고려하여 연산횟수가 최소가되게 만든다(상향식)

n = int(input())
d = [0] * (n+1)


for i in range(2,n+1):
    d[i] = d[i-1] + 1

    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)


print(d[n])



