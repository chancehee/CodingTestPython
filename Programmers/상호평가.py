'''
프로그래머스(level1): <상호 평가>
'''

def solution(scores):
    answer = ''

    real = [[] for _ in range(len(scores))]

    for s in scores:
        for i in range(len(s)):
            real[i].append(s[i])


    for i in range(len(scores)):

        real_sum= sum(real[i])
        n = len(real[i])

        if ( scores[i][i] == max(real[i]) and real[i].count(max(real[i]))==1 ) or (scores[i][i] == min(real[i]) and real[i].count(min(real[i]))==1):
            real_sum = real_sum - real[i][i]

            n = n - 1

        if real_sum/n>= 90:
            answer = answer+'A'
        elif real_sum/n>=80:
            answer += 'B'
        elif real_sum/n>=70:
            answer += 'C'
        elif real_sum/n >=50:
            answer += 'D'
        else:
            answer += 'F'

    print(answer)



    return answer

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])


