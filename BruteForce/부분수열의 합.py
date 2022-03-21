'''
브루트포스: <부분수열의 합>
'''

# 정수의 개수 / 합
n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

def dfs(i, graph, total):
    global result, s, n
    print(total)
    # if sum(total) == s:
    #     result += 1

    for j in range(i+1, n):
        dfs(j, graph, total+ [graph[j]])

for i in range(0, n):
    dfs(i, nums, [nums[i]])

print(result)
