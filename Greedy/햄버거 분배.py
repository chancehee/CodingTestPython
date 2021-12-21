'''
그리디: <햄버거 분배>
'''

# 아이디어: 왼쪽부터 고르기
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
data = list(input())
cnt = 0

for i,d in enumerate(data):
    if d == 'P':
        if i-k < 0:
            start = 0
        else:
            start = i-k

        if i+k > n-1:
            end = n-1
        else:
            end = i+k
        d = data[start:end+1]

        if 'H' in d:
            index = data[start:end+1].index('H')

            data[index+start] = "X"
            cnt += 1

    else:
        continue

print(cnt)


