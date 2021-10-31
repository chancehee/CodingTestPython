'''
프로그래머스(level2) : <소수 찾기>
'''
import itertools
import math

numbers = '17'
def isPrime(x):
    if x == 0:
        return False
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    cnt = 0
    n = []

    for i in numbers:
        n.append(i)

    init = list(set(map(int, n)))

    length = len(n)

    for i in range(2, length + 1):
        a = set(map(''.join, itertools.permutations(n, i)))
        a = list(map(int, a))
        init = init + a
    init = list(set(init))
    print(init)
    for i in init:
        if isPrime(i):
            cnt += 1
    return cnt

print(solution(numbers))



