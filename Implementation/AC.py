"""
구현: <AC>

1.아이디어:
    예외처리 함수 활용
    R: 거꾸로 뒤집기 (몇개인지로 할지 말지 판단)
    D: popleft()연산
"""
import sys
from collections import deque
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

for i in range(T):
    flag = True
    temp = []
    # 연산자 리스트
    op_list = list(input().strip())
    # 숫자의 개수
    n = int(input())
    # 숫자 리스트
    arr = list(input().strip().split(','))

    if len(arr) == 1 and arr[0] != '[]':
        arr = int(arr[0][1:-1])
        temp.append(arr)
        arr = temp
    else:
        arr[0] = arr[0][1:]
        arr[-1] = arr[-1][:-1]
        if arr[0] != '':
            arr = list(map(int, arr))
        else:
            arr = []

    R_cnt = op_list.count('R')
    q = deque(arr)

    idx = 0
    for i,op in enumerate(op_list):
        if op == 'R':
            if idx == 0:
                idx = -1
            elif idx == -1:
                idx = 0
        elif op == 'D':
            try:
                if idx == 0:
                    q.popleft()
                else:
                    q.pop()
            except:
                print('error')
                flag = False
                break

    if flag:
        # 예외가 없는 경우 -> 정상 출력
        arr = list(q)

        if R_cnt % 2 == 1:
            arr.reverse()
        # 리스트 사이에 공백 제거해주기
        if arr:
            answer = '['
            for i, a in enumerate(arr):
                answer += str(a)
                if i == len(arr) - 1:
                    answer += ']'
                    break
                answer += ','
            print(answer)
        else:
            print('[]')