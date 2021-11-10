'''
브루트포스: <블랙잭>
'''
from itertools import combinations

n=10
m=500

data = [93 ,181, 245, 214, 315, 36 ,185 ,138, 216 ,295]

k = 0

x = list(combinations(data,3))
for i in x:
    if sum(i)<=m and sum(i)>k:
        k = sum(i)
print(k)



