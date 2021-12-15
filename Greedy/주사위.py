'''
그리디: <주사위>
'''

import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))

# 마주보고 있는 면 고려하기
a = min(dice[0], dice[5])
b = min(dice[1], dice[4])
c = min(dice[2], dice[3])
data = [a,b,c]
data.sort()
first = data[0]
second = data[1]
third = data[2]
# n = 1 일때 예외 처리
if n==1:
    print(sum(dice)-max(dice))
else:
    result = 0
    # 홀수인 경우
    if n%2==1:
        # 뚜껑
        head = (n-2) * (n-2) * first

        # 모서리
        point = (first+second+third) * 4

        # 옆면
        side = (first+second) * 4 * (n-2)

        down_floor = (n-1) * ( (first * (n-2) * 4)  +  (first+second) * 4)

        result = head + point + side + down_floor

        print(result)

    # 짝수인 경우
    else:
        # 뚜껑
        head = (n-2) * (n-2) * first

        # 모서리
        point = (first+second+third) * 4

        # 옆면
        side = (first+second) * (n-2) * 4

        down_floor = (n-1) * (((n-2) * first * 4) + (first+second) * 4 )

        result = head + point + side + down_floor
        print(result)

