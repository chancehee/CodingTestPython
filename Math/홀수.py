'''
수학: <홀수>
'''

result = []
for _ in range(7):
    a = int(input())

    if a%2==1:
        result.append(a)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
