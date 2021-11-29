'''
그리디 : <이장님 초대>
'''

n = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
t = trees[0]
for i in range(1,n):
    t = max(t - 1,trees[i])


print(t+n+1)


