'''
프로그래머스(level1): <콜라츠 추측>
'''

def solution(n):
    cnt = 0
    while (n != 1):
        if cnt == 500:
            return -1
        if n%2==0:
            n = n / 2
        elif n%2==1:
            n = n*3 + 1
        cnt = cnt + 1
    return cnt
print(solution(1))