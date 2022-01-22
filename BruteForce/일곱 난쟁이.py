'''
브루트 포스: <일곱 난쟁이>
'''
from itertools import combinations

data = []
for i in range(9):
    data.append(int(input()))
data.sort()
A = list(combinations(data, 7))

answer = 0
for a in A:
    if sum(a) == 100:
        answer = a
        break

for i in answer:
    print(i)




