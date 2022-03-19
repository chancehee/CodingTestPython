'''
브루트포스: <차이를 최대로>
'''

'''
1. 아이디어
    배열의 원소로 조합가능한 모든 경우의 배열 만들기.
'''

N = int(input())
arr = list(map(int, input().split()))

# 배열의 원소로 모든 경우 조합하기
from itertools import permutations

data = list(permutations(arr,N))
result = 0
for d in data:
    s = 0
    for i in range(len(d)-1):
        s += abs(d[i] - d[i+1])
    result = max(result, s)
print(result)

