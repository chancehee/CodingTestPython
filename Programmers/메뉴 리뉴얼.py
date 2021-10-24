'''
프로그래머스(level2) : <메뉴 리뉴얼>
'''
# 아이디어: 조합을 사용하여 코스수에 따른 조합을 구하고, XY YX 이런경우를 같은 원소로 처리 하기위해
#       person 각 원소를 정렬한 후 조합하고, dict() 자료형을 통해서 카운트를 누적 시켜주고,
#       리스트 컴프리핸션을 통해서 주문횟수가 2이상인 경우에서 max() 값을 구하여 최종 후보
#       배열에 추가시켜 준다.

import itertools
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

def solution(orders, course):
    result = []
    for c in course:
        D = dict()
        for person in orders:
            # 정렬을 하지 않으면 XY YX 이렇게 같은원소를 다르게 저장하기 때문에 정렬시킨다.
            person = list(person)
            person.sort()
            person = ''.join(person)

            # 코스 수에 따른 조합
            p = list(map(''.join, itertools.combinations(person, c)))
            for i in p:
                if i not in D:
                    D[i] = 1
                else:
                    D[i] += 1

        # max 개수랑 맞는지 그리고 개수가 2이상인지 확인하여 반환
        r = [k for k, v in D.items() if max(D.values()) == v and v > 1]
        for i in r:
            result.append(i)

    result.sort()
    return result

print(solution(orders,course))


