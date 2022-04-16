"""
브루트포스: <모든 순열>

1. 아이디어:
    DFS + 백트래킹을 통하여 모든 순열 탐색
"""
temp = []
def dfs(cnt):
    global temp

    if cnt == N:
        t = " ".join(temp)
        print(t)
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            temp.append(str(i))
            dfs(cnt+1)
            visited[i] = False
            temp.pop()


N = int(input())
visited = [False] * (N+1)
dfs(0)