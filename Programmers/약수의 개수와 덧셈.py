'''
프로그래머스(level1): <약수의 개수와 덧셈>
'''

def divisor_counter(n):
    cnt = 0
    for i in range(1,int(n**(1/2)) + 1):
        if n%i==0:
            cnt = cnt + 1
            if i**2 != n:
                cnt = cnt + 1
    return cnt

def solution(left, right):
    result = 0
    for i in range(left,right+1):
        #짝수일 경우
        if divisor_counter(i)%2==0:
            result = result + i
        else:
            result = result - i
    return result
print(solution(13,17))

