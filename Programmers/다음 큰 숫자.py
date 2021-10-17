'''
프로그래머스(level2): <다음 큰 숫자>
'''

n = 78


def ch(n):
    n_list = []
    while True:
        if n // 2 == 0:
            break
        n_list.append(n % 2)
        n = n // 2
    n_list.append(n)

    cnt = n_list.count(1)
    return cnt


def solution(n):
    a = ch(n)

    while True:
        n = n + 1
        if a == ch(n):
            return n
print(solution(n))


