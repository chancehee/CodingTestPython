'''
수학: <소수 구하기>
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
 (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

import sys
input = sys.stdin.readline
M,N = map(int, input().split())

def prime_list(a,b):

    Net = [True] * (b+1)
    if a==1:
        Net[1]=False
    m = int(b ** 0.5)
    for i in range(2,m+1):
        if Net[i] == True:
            for j in range(i+i, b+1 , i):
                Net[j] = False

    return [i for i in range(a,b+1) if Net[i]==True]

a = prime_list(M,N)

for i in a:
    print(i)


