'''
그리디알고리즘: <행렬>
문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다.
이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3*3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 -> 1, 1 -> 0)

입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
'''

#아이디어: 3X3 부분행렬을 전체 행렬 범위내에서 반복하여 같지 않다면 0과1을 반전시켜 같아지게 끔 구한다

N,M = map(int, input().split())
a = []
b = []
count = 0
for i in range(N):
    a.append(list(map(int, input())))
for i in range(N):
    b.append(list(map(int, input())))


def convertgraph(x,y,arr):
    for i in range(x,x+3):
        for j in range(y,y+3):
            a[i][j] = 1 - a[i][j]


for i in range(N-2):
    for j in range(M-2):
        if a[i][j] != b[i][j]:
            convertgraph(i,j,a)
            count = count + 1

s = False
for i in range(0,N):
    for j in range(0,M):
        if a[i][j] != b[i][j]:
            s = True

if(s):
    print(-1)
else:
    print(count)
