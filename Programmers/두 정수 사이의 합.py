'''
프로그래머스(level1) : <두 정수 사이의 합>
'''

def solution(a,b):
    x=min(a,b)
    y=max(a,b)
    sum = 0

    for i in range(x,y+1):
        sum = sum + i

    return sum

