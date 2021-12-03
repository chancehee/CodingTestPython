'''
그리디: <스네이크버드>
'''


n, l = map(int,input().split())


data = list(map(int,input().split()))
data.sort()

for i in data:
    if l >= i:
        l += 1
    else:
        break
print(l)


