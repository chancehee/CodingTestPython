'''
프로그래머스(level2): <삼각 달팽이>
'''
# 아이디어를 떠올리지 못하여 블로그 글 참조
# 삼각형으로 채우는 것이므로 3가지 경우에 대해서 x,y좌표를 증감시켜주어 숫자를 채워넣는 아이디어

n = 4

arr = [[0]*n for _ in range(n)]

print(arr)
x=-1
y=0
cnt = 1
for i in range(n):
    for j in range(i,n):
        if i%3==0:
            x = x+1
        elif i%3==1:
            y=y+1
        else:
            x=x-1
            y=y-1
        arr[x][y] = cnt
        cnt = cnt + 1
print(arr)

answer = []
for i in arr:
    for j in i:
        if j: # 정확한 문법적의미를 모르겠다..
            print(j)
            answer.append(j)
print(answer)