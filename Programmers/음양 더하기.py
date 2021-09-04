'''
프로그래머스(level1): <음양 더하기>
'''
absolutes= [4,7,12]
signs = [True,False,True]

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        s = signs[i]
        n = absolutes[i]

        if s == False:
            s = '-'
        else:
            s = '+'

        answer += int(s + str(n))
    return answer
print(solution(absolutes,signs))