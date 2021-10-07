'''
프로그래머스(level1): <나누어 떨어지는 숫자 배열>
'''

arr = [5,9,10]
divisor = 5

def solution(arr,divisor):
    result = []
    for a in arr:
        if a%divisor == 0:
            result.append(a)
    result.sort()
    if result:
        return result.sort()
    else:
        result.append(-1)
        return result





