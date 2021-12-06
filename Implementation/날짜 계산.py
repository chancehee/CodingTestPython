'''
구현: <날짜 계산>
'''

E,S,M = map(int, input().split())

x,y,z = 1,1,1
n = 1
while True:
    if x==E and y==S and z==M:
        print(n)
        break
    x += 1
    y += 1
    z += 1

    if x==16:
        x = 1
    if y==29:
        y = 1
    if z==20:
        z = 1
    n += 1