'''
프로그래머스(level1): <같은 숫자는 싫어>
'''
arr = [1,1,1,0,0,1,1]

def solution(arr):
    list_a = list(map(str, arr))
    a = ''.join(list_a)
    for i in range(10):
        while(str(i)+str(i) in a):
            a = a.replace(str(i)+str(i), str(i))
    return list(map(int,a))
print(solution(arr))


