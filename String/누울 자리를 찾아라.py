'''
문자열: <누울 자리를 찾아라>
'''

n = int(input())
graph = []
for i in range(n):
    graph.append(input())


x = 0
y = 0
cnt = 0
cnt2 = 0

for i in range(n):
    x = 0
    y=0
    for j in range(n):
        if graph[i][j] == '.':
            x += 1
            if j== n-1:
                if x>1:
                    cnt += 1

        else:
            if x>1:
                cnt += 1
            x = 0


        if graph[j][i] == '.':
            y += 1
            if j==n-1:
                if y>1:
                    cnt2 += 1
        else:
            if y >1:
                cnt2 += 1
            y= 0

print(cnt, cnt2)







