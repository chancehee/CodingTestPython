'''
프로그래머스(level1): <문자열 내 p와 y의 개수>
'''

def solution(s):
    s = s.lower()
    cnt1 = s.count('p')
    cnt2 = s.count('y')
    return (cnt1==cnt2)

print(solution('PyY'))
