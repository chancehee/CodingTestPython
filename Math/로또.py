'''
수학: <로또>
'''
from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    a = list(map(int, input().split()))

    if a[0] == 0:
        break


    s = a[1:]

    ans = list(combinations(s,6))


    for i in ans:
        for j in i:
            print(j,end=" ")
        print()

    print()







