'''
프로그래머스(level2): <괄호 변환>

'''

'''
p = "))()(("
u=""
v=""
result = []
def solution(p):

    if p == "":
        return p
    a=0
    b=0



    # u v 분리
    for i in range(len(p)):

        if p[i]=="(":
            a=a+1
        else:
            b=b+1

        if (a>0 and b>0) and a==b:
            u = p[:i+1]
            v = p[i+1:]
            # 올바른 문자열인지 판단하기
            if u[0]=="(":
                result.append(u)
                return solution(v)
            else:
                #u: ))((
                #v: ()
                u=u[1:]
                u=u[:-1]
                table = u.maketrans("()",")(")
                r=u.translate(table)
                u = "("+v+")"+r
                return solution(u)
                return solution(v)
    


print(solution(p))
'''

'''
p = "))(("
u = ""
v = ""
result = ""


def solution(p):
    global result
    
    if p == "":
        return result
    a = 0
    b = 0

    # u v 분리
    for i in range(len(p)):

        if p[i] == "(":
            a = a + 1
        else:
            b = b + 1

        if (a > 0 and b > 0) and a == b:
            u = p[:i + 1]
            v = p[i + 1:]
            # 올바른 문자열인지 판단하기
            if u[0] == "(":
                result=result+u
                return solution(v)
            else:
                # u: ))((
                # v: ()
                u = u[1:]
                u = u[:-1]
                table = u.maketrans("()", ")(")
                r = u.translate(table)
                u = "(" + v + ")" + r
                result = result+ u+v
                return solution(v)


print(solution(p))
'''

# 파이썬에서는 if문에서 empty list는 False를, 비어있지 않다면 True를 리턴한다


p = ")()("

#올바른 괄호인가 판단  / 올바른 괄호란 ( ) 형태
from collections import deque

def is_correct(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif stack: #리스트가 있다면
            stack.pop()
    return not stack #비어있다면 True

def detatch(string):
    str_que = deque(string)
    left , right = 0,0
    u,v= "",""

    while str_que: #큐 내부에 원소가 존재할때까지
        u = u + str_que.popleft()
        if u[-1]=='(':
            left = left + 1
        else:
            right = right + 1

        if left == right:
            break

    v=''.join(list(str_que))
    return u,v

def reverse(u):
    return ''.join([')' if s=='(' else '(' for s in u])


def recursive(string):
    if string=='':
        return ''
    u, v = detatch(string)
    if is_correct(u):
        return u + recursive(v)
    else:
        return '('+ recursive(v)+ ')' + reverse(u[1:-1])


def solution(p):
    return p if is_correct(p) else recursive(p)
print(solution(p))



