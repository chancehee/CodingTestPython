'''
그리디: <등수 매기기>
'''
# 아이디어: 정렬 후 -> 1~n 까지 배열의 숫자에서 차이의 절대값을 다 합해준다.
import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()

s = 0
for i,d in enumerate(data):
    s = s+ abs(i+1 - d)

print(s)




