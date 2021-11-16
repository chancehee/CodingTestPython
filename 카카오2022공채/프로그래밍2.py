
n=110011
k=4

import math


def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def p(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n, k):
    answer = 0

    num = '101'
    print(num)

    p_list = num.split('0')
    print(p_list)
    if len(p_list)==1:
        if is_prime_number(int(p_list[0])):
            return 1
        else:
            return 0

    if p_list[0] == '':
        pass
    elif is_prime_number(int(p_list[0])) and p_list[0] != '1':
        answer = answer + 1

    if p_list[-1] == '':
        pass
    elif is_prime_number(int(p_list[-1])) and p_list[-1] != '1':
        answer = answer + 1

    for i in range(1, len(p_list) - 1):
        if p_list[i] == '1' or p_list[i] == '':
            continue
        if is_prime_number(int(p_list[i])):
            answer = answer + 1

    return answer

print(solution(n,k))