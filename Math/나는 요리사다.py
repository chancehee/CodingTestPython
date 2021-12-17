'''
수학: <나는 요리사다>
'''
result = []
temp = 0
cnt = 0
for i in range(1,6):
    x = list(map(int, input().split()))
    if temp <= sum(x):
        temp = sum(x)
        cnt = i

print(cnt, temp)

