'''
프로그래머스(level1): <수박수박수>
'''

def solution(n):
    s = {1:'수' , 0:'박'}
    answer = ''
    for i in range(1,n+1):
        answer = answer+s[i%2]
    return answer

print(solution(10000))