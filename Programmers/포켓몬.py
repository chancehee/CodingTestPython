'''
프로그래머스(level1): <포켓몬>

'''
# set(list) -> list를 집합자료형으로 변환

nums = [1,2,3,4]

def solution(nums):
    n = int(len(nums)/2)
    nums_dic = set(nums)
    n_dic = len(nums_dic)

    if n<= n_dic:
        return n
    else:
        return n_dic

print(solution(nums))


