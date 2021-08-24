'''
비트마스킹: <집합>
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
'''
import sys
input = sys.stdin.readline
M = int(input())
S = set() # 공집합 만들기


for i in range(M):
    list = input().split()
    if list[0] == 'add':
        S.add(int(list[1]))
    elif list[0] == 'remove':
        if int(list[1]) in S:
            S.remove(int(list[1]))
    elif list[0] == 'check':
        if int(list[1]) in S:
            print(1)
        else:
            print(0)
    elif list[0] == 'toggle':
        if int(list[1]) in S:
            S.remove(int(list[1]))
        else:
            S.add(int(list[1]))
    elif list[0] == 'all':
        S = {i for i in range(1,21)}
    elif list[0] == 'empty':
        S = set()




