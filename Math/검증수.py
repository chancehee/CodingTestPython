'''
수학: <검증수>
'''

nums = list(map(int, input().split()))

s = 0
for n in nums:
    s += n**2

print(s%10)



