'''
그리디알고리즘: <회의실 배정>
문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다.
 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
'''

#아이디어: 최소 회의시간 범위를 정하고 이에 비교하여, 안에들어오면 최소 변경 이후일 경우 동 시간대 가장 최소회의 시간을 다음 최소 회의 시간으로 정의



N = int(input())
timetable=[]
for i in range(N):
    timetable.append(list(map(int,input().split())))
timetable.sort()

timetable.append([0,1e9])
timetable.append([0,1e9])

min=timetable[0]
count=1

for i in range(N):
    if min[0]<=timetable[i+1][0]<min[1] and timetable[i+1][1]<=min[1]:
        min= timetable[i+1]

    elif min[1]<=timetable[i+1][0]:
        if timetable[i+1][0]==timetable[i+2][0]:
            if timetable[i+1][1]<=timetable[i+2][1]:
                min = timetable[i+1]
                count=count+1
            else:
                min = timetable[i+2]
                count=count+1
        else:
            min=timetable[i+1]
            count=count+1
    else:
        pass

print(count)