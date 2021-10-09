'''
프로그래머스(level2) : <전화번호 목록>
'''


from collections import deque

phone_book = ["119", "97674223", "1195524421"]


# 내 풀이 : 효율성 3,4 테스트 통과 X -> 반복문을 줄여야 통과할 수 있다
'''
def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    queue = deque(phone_book)

    for _ in range(len(queue) - 1):
        now = queue.popleft()
        length = len(now)
        for q in queue:
            try:
                if now == q[:length]:
                    return False
            except:
                pass

    return True
'''

# 다른 사람의 풀이 : 반복문 하나를 통한 구현 // queue 필요 X , 정렬을 한 후 두 개씩 비교하는 방법

def solution(phone_book):
    phone_book.sort()

    for i in range(1, len(phone_book)):
        length = len(phone_book[i - 1])
        if phone_book[i][:length] == phone_book[i - 1][:length]:
            return False
    return True




