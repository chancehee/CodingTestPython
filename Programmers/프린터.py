'''
프로그래머스(level2): <프린터>
'''
from collections import deque
priorities = [1, 1, 9, 1, 1, 1]
loacation = 0
document = [str(i)+'번문서' for i in range(1,len(priorities)+1)]
print(document)
target = document[loacation]
print(target)
q_body = deque(document)

q = deque(priorities)

result = []

while q:
    now = q.popleft()
    body = q_body.popleft()
    if q:
        if now < max(q):
            q.append(now)
            q_body.append(body)
        else:
            result.append(body)
    if not q:
        result.append(body)

print(result)

answer = result.index(target)
print(answer+1)






