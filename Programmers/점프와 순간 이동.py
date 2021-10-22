'''
프로그래머스(level2): <점프와 순간 이동>
'''
dis = 0

N = 5000
# 수학적으로 생각해보자..
cnt = 1
while N!=1:
    if N%2==0:
        N =N //2
    else:
        N = N - 1
        cnt = cnt + 1
print(cnt)


