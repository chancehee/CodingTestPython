"""
프로그래머스: <소수 찾기> (재귀로 풀이)

1. 아이디어:
    재귀함수를 사용하여 가능한 모든 숫자 조합을 먼저 만든다.
    그 후에, 각각의 숫자들이 소수인지 판단.
    소수의 개수 리턴

"""
import math


def is_prime(x):
    if x == 0:
        return False
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    prime_set = set()
    temp = []
    visited = [False] * len(numbers)

    def make_combinations(cnt):
        if cnt > 0:
            prime_set.add(int("".join(temp)))

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                temp.append(numbers[i])
                make_combinations(cnt + 1)
                visited[i] = False
                temp.pop()

    make_combinations(0)

    answer = 0

    for p in prime_set:
        if is_prime(p):
            answer += 1

    return answer
