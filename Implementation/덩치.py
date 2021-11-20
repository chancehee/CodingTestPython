'''
구현: <덩치>
'''
# 문제 조건이 명확하지 않아서 헤맸다.. 동일 키일경우 몸무게차이가 있다면 덩치의 차이가 있다고 생각했는데
# 무조건 키와 몸무게 둘다 커야지 덩치가 크다는 조건이였다.
import sys
N = int(input())
arr =[]
count_arr = [1 for _ in range(N)]
input = sys.stdin.readline
for i in range(N):
    m,h = map(int, input().split())
    arr.append((m,h))


for i,a in enumerate(arr):

    for j in range(i+1, len(arr)):
        # print(a, 'vs', arr[j])
        if a[0] > arr[j][0] and a[1] > arr[j][1] :

            count_arr[j] = count_arr[j] + 1
        elif a[0] < arr[j][0] and a[1] < arr[j][1]:
            count_arr[i] = count_arr[i] + 1

for c in count_arr:
    print(c, end=" ")







