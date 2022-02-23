'''
그리디: <욱제는 효도쟁이야!!>
'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()
print(sum(a[:-1]))
