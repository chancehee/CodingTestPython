'''
재귀: <이진 탐색>
'''

import sys

sys.setrecursionlimit(10 ** 6)

my_list = list(map(int, input().split()))
print(my_list)


def binary_search(element, my_list, start, end):
    # base case1
    if start > end:
        return None

    mid = (start + end) // 2

    # base case2
    if my_list[mid] == element:
        return mid

    # recursive case
    elif my_list[mid] > element:
        return binary_search(element, my_list, start, mid - 1)
    elif my_list[mid] < element:
        return binary_search(element, my_list, mid + 1, end)


print(binary_search(3, my_list, 0, len(my_list)-1))
