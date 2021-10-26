'''
프로그래머스(level2) : <구명보트>
'''

# 시간초과 (35/100) pop연산을 사용하여서 시간 초과가 있다고 생각함
'''
from collections import deque
# 5만 명
people = [70,80,50,50]
limit = 100
people.sort()

queue = deque(people)

cnt = 0
while len(queue)>=2:
    if queue[0]+queue[-1]>limit:
        queue.pop()
        cnt = cnt + 1
    elif queue[0]+queue[-1]==limit:
        queue.pop()
        queue.popleft()
        cnt = cnt + 1

if queue:
    cnt = cnt + 1

print(cnt)
'''

# pop연산 없이 값 비교만을 통하여 해결
people = [70,80,50,50]
limit = 100
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    if left == right:
        answer += 1

    return answer
print(solution(people,limit))