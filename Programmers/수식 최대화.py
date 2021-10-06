'''
프로그래머스(level2): 수식 최대화
'''
from itertools import permutations
import re
# 정규표현식을 잘 활용해야 구현문제를 일목요연하게 구현할 수 있다.

expression = '100-200*300-500+20'

# split(패턴, 문자열) // 패턴에서 [] 안에는 나눌 패턴을 뜻하고 ( ) 는 분할 후 포함 한다는 뜻이다.
expression = re.split('([-*+])', expression)
print(expression)

results = []
for operator in list(permutations(['-','*','+'],3)):
    exp = expression[:]
    for op in operator:
        # if 가 아니라 while을 통해 검사하여야 끝까지 해당 연산자를 탐색할 수 있다.
        while op in exp:
            idx = exp.index(op)
            # eval() 함수는 문자열을 계산해주는 함수이다.
            exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1]))
            # del 연산자는 범위를 지정하여 삭제할 수 있다.
            del exp[idx:idx+2]
    results.append(abs(int(exp[0])))
print(max(results))









