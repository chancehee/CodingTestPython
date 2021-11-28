'''
그리디: <30>
'''
# 배수 판정법을 통하여 푼다.
# 3 의 배수인경우 : 각 자리 숫자의 합이 3의 배수인 수
N = input()
n = sorted(N,reverse=True)
result = 0
s = 0
if '0' not in N:
    result = -1
for i in N:
    s += int(i)

if s%3 != 0:
    result = -1


if result == -1:
    print(-1)
else:
    print("".join(n))

