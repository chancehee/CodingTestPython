'''
프로그래머스(level1): <다트 게임>
'''

# 내 풀이 : 풀었으나.. 다소 난잡하다..
'''
dartResult = '8S10T*10S'

a= []
what = [0,'S','D','T']
# 문자열 3개로 나누기
# 10 예외처리
dartResult=dartResult.replace('10','K')

for i in range(2):
    if dartResult[2] == '*' or dartResult[2] == '#':
        if dartResult[0] == 'K':
            a.append('10'+dartResult[1:3])
        else:
            a.append(dartResult[:3])
        dartResult = dartResult[3:]
    else:
        if dartResult[0] == 'K':
            a.append('10'+dartResult[1:2])
        else:
            a.append(dartResult[:2])
        dartResult = dartResult[2:]
    if i==1:
        if dartResult[0] == 'K':
            a.append('10'+dartResult[1:])
        else:
            a.append(dartResult)
print(a)
score = [0,0,0]

for i in range(3):
    t_num = ''
    t = a[i]

    for j in range(len(t)):
        if t[j].isdigit():
            t_num = t_num + t[j]
        else:
            break

    if i==0:
        if t[-1] == '*':
            score[i] = (int(t_num) ** what.index(t[-2])) * 2
        elif t[-1] == '#':
            score[i] = -(int(t_num) ** what.index(t[-2]))
        else:
            score[i] = int(t_num) ** what.index(t[-1])
    else:
        if t[-1] == '*':
            score[i-1] = score[i-1] * 2
            score[i] = (int(t_num) ** what.index(t[-2])) * 2
        elif t[-1] == '#':
            score[i] = -(int(t_num) ** what.index(t[-2]))
        else:
            score[i]= int(t_num) ** what.index(t[-1])
print(score)
'''

#다른 사람 풀이
import re #정규 표현식 이용
dartResult = '8S10T*10S'
def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'':1, '*':2, '#':-1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i>0:
            dart[i-1] = dart[i-1]*2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    return sum(dart)

print(solution(dartResult))


