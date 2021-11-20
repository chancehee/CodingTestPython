'''
수학: <팩토리얼 0의 개수>
'''
import math
N = int(input())
s = str(math.factorial(N))

cnt = 0
for i in range(1,len(s)+1):
    if s[-i] == '0':
        cnt += 1
    else:
        break

print(cnt)