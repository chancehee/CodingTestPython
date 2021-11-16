'''
프로그래머스(level2): <n^2 배열 자르기>
'''

# 범위가 10^7 까지 이므로 불필요한 부분은 구하기 않고, max(행,열)의 값으로
# 답에 접근 할 수 있는 패턴을 찾아서 구하였다.
n = 3
left = 2
right = 5
def solution(n, left, right):
    # max(행, 열)

    result = []
    for i in range(left, right + 1):
        x = i // n + 1
        y = i % n + 1
        result.append(max(x, y))

    return result

print(solution(n,left,right))





