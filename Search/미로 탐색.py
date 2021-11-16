n,m = map(int,input().split())
#4,6
wall = [
    [1,1,0,1,1,0],
    [1,1,0,1,1,0],
    [1,1,1,1,1,1],
    [1,1,1,1,0,1]
]

cnt = 0
result = []
def dfs(x,y):
    global cnt

    if x==3 and y==5:
        result.append(cnt)
        return True
    if x>=n or y>=m or x<0 or y<0:

        return False

    if wall[x][y]==1:
        cnt=cnt+1
        wall[x][y]=0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)

        return False
    return False
dfs(0,0)
print(result)
