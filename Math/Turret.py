'''
수학: <터렛>
문제
조규현과 백승환은 터렛에 근무하는 직원이다.
하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다.
다음은 조규현과 백승환의 사진이다.
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다.
조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다.
x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
'''
#수학적 지식 필요
#원 내접 외접 
import sys
import math
input = sys.stdin.readline


T = int(input())

#원의 내접 외접 지식 응용
def location_count(x1,y1,r1,x2,y2,r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dis = [r1,r2,distance]
    m = max(dis)
    dis.remove(m)


    #무한대
    if distance==0 and r1==r2:
        print(-1)

    #한점에서 만날때
    elif (distance == r1 + r2) or m==sum(dis) :
        print(1)

    #만나지 않을때
    elif m > sum(dis):
        print(0)

    #두점에서 만나는 경우
    else:
        print(2)

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    location_count(x1,y1,r1,x2,y2,r2)











