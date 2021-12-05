'''
그리디: <방 번호>
'''
import math

n = input()
count = [0 for _ in range(10)]

for i in n:

    count[int(i)] = count[int(i)] + 1


s = math.ceil((count[6] + count[9])/2)
count[6]=s
count[9]=s

print(max(count))