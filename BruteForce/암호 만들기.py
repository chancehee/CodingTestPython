"""
브루트포스: <암호 만들기>

1. 아이디어:
    모든 경우 (순열) 구하기 -> 모음1개이상, 자음2개 이상인지 검사

"""
from itertools import combinations

L, C = map(int,input().split())
arr = list(input().split())
arr.sort()
# 모음 리스트
M = ['a','e','i','o','u']

# 방법1. 재귀로 조합 구하기
def gen_combinations(arr,n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in gen_combinations(rest_arr, n-1):
            result.append([elem]+c)

    return result

# 방법2. combination 라이브러리 사용하기
com = list(combinations(arr,L))

for g in gen_combinations(arr, L):
    m_cnt = 0
    for m in M:
        if m in g:
            m_cnt += 1

    if 1 <= m_cnt and L-m_cnt >= 2:
        print("".join(g))






