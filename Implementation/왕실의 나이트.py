'''
구현: <왕실의 나이트>
'''
# 8 X 8
#열 / 행 입력

#1. 내 풀이
'''
now = input()
y = int(now[1])
if now[0]=='a':
    x=1
elif now[0]=='b':
    x=2
elif now[0]=='c':
    x=3
elif now[0]=='d':
    x=4
elif now[0]=='e':
    x=5
elif now[0]=='f':
    x=6
elif now[0]=='g':
    x=7
elif now[0]=='h':
    x=8

print(x,y) #현재위치

knigth_vector = ['A','B','C','D','E','F','G','H'] #8가지
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]
cnt = 0

for i in range(len(knigth_vector)):
    a,b= x,y
    a = a + dx[i]
    b = b + dy[i]
    if 1<=a<=8 and 1<=b<=8:
        cnt = cnt +1

print(cnt)
'''

#2. 해설
#배운점1: 문자로된 현재 위치를 숫자로 변환하는 과정을 아스키 코드 활용
#배운점2: dx,dy 두개의 리스트가 아닌 하나의 리스트로 나이트가 이동할 수 있는 8갸지 방향 정의 가능

now = input()
row = int(now[1])
column = int(ord(now[0])) - int(ord('a')) +1 #ord('a') = 97, ord('b')==98 아스키코드
print(row, column) # 열 , 행

steps = [ (-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1) ]
cnt = 0

for step in steps:
    nr = row + step[0]
    ny = column + step[1]
    if 1<=nr<=8 and 1<=ny<=8:
        cnt = cnt+1

print(cnt)
