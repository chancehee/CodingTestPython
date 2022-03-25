"""
브루트포스: <부등호>

1. 아이디어:
    중복 X, 순서가 상관있는 숫자의 순열을 모두 생성하여
    부등호가 성립되는 경우를 판단.

2. 시간복잡도:
    (핵심 아이디어: 파이썬 재귀함수의 메모리 구조에 따라, 재귀함수 아래 부분에
    방문 취소 처리 해주기를 통해, 모든 숫자 조합을 탐색한다.)
    BT 기법(DFS)을 통해 재귀 + 가지치기를 하므로
    N! 보다는 적게 걸릴 것 같다.

3. 변수명
    N: 부등호 개수
    arr: 부등호 리스트
    visited: 방문 여부 리스트
    max_ans: 정답 최대 숫자
    min_ans: 정답 최소 숫자
"""


n = int(input())
arr = input().split()
visited = [False] * 10
max_ans = ""
min_ans = ""


# 부등호식이 True 인지 False 인지 판단하는 함수
def possible(a, b, x):
    if x == '<':
        return a < b
    else:
        return a > b


def solve(cnt, s):
    global min_ans, max_ans
    if cnt == n+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return

    for i in range(10):
        if not visited[i]:
            if cnt == 0 or possible(s[-1],str(i), arr[cnt - 1]):
                visited[i] = True
                solve(cnt+1, s + str(i))
                visited[i] = False


solve(0, "")
print(max_ans)
print(min_ans)