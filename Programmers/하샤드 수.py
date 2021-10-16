'''
프로그래머스(level1) : <하샤드 수>
'''

# x는 1 ~ 10000
def solution(x):
    s=0
    for i in str(x):
        s += int(i)
    if x%s==0:
        return True
    else:
        return False

print(solution(123))