'''
프로그래머스(level1): <없는 숫자 더하기>
'''

numbers = [1,2,3,4,6,7,8,0]
n = [i for i in range(10)]

# [0,1,2,3,4,6,7,8]
# [0,1,2,3,4,5,6,7,8,9]

a_sub_b = [x for x in n if x not in numbers]
print(sum(a_sub_b))


