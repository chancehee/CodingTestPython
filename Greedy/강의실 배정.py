'''
그리디알고리즘: <강의실 배정>
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (1 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.
'''
#시간초과
'''
import sys
import heapq
input = sys.stdin.readline
n = int(input())
cnt = 0
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
print(a)
heapq.heapify(a)


i = 0
x=a[i][0]
y=a[i][1]
j=1
cnt = 0
while True:
    #종료 조건


    if i == len(a)-1:
        break

    if x< a[j][0] <y and a[j][1]>=y:
        j=j+1
    else:
        x=a[j][0]
        y=a[j][1]
        cnt = cnt + 1
        i = j

print(cnt+1)
'''
#큐 자료형 활용
#강의실을 같이 사용못할 때와 같이 사용할 경우의 수를 계산
import sys
import heapq
n = int(input())

timeTable = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue,timeTable[0][1])

for i in range(1,n):
    if queue[0] > timeTable[i][0]:
        heapq.heappush(queue,timeTable[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,timeTable[i][1])
print(len(queue))



