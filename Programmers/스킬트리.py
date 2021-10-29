'''
프로그래머스(level2): <스킬트리>
'''
# 내 코드
# 큐 자료구조를 활용하여 선행스킬트리의 활성화 여부를 구현하여 비교한 후 가능한 경우 카운트증가 하는 방식으로 구현하였다.
from collections import deque

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    cnt = 0
    for target in skill_trees:
        queue = deque(target)

        i = 1
        while queue:
            if queue[0] not in skill:
                queue.popleft()
            else:
                if queue[0] in skill[:i]:
                    # 아예 같은 경우
                    if queue[0] == skill[i - 1]:
                        i = i + 1
                        queue.popleft()
                    else:
                        queue.popleft()
                else:
                    break
        if len(queue) == 0:
            cnt += 1
    return cnt
print(solution(skill,skill_trees))


# 다른 사람 코드
# for-else 문 : for문이 실행될 때 break 나 continue 처럼 제어이동이 없는 경우 else문 실행
'''
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
'''











