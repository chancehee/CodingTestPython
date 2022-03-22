'''
브루트포스: <완전제곱수>
'''

# 10000 이하의 자연수 범위, 10000은 100의 제곱

m = int(input())
n = int(input())

initial_result = []
result = 0
for i in range(1,101):
    if m<= i*i <= n:
        result += i*i
        if len(initial_result) == 0:
            initial_result.append(i*i)

if result == 0:
    print(-1)
else:
    print(result)
    print(initial_result[0])
