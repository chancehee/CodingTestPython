'''
재귀: <리스트 뒤집기>
'''
import sys
# 파이썬 재귀 기본 제한이 1000이므로, 설정을 변경 해준다.
sys.setrecursionlimit(10**6)

my_list = list(map(int, input().split()))

def flip(my_list):
    # base case
    if len(my_list)==1:
        return my_list

    # recurisve case
    return my_list[-1:] + flip(my_list[:-1])

print(flip(my_list))