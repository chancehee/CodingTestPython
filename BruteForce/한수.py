'''
브루트 포스: <한수>
'''

from collections import deque
n = int(input())

cnt = 0
for i in range(1,n+1):
    if len(str(i)) <= 2:
        cnt += 1
        continue
    # 100 이상일 경우
    queue = deque()
    a = str(i)

    for i in range(1,len(a)):
        diff = int(a[i]) - int(a[i-1])
        if len(queue) == 0:
            queue.append(diff)
        elif queue[-1] == diff:
            queue.append(diff)
        else:
            break

    if len(queue) == len(a)-1:
        cnt += 1

print(cnt)









