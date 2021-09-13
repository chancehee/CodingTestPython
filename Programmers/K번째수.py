'''
프로그래머스(level1): <k번째수>
'''

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

def solution(array,commands):
    result = []
    for command in commands:

        temp=array[command[0]-1:command[1]]
        temp.sort()
        r = temp[command[2]-1]
        result.append(r)


    return result
print(solution(array,commands))





