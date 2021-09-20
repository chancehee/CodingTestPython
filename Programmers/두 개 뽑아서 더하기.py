'''
프로그래머스(level1): <두 개 뽑아서 더하기>
'''
from itertools import combinations
numbers = [5,0,2,7]

a = list(combinations(numbers,2))
num = set()
for i in a:
    num.add(sum(i))

print(sorted(list(num)))


