'''
수학: <곱셈>
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''
#첫번째 시도: 시간초과
'''
import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())

print((A**B)%C)
'''


'''
import sys
input = sys.stdin.readline
x=0
A,B,C = map(int,input().split())
if B%2==0: #짝수일때
     for i in range(2,B+1,2):
         x = A**i
         if x >= B:
             break

else: #홀수일때
    for i in range(1,B+1,2):
        x = A**i
        if x>=B:
            break


print((A ** x) % C)
'''


import sys
input = sys.stdin.readline
x=0
A,B,C = map(int,input().split())