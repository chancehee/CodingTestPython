'''
프로그래머스(level1): <예산>
'''
d=[1,3,2,5,4]
budget = 9
def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget = budget - d[i]
        if budget == 0:
            return i+1
        if budget < 0:
            return i
    return len(d)

print(solution(d,budget))